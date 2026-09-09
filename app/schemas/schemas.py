from pydantic import BaseModel, ConfigDict

class PetCreate(BaseModel):
    name: str
    species: str
    breed: str
    age: int
    price: float
    is_available: bool = True

class PetResponse(PetCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)