from fastapi import APIRouter, Depends, status
from sqlalchemy import func, insert
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.field import Field
from app.schemas.field import FieldCreate, FieldRead

router = APIRouter(prefix="/fields", tags=["fields"])


@router.post("", response_model=FieldRead, status_code=status.HTTP_201_CREATED)
def create_field(payload: FieldCreate, db: Session = Depends(get_db)) -> FieldRead:
    geojson_str = payload.geometry.model_dump_json()

    stmt = (
        insert(Field)
        .values(
            name=payload.name,
            geometry=func.ST_SetSRID(func.ST_GeomFromGeoJSON(geojson_str), 4326),
        )
        .returning(Field.id)
    )

    new_id = db.execute(stmt).scalar_one()
    db.commit()

    return FieldRead(id=new_id, name=payload.name, geometry=payload.geometry)