from typing import Annotated

from pydantic import Field

from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Informe o nome do CT",
            examples=["CT Moura Brasil"],
            max_length=50
        )
    ]

    endereco: Annotated[
        str,
        Field(
            description="Informe o endereço do CT",
            examples=["Av. Principal, 123"],
            max_length=50
        )
    ]

    proprietario: Annotated[
        str,
        Field(
            description="Informe o proprietário do CT",
            examples=["Luiz Gonzaga"],
            max_length=50
        )
    ]


class CentroTreinamentoOut(CentroTreinamento):
    pk_id: int