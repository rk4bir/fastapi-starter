from setuptools import setup, find_packages

setup(
    name="FastAPI_Starter",
    version="1.0.0",
    packages=find_packages(where=["src"]),
    options={"bdist_wheel": {"universal": False}},
)
