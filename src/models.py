from datetime import date
from enum import Enum
from pydantic import BaseModel, Field


class PlayerPosition(str, Enum):
    GOALKEEPER = "goalkeeper"
    DEFENDER = "defender"
    MIDFIELDER = "midfielder"
    FORWARD = "forward"


class PreferredFoot(str, Enum):
    RIGHT = "right"
    LEFT = "left"
    BOTH = "both"


class Player(BaseModel):
    id: int | None = None
    full_name: str = Field(..., min_length=3)
    age: int = Field(..., ge=5, le=60)
    position: PlayerPosition
    preferred_foot: PreferredFoot | None = None
    team: str | None = None
    notes: str | None = None


class Match(BaseModel):
    id: int | None = None
    opponent: str = Field(..., min_length=2)
    match_date: date = Field(default_factory=date.today)
    team_goals: int = Field(default=0, ge=0)
    opponent_goals: int = Field(default=0, ge=0)
    notes: str | None = None


class PlayerEvaluation(BaseModel):
    id: int | None = None
    player_id: int
    match_id: int | None = None
    minutes_played: int = Field(default=0, ge=0, le=130)
    goals: int = Field(default=0, ge=0)
    assists: int = Field(default=0, ge=0)
    successful_passes: int = Field(default=0, ge=0)
    failed_passes: int = Field(default=0, ge=0)
    recoveries: int = Field(default=0, ge=0)
    duels_won: int = Field(default=0, ge=0)
    fouls_committed: int = Field(default=0, ge=0)
    yellow_cards: int = Field(default=0, ge=0)
    red_cards: int = Field(default=0, ge=0)
    coach_rating: float = Field(default=0, ge=0, le=10)
    technical_notes: str | None = None

    @property
    def total_passes(self) -> int:
        return self.successful_passes + self.failed_passes

    @property
    def pass_accuracy(self) -> float:
        if self.total_passes == 0:
            return 0
        return round((self.successful_passes / self.total_passes) * 100, 2)


class Recommendation(BaseModel):
    player_id: int
    strengths: list[str]
    weaknesses: list[str]
    training_recommendations: list[str]
