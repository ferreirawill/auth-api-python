from fastapi import FastAPI
from src.routers.base import router as BaseRoute
from src.routers.users import router as UserRoute
from src.routers.company import router as CompanyRoute
from src.routers.groups import router as GroupRoute
app = FastAPI(title="NUC USER API")


app.include_router(UserRoute,tags=["User - Gestão de usuários"],prefix="/user")
app.include_router(CompanyRoute,tags=["Company - Gestão de empresas"],prefix="/company")
app.include_router(GroupRoute,tags=["Group - Gestão de grupos"],prefix="/group")
app.include_router(BaseRoute,tags=["Base URL - KeepAlive da API"])