import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mongodb-helper",
    version="0.1",
    author="Flampt",
    description="Methods that simplify MongoDB collection reading and writing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlamptX/mongodb-helper",
    project_urls={
        "Python Bot": "https://python-bot.web.app",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='pythonbot, api',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)