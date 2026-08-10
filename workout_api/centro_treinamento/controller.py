from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import (
    CentroTreinamento,
    CentroTreinamentoOut,
)
from workout_api.contrib.repository.dependencies import get_session


router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CentroTreinamentoOut,
)
async def post(
    centro_treinamento: CentroTreinamento,
    db_session: AsyncSession = Depends(get_session),
):
    centro_treinamento_model = CentroTreinamentoModel(
        nome=centro_treinamento.nome,
        endereco=centro_treinamento.endereco,
        proprietario=centro_treinamento.proprietario,
    )

    db_session.add(centro_treinamento_model)

    try:
        await db_session.commit()

    except IntegrityError:
        await db_session.rollback()

        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=(
                "Já existe um centro de treinamento "
                f"cadastrado com o nome: {centro_treinamento.nome}"
            ),
        )

    await db_session.refresh(centro_treinamento_model)

    return centro_treinamento_model


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[CentroTreinamentoOut],
)
async def get_all(
    db_session: AsyncSession = Depends(get_session),
):
    query = select(CentroTreinamentoModel)

    result = await db_session.execute(query)

    centros_treinamento = result.scalars().all()

    return centros_treinamento