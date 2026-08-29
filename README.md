# AgroGeo

Projeto de geoprocessamento aplicado ao agronegócio, unindo backend, banco espacial e ferramentas GIS.

## Tecnologias

* Python
* FastAPI
* PostgreSQL/PostGIS
* SQLAlchemy
* GeoAlchemy2
* Alembic
* Docker
* QGIS

## Funcionalidades atuais

* Cadastro de talhões via GeoJSON
* Armazenamento de geometrias `Polygon` no PostGIS
* SRID 4326
* Índice espacial GiST
* Listagem de talhões
* Consulta por ID
* Conversão PostGIS → GeoJSON
* Cálculo de área em hectares

## Exemplo

```json
{
  "name": "Talhao Teste",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [-54.585, -25.516],
        [-54.580, -25.516],
        [-54.580, -25.510],
        [-54.585, -25.510],
        [-54.585, -25.516]
      ]
    ]
  }
}
```

## Endpoints

```text
POST /fields
GET  /fields
GET  /fields/{id}
```

Swagger:

```text
http://localhost:8000/docs
```

## Executando

```bash
docker compose up -d --build
```

## Arquitetura

```text
FastAPI
   ↓
PostgreSQL + PostGIS
   ↑
  QGIS
```

## Próximos passos

* [ ] Integração com QGIS
* [ ] Mapas temáticos
* [ ] Consultas espaciais avançadas
* [ ] Sentinel-2
* [ ] NDVI
* [ ] SAVI

## Objetivo

Aprofundar conhecimentos em desenvolvimento de software, geoprocessamento, bancos de dados espaciais e sensoriamento remoto aplicados ao agronegócio.