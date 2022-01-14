import downloader
from setuptools import setup, find_packages

install_requires = [
    "setuptools",
    "selenium"
]


def long_description():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="downloader",
    version=downloader.__version__,
    description=downloader.__doc__.strip(),
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/farooq-teqniqly/tqdnld",
    author=downloader.__author__,
    author_email="farooq@teqniqly.com",
    license=downloader.__license__,
    packages=find_packages(include=["downloader", "downloader.*"]),
    entry_points={
        "console_scripts": [
            "downloader = downloader.__main__:main"
        ],
    },
    python_requires=">=3.8",
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Utilities"
    ],
    project_urls={
        "GitHub": "https://github.com/farooq-teqniqly/tqdnld"
    }
)
