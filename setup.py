from setuptools import setup, find_packages
import kwork

setup(
    name="pykwork",
    version=kwork.__version__,
    url="https://github.com/kesha1225/pykwork",
    author="kesha1225",
    packages=find_packages(),
    description="simple wrapper for kwork.ru",
    install_requires=["aiohttp", "pydantic", "websockets", "fake_useragent"],
)