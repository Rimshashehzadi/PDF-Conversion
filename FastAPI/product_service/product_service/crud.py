from sqlmodel import Session
from .models import SampleData

def create_sample_data(session: Session, data: SampleData):
    session.add(data)
    session.commit()
    session.refresh(data)
    return data
