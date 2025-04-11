# 🌦️ Weather Forecasting using Machine Learning

## 📌 Project Overview

This project aims to develop a Machine Learning (ML) model for predicting key weather metrics such as temperature, humidity, wind speed, and precipitation. It includes automated data updates and visualizes forecasts on a Supaboard dashboard, enabling users to access accurate, real-time weather insights.

---

## 🧠 Problem Statement

Weather forecasting plays a crucial role in sectors like agriculture, transportation, energy, and event planning. Due to the complexity of changing variables (temperature, humidity, wind, etc.), building an accurate forecast model can provide critical value in decision-making and planning.

---

## 📊 Project Components

### 1. ML Model for Weather Forecasting
- Supervised learning model trained on historical weather data.
- Predicts metrics like temperature, humidity, and weather conditions.
- Evaluation using MAE, RMSE, and R².

### 2. Data Scheduler
- Automates regular data ingestion from external APIs or internal sources.
- Cleans and processes incoming data.
- Updates model inputs and retrains if necessary.
- Tools: Cron, Airflow, or Python scheduler.

### 3. Supaboard Dashboard
- Displays historical trends, real-time predictions, and model insights.
- Key metrics shown via KPI cards for intuitive understanding.
- Users can explore data through graphs, filters, and tables.

---

## 📁 Dataset Overview

| Column Name        | Description                                        |
|--------------------|----------------------------------------------------|
| `date_time`        | Date and time of the weather record                |
| `temperature`      | Air temperature (°C or °F)                         |
| `humidity`         | Relative humidity (%)                              |
| `wind_speed`       | Wind speed (km/h or m/s)                           |
| `wind_direction`   | Wind direction in degrees (0–360)                  |
| `pressure`         | Atmospheric pressure (hPa)                         |
| `precipitation`    | Rain or snowfall amount (mm)                       |
| `cloud_coverage`   | Cloud coverage percentage (%)                      |
| `weather_condition`| Categorical condition (e.g., Clear, Rainy, Cloudy) |
| `forecasted_weather`| Target variable (numeric/categorical forecast)    |

---

## 📈 KPIs Tracked on Dashboard

- Forecasted Temperature (Today / 7 Days)
- Forecasted Humidity and Wind Speed
- Rain Probability
- Weather Condition
- Model Accuracy, MAE, RMSE
- Historical Weather Averages
- Forecast Update Time

---

## 🛠️ Tech Stack

- **Python** (Pandas, Scikit-learn, XGBoost, etc.)
- **APIs** (for live weather data ingestion)
- **Scheduler**: Cron / Airflow / Python scripts
- **Visualization**: Supaboard / Power BI (optional)
- **Data Storage**: CSV / Database / Supabase

---

## ✅ Future Enhancements

- Integrate severe weather alert system.
- Add mobile-friendly dashboard UI.
- Use deep learning (LSTM) for better time series forecasting.

---
## 🏃‍♂️ How to Run

### 🔧 1. Set Up Environment

- Install required Python libraries:
  ```bash
  pip install -r requirements.txt
--- 

## 👥 Contributors

- **[Ajam Ali]** – Project Lead, Data Preprocessing, Model Development, Dashboard Design  
- **Neha raju** – Feature Engineering, Model Tuning, Documentation, Dashboard Support

We collaborated on every stage of this project — from data collection and cleaning to modeling, automation, and visualization.
