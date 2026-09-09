from app.database.connection import get_db_connection
from app.schemas.schemas import PetCreate


def create_pet(pet_data: PetCreate) -> dict:
    query = """
        INSERT INTO pets
        (name, species, breed, age, price, is_available)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id, name, species, breed, age, price, is_available;
    """

    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                query,
                (
                    pet_data.name,
                    pet_data.species,
                    pet_data.breed,
                    pet_data.age,
                    pet_data.price,
                    pet_data.is_available,
                ),
            )

            row = cursor.fetchone()

            return {
                "id": row[0],
                "name": row[1],
                "species": row[2],
                "breed": row[3],
                "age": row[4],
                "price": row[5],
                "is_available": row[6],
            }


def get_pets() -> list[dict]:
    query = """
        SELECT id, name, species, breed, age, price, is_available
        FROM pets
        ORDER BY id;
    """

    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)

            rows = cursor.fetchall()

            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "species": row[2],
                    "breed": row[3],
                    "age": row[4],
                    "price": row[5],
                    "is_available": row[6],
                }
                for row in rows
            ]