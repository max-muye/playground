from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# Cython扩展
cython_extensions = [
    Extension(
        "cython_example",
        sources=["cython_example.pyx"],
        include_dirs=[np.get_include()],
        language="c++",
        extra_compile_args=["-std=c++11"],
        extra_link_args=["-std=c++11"]
    )
]

# pybind11扩展 (需要安装pybind11)
# pybind11_extensions = [
#     Extension(
#         "cpp_math",
#         sources=["cpp_extension_example.cpp"],
#         include_dirs=[pybind11.get_include()],
#         language="c++",
#         extra_compile_args=["-std=c++11"],
#         extra_link_args=["-std=c++11"]
#     )
# ]

setup(
    name="python_cpp_examples",
    version="1.0",
    description="Python和C++混合编程示例",
    author="Your Name",
    author_email="your.email@example.com",
    ext_modules=cythonize(cython_extensions),
    install_requires=[
        "numpy",
        "cython"
    ],
    python_requires=">=3.6"
) 