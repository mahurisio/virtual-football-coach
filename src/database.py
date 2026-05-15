from src.models import Match, Player, PlayerEvaluation


players: list[Player] = []
matches: list[Match] = []
evaluations: list[PlayerEvaluation] = []


def get_next_id(collection: list) -> int:
    if not collection:
        return 1

    return max(item.id or 0 for item in collection) + 1
