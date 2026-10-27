from dataclasses import dataclass
from app.models.breed import Breed
from app.models.pet_type import PetType

@dataclass
class Pet:
    id: int
    name: str
    breed: Breed
    pet_type: PetType
    age: int
    price: float
    is_available: bool