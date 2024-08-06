from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="my_cookies",
    packages=["my_cookies"],
    version="0.1.5",
    license="MIT",
    description="Retrieve cookies from your favorite browsers.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Wang Kai",
    author_email="kaiwkx@gmail.com",
    url="https://github.com/kaiwk/my_cookies",
    download_url="https://github.com/kaiwk/my_cookies",
    keywords=["browser", "cookies"],
    scripts=["bin/my_cookies"],
    install_requires=["click", "browser_cookie3"],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta", or "5 - Production/Stable"
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
