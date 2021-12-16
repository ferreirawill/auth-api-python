import uvicorn
from src.services.database.connection import DatabaseConnection

if __name__ == "__main__":
    instance = DatabaseConnection.getInstance()
    uvicorn.run("app:app", host="0.0.0.0", port=7000, http="h11")