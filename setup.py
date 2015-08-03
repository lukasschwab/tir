from setuptools import setup


setup (
    name = "tir",
    version="0.0.1",
    entry_points={
        'console_scripts': [
            'tir=tir:main'
        ],
    }
)
