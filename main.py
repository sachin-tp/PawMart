from app.database.connection import get_connection

connection = get_connection()

print("Database connection established successfully!")

connection.close()