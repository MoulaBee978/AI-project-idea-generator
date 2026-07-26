from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.langchain_service import LangChainService

router = APIRouter()


class GenerateRequest(BaseModel):
    domain: str
    language: str
    tech_stack: str
    difficulty: str


class GenerateResponse(BaseModel):
    projects: list


@router.post("/generate-projects", response_model=GenerateResponse)
async def generate_projects(req: GenerateRequest):
    try:
        svc = LangChainService()
        projects = await svc.generate_ideas(
            domain=req.domain,
            language=req.language,
            tech_stack=req.tech_stack,
            difficulty=req.difficulty,
        )
        return {"projects": projects}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
