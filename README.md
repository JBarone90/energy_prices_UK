# Policy Intervention: Energy Price Increase Analysis

## Overview

This project is part of the Data Science Graduate Programme 2022/23 and focuses on conducting an independent analysis of the impact of increasing energy prices on various economic sectors in Great Britain. The primary objective is to provide recommendations that can inform policy decisions.

## Project Description

The project involves the following key steps:

- Data collection and preprocessing: Gather relevant data on energy prices and economic indicators.
- Exploratory data analysis (EDA): Explore and analyze the data to identify trends and patterns.
- Sector-specific analysis: Assess the impact of energy price increases on different economic sectors.
- Policy recommendations: Derive data-driven recommendations to inform policy decisions.

## Data Sources (Work in progess)

- Consumer Prices Index including owner occupiers' housing costs (CPIH)

    <https://www.ons.gov.uk/datasets/cpih01/editions/time-series/versions/37>

- Passenger Rail usage by ticket type

    <https://dataportal.orr.gov.uk/statistics/usage/passenger-rail-usage/table-1222-passenger-journeys-by-ticket-type/>




## Project Structure
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- Make this project pip installable with `pip install -e`
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
