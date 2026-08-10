from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from workout_api.categorias.models import CategoriaModel
from workout_api.categorias.schemas import Categoria, CategoriaOut
from workout_api.contrib.repository.dependencies import get_session


router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
    categoria: Categoria,
    db_session: AsyncSession = Depends(get_session),
):
    categoria_model = CategoriaModel(
        nome=categoria.nome
    )

    db_session.add(categoria_model)

    try:
        await db_session.commit()

    except IntegrityError:
        await db_session.rollback()

        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f"Já existe uma categoria cadastrada com o nome: {categoria.nome}",
        )

    await db_session.refresh(categoria_model)

    return categoria_model


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut],
)
async def get_all(
    db_session: AsyncSession = Depends(get_session),
):
    query = select(CategoriaModel)

    result = await db_session.execute(query)

    categorias = result.scalars().all()

    return categorias