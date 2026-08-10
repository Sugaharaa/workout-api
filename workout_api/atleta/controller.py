from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import LimitOffsetPage
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from workout_api.atleta.models import AtletaModel
from workout_api.atleta.schemas import Atleta, AtletaListOut, AtletaOut
from workout_api.categorias.models import CategoriaModel
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.contrib.repository.dependencies import get_session


router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def post(
    atleta: Atleta,
    db_session: AsyncSession = Depends(get_session),
):
    atleta_model = AtletaModel(
        nome=atleta.nome,
        cpf=atleta.cpf,
        idade=atleta.idade,
        peso=atleta.peso,
        altura=atleta.altura,
        sexo=atleta.sexo,
        categoria_id=atleta.categoria_id,
        centro_treinamento_id=atleta.centro_treinamento_id,
    )

    db_session.add(atleta_model)

    try:
        await db_session.commit()

    except IntegrityError:
        await db_session.rollback()

        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=(
                "Já existe um atleta cadastrado "
                f"com o cpf: {atleta.cpf}"
            ),
        )

    await db_session.refresh(atleta_model)

    return atleta_model


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=LimitOffsetPage[AtletaListOut],
)
async def get_all(
    nome: str | None = None,
    cpf: str | None = None,
    db_session: AsyncSession = Depends(get_session),
):
    query = (
        select(
            AtletaModel.nome.label("nome"),
            CentroTreinamentoModel.nome.label(
                "centro_treinamento"
            ),
            CategoriaModel.nome.label("categoria"),
        )
        .join(
            CentroTreinamentoModel,
            AtletaModel.centro_treinamento_id
            == CentroTreinamentoModel.pk_id,
        )
        .join(
            CategoriaModel,
            AtletaModel.categoria_id
            == CategoriaModel.pk_id,
        )
    )

    if nome:
        query = query.where(
            AtletaModel.nome == nome
        )

    if cpf:
        query = query.where(
            AtletaModel.cpf == cpf
        )

    return await paginate(
        db_session,
        query,
    )