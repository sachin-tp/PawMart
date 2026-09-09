from sqlalchemy.orm import Session
from app.models.models import Pet
from app.schemas.schemas import PetCreate

# Create Operation
def create_pet(db: Session, pet_data: PetCreate) -> Pet:
    new_pet = Pet(
        name=pet_data.name,
        species=pet_data.species,
        breed=pet_data.breed,
        age=pet_data.age,
        price=pet_data.price,
        is_available=pet_data.is_available
    )
    db.add(new_pet)
    db.commit()
    db.refresh(new_pet)
    return new_pet

# Read Operation
def get_pets(db: Session) -> list[Pet]:
    return db.query(Pet).all()