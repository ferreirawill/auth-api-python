from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def baseUrl():
    return "Hello World"
