# 🏃 FitTrack – Fitness Data Analytics Dashboard

An end-to-end **Fitness Data Analytics project** built using Python, Pandas, SQL, Plotly and Streamlit to analyze daily physical activity, calories, sleep patterns, heart rate and user-level fitness behavior.

The project transforms raw fitness tracking data into meaningful analytical insights through data cleaning, transformation, exploratory data analysis and an interactive dashboard.

---

## 🚀 Live Dashboard

🔗 **Streamlit Dashboard:**  
https://fittrack-fitness-data-analytic-dash.streamlit.app/

---

## 📌 Project Overview

FitTrack Fitness Data Analytics is an analytics case study focused on understanding fitness and lifestyle patterns from activity-tracking data.

The project analyzes:

- 👟 Daily steps
- 🔥 Calories burned
- 📍 Distance covered
- 🏃 Activity intensity
- 🪑 Sedentary time
- 😴 Sleep duration
- ❤️ Heart rate
- 👤 Individual user activity

The goal is to convert raw fitness data into actionable insights using data analytics and visualization techniques.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Analyze daily fitness activity patterns.
2. Understand the relationship between steps, distance and calories.
3. Analyze different activity intensity levels.
4. Study sleep duration and time spent in bed.
5. Analyze average heart-rate patterns.
6. Compare activity behavior across users.
7. Identify important correlations between fitness metrics.
8. Build an interactive dashboard for business-style analysis.

---

## 📂 Dataset

The project uses fitness tracker data containing multiple datasets at different granularities.

### Dataset Categories

| Granularity | Data |
|---|---|
| Daily | Daily Activity |
| Daily | Daily Calories |
| Daily | Daily Intensities |
| Daily | Daily Steps |
| Hourly | Hourly Calories |
| Hourly | Hourly Intensities |
| Hourly | Hourly Steps |
| Minute | Minute Calories |
| Minute | Minute Intensities |
| Minute | Minute METs |
| Minute | Minute Sleep |
| Minute | Minute Steps |
| Second | Heart Rate |
| Daily | Sleep |
| Daily | Weight |

The raw datasets are maintained separately in the project to preserve their original structure and granularity.

---

## 🧹 Data Preparation

The data analytics workflow includes:

- Loading raw CSV datasets using Pandas
- Inspecting dataset structure
- Checking data types
- Detecting missing values
- Checking duplicate records
- Converting date/time columns
- Handling invalid values
- Converting numerical columns to appropriate data types
- Creating analytical summary datasets
- Preparing data for visualization and dashboard development

---

## 📊 Analysis Performed

### 1. Activity Analysis

Analyzed:

- Average daily steps
- Daily calories burned
- Distance covered
- Very active minutes
- Fairly active minutes
- Lightly active minutes
- Sedentary minutes
- Activity intensity

### 2. Sleep Analysis

Analyzed:

- Sleep duration
- Time spent in bed
- Sleep distribution
- Average sleep duration
- Relationship between sleep and activity

### 3. Heart Rate Analysis

Analyzed:

- Average heart rate
- Minimum heart rate
- Maximum heart rate
- Heart-rate distribution
- Heart-rate variability across records

### 4. User Analysis

Analyzed:

- User activity levels
- Average daily steps by user
- User-level fitness summaries
- Top users based on average daily steps

### 5. Correlation Analysis

Studied relationships between:

- Steps
- Distance
- Calories
- Activity minutes
- Intensity metrics

---

## 📈 Interactive Dashboard

The Streamlit dashboard contains five major sections:

### 📊 Overview

Provides a high-level summary of fitness activity including:

- Total users
- Activity days
- Average daily steps
- Average calories
- Average distance
- Average sedentary minutes
- Average sleep
- Average heart rate

Visualizations include:

- Activity level distribution
- Daily steps distribution
- Steps vs calories
- Fitness metric correlations

---

### 🏃 Activity

The Activity section provides:

- Average daily activity minutes
- Distance vs calories analysis
- Daily calorie distribution
- Fitness metric correlation heatmap

---

### 😴 Sleep

The Sleep section provides:

- Sleep duration distribution
- Average sleep vs time in bed
- Sleep data table

---

### ❤️ Heart Rate

The Heart Rate section provides:

- Average BPM
- Minimum BPM
- Maximum BPM
- Heart-rate distribution
- Heart-rate box plot

---

### 👤 Users

The Users section provides:

- Top users by average daily steps
- User-level activity analysis
- Detailed user activity table

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and application development |
| Pandas | Data cleaning and transformation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Exploratory visualization |
| Plotly | Interactive visualizations |
| Streamlit | Interactive dashboard |
| SQL | Data analysis and querying |
| Jupyter Notebook | Exploratory data analysis |
| Git & GitHub | Version control and project management |

---

## 📁 Project Structure

```text
FitTrack-Fitness-Data-Analytics/
│
├── data/
│   ├── raw/
│   │   ├── dailyActivity_merged.csv
│   │   ├── dailyCalories_merged.csv
│   │   ├── dailyIntensities_merged.csv
│   │   ├── dailySteps_merged.csv
│   │   ├── heartrate_seconds_merged.csv
│   │   ├── hourlyCalories_merged.csv
│   │   ├── hourlyIntensities_merged.csv
│   │   ├── hourlySteps_merged.csv
│   │   ├── minuteCaloriesNarrow_merged.csv
│   │   ├── minuteCaloriesWide_merged.csv
│   │   ├── minuteIntensitiesNarrow_merged.csv
│   │   ├── minuteIntensitiesWide_merged.csv
│   │   ├── minuteMETsNarrow_merged.csv
│   │   ├── minuteSleep_merged.csv
│   │   ├── minuteStepsNarrow_merged.csv
│   │   ├── minuteStepsWide_merged.csv
│   │   ├── sleepDay_merged.csv
│   │   └── weightLogInfo_merged.csv
│   │
│   └── processed/
│
├── notebooks/
│   └── fitness_analysis.ipynb
│
├── sql/
│   ├── 01_data_quality.sql
│   ├── 02_analysis_queries.sql
│   └── 03_business_insights.sql
│
├── dashboard/
│   └── powerbi/
│
├── streamlit/
│   ├── app.py
│   ├── fitness_dashboard_data.csv
│   ├── daily_sleep_summary.csv
│   ├── daily_heart_rate_summary.csv
│   └── user_activity_summary.csv
│
├── assets/
│   └── charts/
│
├── requirements.txt
├── README.md
└── .gitignore
