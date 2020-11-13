from setuptools import setup


requirements = [
    'google-api-python-client',
    'pyzmq',
]

dev_requirements = [
    'black',
    'mypy',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="SpongeSplits",
    version="0.0.1",
    author="Velkog",
    author_email="thevelkog@gmail.com",
    description="A Video Autosplitting Tool for SpongeBob Squarepants: Battle for Bikini Bottom",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/velkog/SpongeSplits",
    install_requires=requirements,
    extras_require= { 'dev': dev_requirements },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
