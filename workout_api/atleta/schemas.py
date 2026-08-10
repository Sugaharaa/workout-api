from typing import Annotated

from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do atleta",
            examples=["João"],
            max_length=50,
        ),
    ]

    cpf: Annotated[
        str,
        Field(
            description="CPF do atleta sem pontos",
            examples=["12345678911"],
            min_length=11,
            max_length=11,
        ),
    ]

    idade: Annotated[
        int,
        Field(
            description="Idade do atleta",
            examples=[20],
            gt=0,
        ),
    ]

    peso: Annotated[
        PositiveFloat,
        Field(
            description="Peso do atleta",
            examples=[63.5],
        ),
    ]

    altura: Annotated[
        PositiveFloat,
        Field(
            description="Altura do atleta em centímetros",
            examples=[173],
        ),
    ]

    sexo: Annotated[
        str,
        Field(
            description="Sexo do atleta",
            examples=["M"],
            min_length=1,
            max_length=1,
        ),
    ]

    categoria_id: int
    centro_treinamento_id: int


class AtletaOut(Atleta):
    pk_id: int


class AtletaListOut(BaseSchema):
    nome: str
    centro_treinamento: str
    categoria: str