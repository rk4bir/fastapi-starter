from datetime import datetime
from src.config import SERVER_TIMEZONE


def get_server_date(fmt: str = "%Y-%m-%d"):
    dt = datetime.now().astimezone(SERVER_TIMEZONE)
    return dt.strftime(f"{fmt}")


def get_iso_timestamp():
    dt = datetime.now().astimezone(SERVER_TIMEZONE)
    return dt.isoformat().replace("+00:00", "Z")
