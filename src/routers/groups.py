from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Lê todos os grupos")
async def getGroups():
    return "William Ferreira"


@router.get("/{id}", summary="Lê grupos por ID")
async def getGroups(id: int):
    return "William Ferreira"


@router.post("/",summary="Cria novo grupo")
async def postGroup():
    return "Cria usuário"


@router.put("/{id}",summary="Atualiza um grupo existente")
async def putGroup(id: int):
    return "Atualiza usuário"


@router.delete("/{id}",summary="Deleta um grupo existente")
async def deleteGroup(id: int):
    return "Deleta usuário"
