import pytest

@pytest.fixture(scope="session")
def strategy():
    from src.utils import BlackjackStrategy
    return BlackjackStrategy()