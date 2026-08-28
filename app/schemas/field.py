from typing import Literal

from pydantic import BaseModel, Field, field_validator


class PolygonGeoJSON(BaseModel):
    """Um Polygon no formato GeoJSON (RFC 7946)."""

    type: Literal["Polygon"]
    coordinates: list[list[list[float]]]

    @field_validator("coordinates")
    @classmethod
    def validar_aneis(cls, coordinates: list[list[list[float]]]) -> list[list[list[float]]]:
        if not coordinates:
            raise ValueError("Polygon precisa de pelo menos um anel (ring).")

        for ring in coordinates:
            if len(ring) < 4:
                raise ValueError(
                    "Cada anel precisa de pelo menos 4 posições (incluindo o "
                    "ponto de fechamento)."
                )
            if ring[0] != ring[-1]:
                raise ValueError(
                    "O anel precisa ser fechado: o primeiro e o último ponto "
                    "devem ser idênticos."
                )
            for posicao in ring:
                if len(posicao) != 2:
                    raise ValueError(
                        "Cada posição deve ter exatamente 2 valores: [longitude, latitude]."
                    )

        return coordinates


class FieldCreate(BaseModel):
    """Payload de entrada do POST /fields."""

    name: str = Field(min_length=1, max_length=120)
    geometry: PolygonGeoJSON


class FieldRead(BaseModel):
    """Talhão retornado pela API."""

    id: int
    name: str
    geometry: PolygonGeoJSON