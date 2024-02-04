<img heigth="8" src="https://i.imgur.com/PjhxQ1Q.png" alt="llmir">

<h1 align="center">llmir</h1>

<p align="center"><i>A Compilation of Notes of Large Language Models for Information Retrieval</i></p>

<p align="center">
  <b>Joseph F. Vergel-Becerra</b> | <a href="https://joefaver.dev/">joefaver.dev</a>
  <br><br>
  <a href="#about">About</a> •
  <a href="#features">Features</a>
  <br><br>
  <a href="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000">
    <img src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" alt="Version" height="18">
  </a>
</p>
<br>

---

## About

`llm-information-retrieval` is a Python library for training, testing and reporting of the FTL-Pricing predictive models. This `Python` library is designed to training and generate the machine and deep learning models that predicts base transportation cost of FTL modality in United States & Canada. 


---

## Features

`llm-information-retrieval` is built on `Python 3.11` with [pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/) and [scikit-learn](https://scikit-learn.org/stable/), [matplotlib](https://matplotlib.org/), [seaborn](https://seaborn.pydata.org/), [plotly](https://plotly.com/python/)  among others, to preprocess the data, build the machine learning models, and visualize the results. 

For development, the library use:

- Formatting with [black](https://github.com/psf/black)
- Import sorting with [isort](https://github.com/timothycrosley/isort)
- Linting with [flake8](http://flake8.pycqa.org/en/latest/)
- Git hooks that run all the above with [pre-commit](https://pre-commit.com/)
- Testing with [pytest](https://docs.pytest.org/en/latest/)


---

## Life Cycle

As a proposal for the data science life cycle, [OSEMN](https://towardsdatascience.com/5-steps-of-a-data-science-project-lifecycle-26c50372b492) is mainly proposed. Standing for Obtain, Scrub, Explore, Model, and iNterpret, OSEMN is a five-phase life cycle.

<img heigth="8" src="https://i.imgur.com/tDP8VUd.png" alt="guane"><br>

Other good option is [Microsoft TDSP: The Team Data Science Process](https://learn.microsoft.com/en-us/azure/architecture/data-science-process/overview) combines many modern agile practices with the life cycle. It has five steps: Business Understanding, Data Acquisition and Understanding, Modeling, Deployment, and Customer Acceptance.

The important thing is that if you think they should be combined and form their own life cycle, feel free to do so.


---

## Contribute

First, make sure that before enabling pipenv, you must have `Python 3.11` installed. If it does not correspond to the version you have installed, you can create a conda environment with:

```sh
# Create and activate python 3.9 virutal environment
$ conda create -n py311 python=3.11
$ conda activate py311
```

Now, you can managament the project dependencies with `Pipenv`. To create de virtual environment and install all dependencies follow:

```sh
# Install pipx if pipenv and cookiecutter are not installed
$ python3 -m pip install pipx
$ python3 -m pipx ensurepath

# Install pipenv using pipx
$ pipx install pipenv

# Create pipenv virtual environment
$ pipenv shell

# Install dependencies
$ pipenv install --dev
```

Once the dependencies are installed, we need to notify `Jupyter` of this new `Python` environment by creating a kernel:

```sh
$ ipython kernel install --user --name KERNEL_NAME
```
