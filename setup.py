from setuptools import setup


setup (
    name = "tir",
    version="0.0.1",
    packages=["tir"],
    entry_points={
        'console_scripts': [
            'tir=tir.__main__:main'
        ],
    }
)
