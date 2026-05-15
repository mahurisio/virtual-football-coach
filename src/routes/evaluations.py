from fastapi import APIRouter, HTTPException

from src.database import evaluations, get_next_id, players
from src.models import PlayerEvaluation, Recommendation

router = APIRouter(prefix="/evaluations", tags=["evaluations"])


@router.get("/")
def list_evaluations() -> list[PlayerEvaluation]:
    return evaluations


@router.post("/")
def create_evaluation(evaluation: PlayerEvaluation) -> PlayerEvaluation:
    player_exists = any(player.id == evaluation.player_id for player in players)

    if not player_exists:
        raise HTTPException(status_code=400, detail="Player does not exist")

    evaluation.id = get_next_id(evaluations)
    evaluations.append(evaluation)
    return evaluation


@router.get("/{player_id}/recommendation")
def get_player_recommendation(player_id: int) -> Recommendation:
    player_evaluations = [item for item in evaluations if item.player_id == player_id]

    if not player_evaluations:
        raise HTTPException(status_code=404, detail="No evaluations found for this player")

    last_evaluation = player_evaluations[-1]
    strengths: list[str] = []
    weaknesses: list[str] = []
    training_recommendations: list[str] = []

    if last_evaluation.pass_accuracy >= 80:
        strengths.append("Good passing accuracy")
    else:
        weaknesses.append("Passing accuracy needs improvement")
        training_recommendations.append("Work on short passing under pressure")

    if last_evaluation.recoveries >= 5:
        strengths.append("Strong defensive recovery")
    else:
        weaknesses.append("Low defensive recovery")
        training_recommendations.append("Improve positioning and ball recovery drills")

    if last_evaluation.coach_rating >= 7:
        strengths.append("Positive overall coach evaluation")
    else:
        weaknesses.append("Overall performance needs improvement")
        training_recommendations.append("Review tactical decisions and match involvement")

    return Recommendation(
        player_id=player_id,
        strengths=strengths,
        weaknesses=weaknesses,
        training_recommendations=training_recommendations,
    )
