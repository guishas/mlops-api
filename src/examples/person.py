from typing import Annotated
from fastapi import Body

from models.person import Person

PersonExample = Annotated[
  Person,
  Body(
    examples=[
      {
        "age": 42,
        "job": "entrepreneur",
        "marital": "married",
        "education": "primary",
        "balance": 558,
        "housing": "yes",
        "duration": 186,
        "campaign": 2
      }
    ],
  )
]