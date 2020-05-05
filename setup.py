from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read()

setup(
    name="draftsimulator",
    version="1.0",
    description="Simulation of a sports draft",
    author="Jacob Dodd",
    author_email="jacobdodd94@gmail.com",
    python_requires="~=3.7",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: General Audience",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=False,
    install_requires=requirements,
)