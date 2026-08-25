# AgroGeo

Projeto de geotecnologia aplicado ao agronegócio, combinando desenvolvimento backend, banco geoespacial e sensoriamento remoto.

## Stack inicial

- Python 3.12
- FastAPI
- PostgreSQL 16
- PostGIS
- SQLAlchemy 2
- GeoAlchemy2
- Alembic
- Docker / Docker Compose

## Objetivo do projeto

Construir uma API capaz de cadastrar propriedades e talhões, armazenar geometrias no PostGIS, integrar dados com QGIS e posteriormente processar imagens de satélite para cálculo de NDVI.

## Roadmap

- [x] Estrutura inicial da API
- [x] PostgreSQL + PostGIS via Docker
- [x] Modelo geoespacial inicial de talhão
- [ ] Migrations com Alembic
- [ ] CRUD de propriedades e talhões
- [ ] Entrada e saída em GeoJSON
- [ ] Cálculo de área em hectares
- [ ] Conexão do QGIS com PostGIS
- [ ] Consultas espaciais
- [ ] Sentinel-2
- [ ] NDVI
- [ ] Histórico de NDVI por talhão

## Como rodar

1. Copie o arquivo de ambiente:

```bash
cp .env.example .env
```

No Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

2. Suba os containers:

```bash
docker compose up --build
```

3. Abra:

- API: http://localhost:8000
- Swagger: http://localhost:8000/docs
- Healthcheck: http://localhost:8000/health

## Estrutura

```text
app/
├── api/
├── core/
├── db/
├── models/
├── schemas/
├── services/
└── main.py
```
