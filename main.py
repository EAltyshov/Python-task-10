from fastapi import FastAPI, Query, UploadFile, HTTPException, File
from typing import List
import collections, os, os.path
from fastapi.responses import FileResponse
import schemas


app = FastAPI()

@app.post('/filter/case_sensitive')
def family(list1: List[str] = Query([])):
    list2 = [item for item, count in collections.Counter(list1).items() if count > 1]
    list3 = [x.lower() for x in list1]
    list4 = [x.lower() for x in list2]
    result = list(set(list3) ^ set(list4))
    return result
@app.post("/upload/{filename}")
def accumulate_files(files: list[UploadFile], filename: str):
    error_files = []
    for file in files:
        if not file.filename.endswith((".csv", ".json")):
            error_files.append(file.filename)
    if error_files:
        raise HTTPException(status_code=415, detail=error_files)
    schemas.accum_files(files, filename)
    return {"filename": filename}



@app.post("/load/{filename}")
def load_file(filename: str):
    path = os.path.join('data/', filename)
    if os.path.isfile(path):
        return FileResponse(path)
    else:
        raise HTTPException(status_code=404, detail="file not found: " + filename)

@app.post("/upload/<file_name>")
def upload_file(file: UploadFile = File(...)):
    error_files = "Wrong format: .csv, .json"
    if file.filename.endswith((".csv", ".json")):
        with open(f'{file.filename}', 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"file": file}
    else:
        raise HTTPException(status_code=415, detail=error_files)