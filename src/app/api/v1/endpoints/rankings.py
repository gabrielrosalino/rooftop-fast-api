from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Any

router = APIRouter(prefix="/rankings")


class RankingOut(BaseModel):
    id: int
    title: str
    author: str


@router.get("/", response_model=List[RankingOut])
def read_rankings() -> Any:
    """Retrive rankings"""
    return [
        RankingOut(id=1, title="Top Guitarrist of All time", author="John Doe"),
    ]
