# global configs: src/config.py
import os
from dotenv import load_dotenv
from zoneinfo import ZoneInfo

name = "FastAPI_Starter"

platform = os.name.lower()
fp_separator = "\\" if platform == "nt" else "/"
SERVER_TIMEZONE = ZoneInfo("UTC")

try:
    from .config_dev import MODE
except Exception as err:
    MODE = "prod"


if MODE == "prod":
    # load prod configs
    from src._logger import get_logger_prod

    HOME_DIR = "/path/to"
    PROJECT_ROOT = f"{fp_separator}".join(
        os.path.abspath(__file__).split(fp_separator)[:-2]
    )
    LOG_DIR = os.path.join(PROJECT_ROOT, "logs/")
    ENV_FILE = os.path.join(HOME_DIR, ".env")
    logger = get_logger_prod(log_dir=LOG_DIR, buffer_size=1)
    ALLOWED_ORIGINS = ["*"]

else:
    # load dev configs
    from src._logger import get_logger_dev

    PROJECT_ROOT = f"{fp_separator}".join(
        os.path.abspath(__file__).split(fp_separator)[:-2]
    )
    LOG_DIR = os.path.join(PROJECT_ROOT, "logs/")
    ENV_FILE = os.path.join(PROJECT_ROOT, ".env")
    logger = get_logger_dev(log_dir=LOG_DIR, buffer_size=1)
    ALLOWED_ORIGINS = ["*"]


def get_logger():
    yield logger


load_dotenv(ENV_FILE)
SRC_ROOT = os.path.join(PROJECT_ROOT, "src")
__dir_separator = f"{fp_separator}{PROJECT_ROOT.split(fp_separator)[-1]}"

SECRET = os.getenv("SECRET")

# Print out project configs
print("\n" + "=" * 50)
print(f"Project            : {name}")
print(f"File Path Separator: {fp_separator}")
print(f"Settings           : {MODE}")
print(f"Platform           : {platform}")
print(f"Timezone           : {SERVER_TIMEZONE}")
print(f"Log level          : {logger.level}")
print(
    f"Project Root       : ~{__dir_separator}{PROJECT_ROOT.split(__dir_separator)[-1]}"
)
print(f"Src Root           : ~{__dir_separator}{SRC_ROOT.split(__dir_separator)[-1]}")
print(f"Log Dir            : ~{__dir_separator}{LOG_DIR.split(__dir_separator)[-1]}")
print(f"Test secret        : {SECRET}")
print("=" * 50 + "\n")
