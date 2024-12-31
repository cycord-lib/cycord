from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name="cycord",
        sources=["__init__.pyx"],
    ),
]

setup(
    ext_modules=cythonize(extensions, language_level="3"),
    zip_safe=False,
)