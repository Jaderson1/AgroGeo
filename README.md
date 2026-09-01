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
* Uso do SRID 4326
* Índice espacial GiST
* Listagem de talhões
* Consulta de talhão por ID
* Conversão PostGIS → GeoJSON
* Cálculo de área em hectares
* Integração do PostGIS com QGIS
* Visualização dos talhões sobre mapa base OpenStreetMap

## Exemplo de talhão

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

## Executando o projeto

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
               ↓
         OpenStreetMap
```

A API e o QGIS utilizam o mesmo banco PostGIS como fonte de dados.

## Status

* [x] FastAPI
* [x] PostgreSQL/PostGIS
* [x] Docker
* [x] GeoJSON
* [x] Polygon com SRID 4326
* [x] Índice espacial GiST
* [x] Cálculo de área em hectares
* [x] Integração com QGIS
* [x] Visualização sobre OpenStreetMap
* [ ] Mapas temáticos
* [ ] Consultas espaciais avançadas
* [ ] Imagens Sentinel-2
* [ ] NDVI
* [ ] SAVI

## Próximos passos

* Criar mapas temáticos no QGIS
* Explorar consultas espaciais com PostGIS
* Trabalhar com dados raster
* Integrar imagens Sentinel-2
* Calcular NDVI e SAVI
* Relacionar indicadores de vegetação aos talhões

## Objetivo

Aprofundar conhecimentos em desenvolvimento de software, bancos de dados espaciais, geoprocessamento e sensoriamento remoto aplicados ao agronegócio.
