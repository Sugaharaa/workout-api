from fastapi import FastAPI
from fastapi_pagination import add_pagination

from workout_api.atleta.controller import router as atleta_router
from workout_api.categorias.controller import router as categorias_router
from workout_api.centro_treinamento.controller import (
    router as centro_treinamento_router,
)


app = FastAPI(
    title="WorkoutApi"
)


app.include_router(
    categorias_router,
    prefix="/categorias",
    tags=["categorias"],
)


app.include_router(
    centro_treinamento_router,
    prefix="/centros-treinamento",
    tags=["centros de treinamento"],
)


app.include_router(
    atleta_router,
    prefix="/atletas",
    tags=["atletas"],
)


add_pagination(app)