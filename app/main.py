from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="AgroGeo API",
    version="0.1.0",
    description="API geoespacial para propriedades rurais, talhões e análises agrícolas.",
)

app.include_router(router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "AgroGeo API is running"}
