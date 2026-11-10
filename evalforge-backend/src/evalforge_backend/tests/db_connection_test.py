import pytest

from evalforge_backend.services.db_service import get_db_connection

def test_get_db_api_key_missing(monkeypatch):
    
    monkeypatch.delenv("DB_URL", raising=False)
    
    with pytest.raises(ValueError, match="DB_URL"):
        get_db_connection()
        
def test_get_db_api_key_empty_string(monkeypatch):
    
    monkeypatch.setenv("DB_URL", "")
    
    with pytest.raises(ValueError):
        get_db_connection()
        
def test_get_db_connection_lifecycle():
    
    with get_db_connection() as conn:
        assert not conn.closed
    assert conn.closed
    
    