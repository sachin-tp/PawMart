from fastapi import APIRouter

from app.crud.operations import create_pet, get_pets
from app.schemas.schemas import PetCreate, PetResponse


router = APIRouter(
    prefix="/pets",
    tags=["Pets"],
)


@router.post("/", response_model=PetResponse)
def add_pet(pet_data: PetCreate):
    return create_pet(pet_data)


@router.get("/", response_model=list[PetResponse])
def get_all_pets():
    return get_pets()