from fastapi import APIRouter, HTTPException

from src.database import get_next_id, players
from src.models import Player

router = APIRouter(prefix="/players", tags=["players"])


@router.get("/")
def list_players() -> list[Player]:
    return players


@router.post("/")
def create_player(player: Player) -> Player:
    player.id = get_next_id(players)
    players.append(player)
    return player


@router.get("/{player_id}")
def get_player(player_id: int) -> Player:
    for player in players:
        if player.id == player_id:
            return player

    raise HTTPException(status_code=404, detail="Player not found")
