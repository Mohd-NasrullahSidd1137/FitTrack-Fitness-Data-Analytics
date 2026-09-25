# 🏃 FitTrack Fitness Data Analytics

An interactive fitness analytics project built using Python, Pandas, Plotly, and Streamlit to analyze fitness activity, calories, steps, sleep, heart rate, and user-level health metrics.

## 📊 Project Overview

FitTrack Fitness Data Analytics is an end-to-end data analytics project that transforms fitness tracking data into meaningful insights through data cleaning, preprocessing, exploratory data analysis, visualization, and an interactive Streamlit dashboard.

The project analyzes multiple fitness datasets covering daily, hourly, minute-level, sleep, heart-rate, and weight information.

## 🎯 Project Objectives

- Analyze users' daily fitness activity
- Understand calorie consumption patterns
- Analyze daily and hourly step activity
- Study activity intensity levels
- Analyze sleep duration and patterns
- Examine heart-rate trends
- Analyze user-level fitness behavior
- Identify meaningful trends and patterns
- Build an interactive fitness analytics dashboard

## 📁 Dataset

The project uses multiple fitness tracking CSV datasets, including:

- Daily Activity
- Daily Calories
- Daily Intensities
- Daily Steps
- Heart Rate
- Hourly Calories
- Hourly Intensities
- Hourly Steps
- Minute Calories
- Minute Intensities
- Minute METs
- Minute Sleep
- Minute Steps
- Sleep Day
- Weight Log Information

Different datasets contain different levels of granularity such as daily, hourly, minute-level, and second-level records.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- SQL
- Git & GitHub

## 🔍 Data Analytics Process

The project follows an end-to-end analytics workflow:

1. Data Collection
2. Data Understanding
3. Data Quality Assessment
4. Data Cleaning
5. Data Transformation
6. Exploratory Data Analysis
7. Data Visualization
8. Business Insights
9. Interactive Dashboard Development

## 🧹 Data Cleaning

The preprocessing workflow includes:

- Checking missing values
- Checking duplicate records
- Converting date/time columns
- Validating data types
- Checking user-level records
- Handling data quality issues
- Preparing datasets for analysis

## 📈 Dashboard Features

The FitTrack Analytics dashboard provides:

### Overview
- Total Users
- Activity Days
- Average Daily Steps
- Average Calories
- Average Sleep
- Average Heart Rate
- Average Sedentary Minutes
- Average Distance

### Activity Analysis
- Activity level distribution
- Daily steps distribution
- Fitness activity patterns
- User-level activity filtering

### Sleep Analysis
- Sleep duration
- Sleep patterns
- User-level sleep analysis

### Heart Rate Analysis
- Average heart rate
- Heart-rate trends
- User-level heart-rate analysis

### User Analysis
- User selection
- Individual fitness metrics
- Interactive filtering

## 📊 Key KPIs

The dashboard tracks important fitness KPIs such as:

- Total Users
- Average Steps
- Average Calories
- Average Distance
- Average Sleep
- Average Heart Rate
- Average Sedentary Minutes
- Activity Levels

## 🖥️ Streamlit Dashboard

The project includes an interactive Streamlit dashboard for exploring fitness data through filters, KPIs, charts, and analytical views.

## 📂 Project Structure

```text
FitTrack-Fitness-Data-Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── fitness_analysis.ipynb
│
├── streamlit/
│   └── app.py
│
├── assets/
│   └── charts/
│
├── sql/
│
├── requirements.txt
├── README.md
└── .gitignore
