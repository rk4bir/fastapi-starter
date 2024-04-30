from datetime import datetime
from src.config import SERVER_TIMEZONE

from src.core.utils import get_server_date


def test_get_server_date():
    dt = datetime.now().astimezone(SERVER_TIMEZONE)
    assert dt.strftime("%Y-%m-%d") == get_server_date()
