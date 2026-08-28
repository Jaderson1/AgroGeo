import json

from fastapi import APIRouter, Depends, HTTPException, status
from geoalchemy2 import Geography
from sqlalchemy import cast, func, insert, select
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.field import Field
from app.schemas.field import FieldCreate, FieldRead

router = APIRouter(prefix="/fields", tags=["fields"])


def _area_hectares_expr():
    return (func.ST_Area(cast(Field.geometry, Geography)) / 10000).label("area_hectares")


@router.post("", response_model=FieldRead, status_code=status.HTTP_201_CREATED)
def create_field(payload: FieldCreate, db: Session = Depends(get_db)) -> FieldRead:
    geojson_str = payload.geometry.model_dump_json()

    stmt = (
        insert(Field)
        .values(
            name=payload.name,
            geometry=func.ST_SetSRID(func.ST_GeomFromGeoJSON(geojson_str), 4326),
        )
        .returning(Field.id, _area_hectares_expr())
    )

    result = db.execute(stmt).one()
    db.commit()

    return FieldRead(
        id=result.id,
        name=payload.name,
        geometry=payload.geometry,
        area_hectares=result.area_hectares,
    )


def _row_to_field_read(row) -> FieldRead:
    return FieldRead(
        id=row.id,
        name=row.name,
        geometry=json.loads(row.geometry_geojson),
        area_hectares=row.area_hectares,
    )


@router.get("", response_model=list[FieldRead])
def list_fields(db: Session = Depends(get_db)) -> list[FieldRead]:
    stmt = select(
        Field.id,
        Field.name,
        func.ST_AsGeoJSON(Field.geometry).label("geometry_geojson"),
        _area_hectares_expr(),
    ).order_by(Field.id)

    rows = db.execute(stmt).all()
    return [_row_to_field_read(row) for row in rows]


@router.get("/{field_id}", response_model=FieldRead)
def get_field(field_id: int, db: Session = Depends(get_db)) -> FieldRead:
    stmt = select(
        Field.id,
        Field.name,
        func.ST_AsGeoJSON(Field.geometry).label("geometry_geojson"),
        _area_hectares_expr(),
    ).where(Field.id == field_id)

    row = db.execute(stmt).first()
    if row is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Talhão não encontrado.",
        )

    return _row_to_field_read(row)