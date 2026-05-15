from fastapi import APIRouter

from src.database import get_next_id, matches
from src.models import Match

router = APIRouter(prefix="/games", tags=["games"])


@router.get("/")
def list_games() -> list[Match]:
    return matches


@router.post("/")
def create_game(game: Match) -> Match:
    game.id = get_next_id(matches)
    matches.append(game)
    return game
