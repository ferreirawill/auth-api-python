from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Lê todas as empresas")
async def getCompany():
    return "William Ferreira"


@router.get("/{id}", summary="Lê empresas por ID")
async def getCompany(id: int):
    return "William Ferreira"


@router.post("/",summary="Cria nova empresa")
async def postCompany():
    return "Cria usuário"


@router.put("/{id}",summary="Atualiza uma empresa existente")
async def putCompany(id: int):
    return "Atualiza usuário"


@router.delete("/{id}",summary="Deleta uma empresa existente")
async def deleteCompany():
    return "Deleta usuário"
