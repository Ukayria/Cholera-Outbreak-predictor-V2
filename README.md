
# Cholera Outbreak Risk Predictor

An AI-powered early warning tool that predicts weekly cholera outbreak levels in Nigeria using epidemiological and environmental data.

> **This project is an improved version of my previous Cholera Outbreak Predictor.** The new version improves the modelling approach, feature engineering, validation, and adds a web interface for making predictions.

**Previous version:** [View previous repository](https://github.com/Ukayria/cholera-outbreak-predictor)

**Live application:** [Try the web app](https://cholera-outbreak-predictor-v2.onrender.com/)

## Project Overview

The system predicts cholera outbreak levels using weekly data:

* **Level 0:** No outbreak
* **Level 1:** 1–5 suspected cases
* **Level 2:** 6 or more suspected cases

The dataset covers **2020–2026**, with data available up to epidemiological week 27 of 2026. After preprocessing, **236 weekly observations** were used for modelling.

## Data Sources

* **Nigeria Centre for Disease Control and Prevention (NCDC):** Weekly epidemiological reports used for cholera surveillance data.
* **NASA:** Weekly rainfall and temperature data used as environmental predictors.

## Model

Logistic Regression, Random Forest, and XGBoost were evaluated.

**XGBoost was selected as the final model** because it was better at identifying actual outbreak weeks. Time-series cross-validation gave XGBoost an average recall of **68% for the outbreak class**, compared with **49% for Random Forest**.

The model uses:

* Suspected cholera cases
* Number of states affected
* Weekly rainfall
* Weekly temperature
* Lagged rainfall and temperature
* Epidemiological week

## Tech Stack

* Python
* XGBoost
* Scikit-learn
* Pandas
* NumPy
* Flask
* HTML/CSS
* GitHub
* Render

## Limitations

The dataset is relatively small, with 236 usable observations, and the current environmental data is national rather than state-level.

Future improvements will focus on expanding the dataset and adding more detailed state or local environmental data.

## Disclaimer

This tool is intended for research and decision-support purposes. It is not a replacement for official cholera surveillance, laboratory confirmation, or public health decision-making.
