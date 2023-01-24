from fastapi import FastAPI, Query
from schemas import Request, Word
from typing import List
import collections

app = FastAPI()

@app.post('/request')
def post_name(list1: List[str] = Query([])):
    list2 = [item for item, count in collections.Counter(list1).items() if count > 1]
    list3 = [x.lower() for x in list1]
    list4 = [x.lower() for x in list2]
    result = list(set(list3) ^ set(list4))
    return result
