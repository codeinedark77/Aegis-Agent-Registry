import pytest
from app.main import create_app
from app.config import get_settings

def test_app_creation():
    """Verify FastAPI application instantiates with correct metadata."""
    app = create_app()
    assert app.title == "AgentRegistry"
    assert app.docs_url == "/api/docs"
    assert app.openapi_url == "/api/openapi.json"

def test_settings_loaded():
    """Verify application settings load properly."""
    settings = get_settings()
    assert settings.SECRET_KEY is not None
    assert "sqlite" in settings.DATABASE_URL

def test_api_routes_registered():
    """Verify expected v1 endpoints are mounted."""
    app = create_app()
    route_paths = [getattr(r, 'path', '') for r in app.routes]
    openapi = app.openapi()
    assert "/api/v1/auth/login" in openapi["paths"] or "/api/v1/auth" in "".join(openapi["paths"].keys())
    assert any("/api/v1/agents" in p for p in openapi["paths"].keys())
