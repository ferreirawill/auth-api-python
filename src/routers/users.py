from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Lê todos usuários")
async def getUser():
    return "William Ferreira"


@router.get("/{id}", summary="Lê usuários por ID")
async def getUser():
    return "William Ferreira"


@router.post("/",summary="Cria novo usuario")
async def postUser():
    return "Cria usuário"


@router.put("/{id}",summary="Atualiza um usuário existente")
async def putUser():
    return "Atualiza usuário"


@router.delete("/{id}",summary="Deleta um usuário existente")
async def deleteUser():
    return "Deleta usuário"
