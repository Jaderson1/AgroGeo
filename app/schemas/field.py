from pydantic import BaseModel, ConfigDict


class FieldBase(BaseModel):
    name: str


class FieldRead(FieldBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
