# from typing import Union

# from fastapi import FastAPI

# app = FastAPI()
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]



# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
# #path
# @app.get("/hello")
# def dv_root():
#     return {"Hello": "World"}


# # Query Parameter
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}