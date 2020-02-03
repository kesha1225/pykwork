from setuptools import setup, find_packages
import kwork

setup(
    name="kwork",
    version=kwork.__version__,
    url="https://github.com/kesha1225/pykwork",
    author="kesha1225",
    packages=find_packages(),
    description="simple wrapper for kwork.ru",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=["aiohttp", "pydantic", "websockets", "fake_useragent"],
    python_requires='>=3.7',
)