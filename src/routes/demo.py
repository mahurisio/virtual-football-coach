from fastapi import APIRouter

from src.database import evaluations, matches, players
from src.models import Match, Player, PlayerEvaluation, PlayerPosition, PreferredFoot

router = APIRouter(prefix="/demo", tags=["demo"])


@router.post("/load-sample-data")
def load_sample_data() -> dict[str, str | int]:
    """Load sample players, one game and basic evaluations for testing."""

    players.clear()
    matches.clear()
    evaluations.clear()

    player_one = Player(
        id=1,
        full_name="Juan Perez",
        age=14,
        position=PlayerPosition.MIDFIELDER,
        preferred_foot=PreferredFoot.RIGHT,
        team="Colegio Manizales",
        notes="Jugador con buena vision de juego y margen de mejora en recuperacion.",
    )

    player_two = Player(
        id=2,
        full_name="Carlos Ramirez",
        age=15,
        position=PlayerPosition.DEFENDER,
        preferred_foot=PreferredFoot.LEFT,
        team="Colegio Manizales",
        notes="Defensa fuerte en duelos, debe mejorar salida con balon.",
    )

    game = Match(
        id=1,
        opponent="Colegio Rival",
        team_goals=2,
        opponent_goals=1,
        notes="Partido de prueba para validar el sistema.",
    )

    evaluation_one = PlayerEvaluation(
        id=1,
        player_id=1,
        match_id=1,
        minutes_played=70,
        goals=1,
        assists=1,
        successful_passes=32,
        failed_passes=8,
        recoveries=4,
        duels_won=5,
        coach_rating=8.0,
        technical_notes="Buen partido ofensivo. Debe mejorar recuperacion defensiva.",
    )

    evaluation_two = PlayerEvaluation(
        id=2,
        player_id=2,
        match_id=1,
        minutes_played=80,
        goals=0,
        assists=0,
        successful_passes=18,
        failed_passes=12,
        recoveries=7,
        duels_won=9,
        coach_rating=7.2,
        technical_notes="Solido en defensa, pero con baja precision en salida.",
    )

    players.extend([player_one, player_two])
    matches.append(game)
    evaluations.extend([evaluation_one, evaluation_two])

    return {
        "message": "Sample data loaded",
        "players": len(players),
        "games": len(matches),
        "evaluations": len(evaluations),
    }
