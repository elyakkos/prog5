from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='lr3',
    version='0.0',
    description='Openweather API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elyakkos/lr3-prog5",
    packages=['open-weather_LW'], 
    author='Kostyleva Eleonora',
    author_email='elkostylevaa@gmail.com',
    zip_safe=False
)
