import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nba_tweepy",
    version="0.0.1",
    author="Scott LaForest",
    author_email="scott.w.laforest@gmail.com",
    description="A small package built to access NBA Twitter using tweepy.",
    long_description=long_description
    long_description_content_type="text/markdown",
    url="https://github.com/scottyla19/nba-tweepy",
    packages=setuptools.find_packages(),
    install_requires=[
          'tweepy',
          'pandas'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)