from typing import List
from pydantic import BaseModel
from datetime import date

class Word(BaseModel):
    name: str

class Request(BaseModel):
    words: List[Word]