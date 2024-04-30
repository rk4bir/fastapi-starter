![coverage-badge](./docs/coverage.svg)


## FastAPI_Starter

> FastAPI starter project

Project structure
```md
.
├── LICENSE
├── MANIFEST.in
├── README.md
├── pyproject.toml
├── pytest.ini
├── requirements
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
├── requirements-dev.txt
├── requirements.txt
├── setup.cfg
├── setup.py
├── src
│   ├── __init__.py
│   ├── _logger.py
│   ├── config.py
│   ├── config_dev.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── utils.py
│   ├── database.py
│   └── main.py
└── tox.ini
```
Run the local development server

```bash
$ uvicorn src:app --host 0.0.0.0 --port 8000 --reload
```

```md
INFO:     Will watch for changes in these directories: ['/path/to/fastapi-starter']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [59575] using WatchFiles

==================================================
Project            : FastAPI_Starter
File Path Separator: /
Settings           : dev
Platform           : posix
Timezone           : UTC
Log level          : 20
Project Root       : ~/fastapi-starter
Src Root           : ~/fastapi-starter/src
Log Dir            : ~/fastapi-starter/logs/
Test secret        : secret-key
==================================================

INFO:     Started server process [59588]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
