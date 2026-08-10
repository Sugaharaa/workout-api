from typing import Annotated

from pydantic import Field

from workout_api.contrib.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Informe a categoria",
            examples=["Natação"],
            max_length=50
        )
    ]


class CategoriaOut(Categoria):
    pk_id: int