from fastapi import FastAPI, File, UploadFile, Depends
import pandas as pd  #type:ignore
from .models import SampleData
from .crud import create_sample_data
from .database import get_session, create_db_and_tables
from sqlmodel import Session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), session: Session = Depends(get_session)):
    # Load Excel file into a DataFrame
    df = pd.read_excel(file.file)
    
    # Iterate over rows and insert data into the database
    for _, row in df.iterrows():
        data = SampleData(
            name=row['name'],  # Adjust the column names according to your file
            age=row['age'],
            city=row['city']
        )
        create_sample_data(session, data)
    
    return {"message": "Data uploaded and saved to database successfully"}
