from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud.operations import create_pet, get_pets
from app.database.connection import get_db
from app.schemas.schemas import PetCreate, PetResponse

router = APIRouter(
    prefix="/pets", tags=["pets"]
    )

# Create a new pet
@router.post("/", response_model=PetResponse)
def add_pet(
    pet_data: PetCreate,
    db: Session = Depends(get_db),
):
    return create_pet(db, pet_data)

# Get all pets
@router.get("/", response_model=list[PetResponse])
def get_all_pets(db: Session = Depends(get_db)):
    return get_pets(db)