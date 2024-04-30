# _logger.py
import logging
from datetime import datetime
from zoneinfo import ZoneInfo

from src.core.utils import get_server_date


class TextFileLogHandler(logging.Handler):
    def __init__(self, file_name, buffer_size=10):
        super().__init__()
        self.file_name = file_name
        self.buffer_size = buffer_size
        self.buffer = []

    def emit(self, record):
        log_entry = self.format(record).encode("utf-8")
        self.buffer.append(log_entry)

        if len(self.buffer) >= self.buffer_size:
            self.flush_buffer()

    def flush_buffer(self):
        if self.buffer:
            all_logs = b"\n".join(self.buffer)
            with open(self.file_name, "ba") as f:
                f.write(all_logs)
            self.buffer.clear()


def get_logger_dev(log_dir: str, buffer_size: int = 10) -> logging.Logger:
    _formatter = logging.Formatter(
        '[%(asctime)s - %(levelname)s] - %(filename)s->%(funcName)s():Line %(lineno)d - "%(message)s"\n'
    )
    file_path = f"{log_dir}/{get_server_date()}.txt"

    _handler = TextFileLogHandler(file_name=file_path, buffer_size=buffer_size)
    _handler.setFormatter(_formatter)
    logging.Formatter.converter = (
        lambda *args: datetime.now().astimezone(ZoneInfo("UTC")).timetuple()
    )
    logger = logging.getLogger(__name__)
    logger.addHandler(_handler)
    logger.setLevel(logging.INFO)

    return logger


def get_logger_prod(log_dir: str, buffer_size: int = 10) -> logging.Logger:
    _formatter = logging.Formatter(
        '[%(asctime)s - %(levelname)s - %(processName)s: %(process)d - %(threadName)s: %(thread)d] - %(filename)s->%(funcName)s():Line %(lineno)d - "%(message)s"\n'
    )
    file_path = f"{log_dir}/{get_server_date()}.txt"
    _handler = TextFileLogHandler(file_name=file_path, buffer_size=buffer_size)

    logging.Formatter.converter = (
        lambda *args: datetime.now().astimezone(ZoneInfo("UTC")).timetuple()
    )
    logger = logging.getLogger(__name__)
    logger.addHandler(_handler)
    logger.setLevel(logging.INFO)
    return logger
