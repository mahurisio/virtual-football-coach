from fastapi import FastAPI

from src.routes import demo_router, evaluations_router, games_router, players_router


def create_app() -> FastAPI:
    app = FastAPI(title="Virtual Football Coach", version="0.1.0")

    app.include_router(players_router)
    app.include_router(games_router)
    app.include_router(evaluations_router)
    app.include_router(demo_router)

    @app.get("/")
    def root() -> dict[str, str]:
        return {"message": "Virtual Football Coach API", "status": "running"}

    @app.get("/health")
    def health_check() -> dict[str, str]:
        return {"status": "ok"}

    return app
