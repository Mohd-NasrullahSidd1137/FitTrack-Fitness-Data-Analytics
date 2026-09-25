import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="FitTrack Analytics",
    page_icon="🏃",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.block-container {
    padding-top: 1.5rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

.dashboard-title {
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 0px;
}

.dashboard-subtitle {
    font-size: 16px;
    color: #6b7280;
    margin-top: 5px;
    margin-bottom: 25px;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 3px 12px rgba(0,0,0,0.05);
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-top: 25px;
    margin-bottom: 15px;
}

.small-text {
    color: #6b7280;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    base_dir = Path(__file__).resolve().parent

    master = pd.read_csv(
        base_dir / "fitness_dashboard_data.csv"
    )

    sleep = pd.read_csv(
        base_dir / "daily_sleep_summary.csv"
    )

    heart = pd.read_csv(
        base_dir / "daily_heart_rate_summary.csv"
    )

    users = pd.read_csv(
        base_dir / "user_activity_summary.csv"
    )

    # -----------------------------------------------------
    # DATE CONVERSION
    # -----------------------------------------------------

    if "ActivityDate" in master.columns:
        master["ActivityDate"] = pd.to_datetime(
            master["ActivityDate"],
            errors="coerce"
        )

    if "SleepDay" in sleep.columns:
        sleep["SleepDay"] = pd.to_datetime(
            sleep["SleepDay"],
            errors="coerce"
        )

    if "ActivityDate" in heart.columns:
        heart["ActivityDate"] = pd.to_datetime(
            heart["ActivityDate"],
            errors="coerce"
        )

    return master, sleep, heart, users


# =========================================================
# DATA LOAD ERROR HANDLING
# =========================================================

try:

    master_daily, sleep_data, heart_data, user_data = load_data()

except Exception as e:

    st.error(
        "❌ Dataset loading failed. "
        "Please make sure all CSV files are inside "
        "the same folder as app.py."
    )

    st.code(str(e))

    st.stop()


# =========================================================
# BASIC DATA VALIDATION
# =========================================================

required_master_columns = [
    "Id",
    "ActivityDate"
]

missing_master_columns = [
    col for col in required_master_columns
    if col not in master_daily.columns
]

if missing_master_columns:

    st.error(
        "❌ Missing columns in fitness_dashboard_data.csv:"
    )

    st.write(missing_master_columns)

    st.stop()


# Remove invalid dates

master_daily = master_daily.dropna(
    subset=["ActivityDate"]
).copy()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    "## 🏃 FitTrack Analytics"
)

st.sidebar.markdown(
    "### Dashboard Filters"
)

st.sidebar.markdown("---")


# =========================================================
# USER FILTER
# =========================================================

user_list = sorted(
    master_daily["Id"]
    .dropna()
    .unique()
)

selected_users = st.sidebar.multiselect(
    "👤 Select Users",
    user_list,
    default=user_list
)


# =========================================================
# ACTIVITY LEVEL FILTER
# =========================================================

if "ActivityLevel" in master_daily.columns:

    activity_levels = sorted(
        master_daily["ActivityLevel"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_activity = st.sidebar.multiselect(
        "⚡ Activity Level",
        activity_levels,
        default=activity_levels
    )

else:

    selected_activity = []


# =========================================================
# DATE FILTER
# =========================================================

min_date = master_daily["ActivityDate"].min()
max_date = master_daily["ActivityDate"].max()

min_date_value = min_date.date()
max_date_value = max_date.date()

date_range = st.sidebar.date_input(
    "📅 Date Range",
    value=(min_date_value, max_date_value),
    min_value=min_date_value,
    max_value=max_date_value
)


st.sidebar.markdown("---")

st.sidebar.info(
    "📊 Fitness Data Analytics\n\n"
    "Interactive dashboard built using "
    "Python, Pandas, Plotly and Streamlit."
)


# =========================================================
# FILTER MASTER DATA
# =========================================================

filtered_master = master_daily.copy()


filtered_master = filtered_master[
    filtered_master["Id"].isin(selected_users)
]


if "ActivityLevel" in filtered_master.columns:

    filtered_master = filtered_master[
        filtered_master["ActivityLevel"]
        .isin(selected_activity)
    ]


if len(date_range) == 2:

    start_date = pd.to_datetime(
        date_range[0]
    )

    end_date = pd.to_datetime(
        date_range[1]
    )

    filtered_master = filtered_master[
        (filtered_master["ActivityDate"] >= start_date)
        &
        (filtered_master["ActivityDate"] <= end_date)
    ]


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="dashboard-title">'
    '🏃 FitTrack Analytics Dashboard'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="dashboard-subtitle">'
    'Fitness activity, calories, sleep and heart-rate analytics'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# KPI CALCULATIONS
# =========================================================

total_users = filtered_master["Id"].nunique()

activity_days = filtered_master["ActivityDate"].nunique()


# Safe numeric conversion

numeric_columns = [
    "TotalSteps_x",
    "TotalDailyCalories",
    "TotalDistance",
    "SedentaryMinutes",
    "VeryActiveMinutes",
    "FairlyActiveMinutes",
    "LightlyActiveMinutes",
    "TotalIntensity",
    "AverageIntensity"
]

for col in numeric_columns:

    if col in filtered_master.columns:

        filtered_master[col] = pd.to_numeric(
            filtered_master[col],
            errors="coerce"
        )


avg_steps = (
    filtered_master["TotalSteps_x"].mean()
    if "TotalSteps_x" in filtered_master.columns
    else 0
)

avg_calories = (
    filtered_master["TotalDailyCalories"].mean()
    if "TotalDailyCalories" in filtered_master.columns
    else 0
)

avg_distance = (
    filtered_master["TotalDistance"].mean()
    if "TotalDistance" in filtered_master.columns
    else 0
)

avg_sedentary = (
    filtered_master["SedentaryMinutes"].mean()
    if "SedentaryMinutes" in filtered_master.columns
    else 0
)


# =========================================================
# KPI CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "👤 Total Users",
        f"{total_users:,}"
    )


with col2:

    st.metric(
        "📅 Activity Days",
        f"{activity_days:,}"
    )


with col3:

    st.metric(
        "👟 Avg Daily Steps",
        f"{avg_steps:,.0f}"
    )


with col4:

    st.metric(
        "🔥 Avg Calories",
        f"{avg_calories:,.0f}"
    )


col5, col6, col7, col8 = st.columns(4)


with col5:

    st.metric(
        "📍 Avg Distance",
        f"{avg_distance:.2f}"
    )


with col6:

    st.metric(
        "🪑 Avg Sedentary Min",
        f"{avg_sedentary:.0f}"
    )


with col7:

    avg_sleep = (
        sleep_data["SleepHours"].mean()
        if "SleepHours" in sleep_data.columns
        else 0
    )

    st.metric(
        "😴 Avg Sleep",
        f"{avg_sleep:.2f} hrs"
    )


with col8:

    avg_heart = (
        heart_data["AverageHeartRate"].mean()
        if "AverageHeartRate" in heart_data.columns
        else 0
    )

    st.metric(
        "❤️ Avg Heart Rate",
        f"{avg_heart:.0f} BPM"
    )


# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "📊 Overview",
        "🏃 Activity",
        "😴 Sleep",
        "❤️ Heart Rate",
        "👤 Users"
    ]
)


# =========================================================
# TAB 1 - OVERVIEW
# =========================================================

with tab1:

    st.markdown(
        '<div class="section-title">'
        '📊 Fitness Overview'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)


    # -----------------------------------------------------
    # Activity Level
    # -----------------------------------------------------

    with col1:

        if "ActivityLevel" in filtered_master.columns:

            activity_count = (
                filtered_master["ActivityLevel"]
                .value_counts()
                .reset_index()
            )

            activity_count.columns = [
                "ActivityLevel",
                "Days"
            ]

            fig = px.pie(
                activity_count,
                names="ActivityLevel",
                values="Days",
                hole=0.55,
                title="Activity Level Distribution"
            )

            fig.update_layout(
                template="plotly_white",
                legend_title="Activity Level"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:

            st.info(
                "ActivityLevel column not available."
            )


    # -----------------------------------------------------
    # Steps Distribution
    # -----------------------------------------------------

    with col2:

        if "TotalSteps_x" in filtered_master.columns:

            fig = px.histogram(
                filtered_master,
                x="TotalSteps_x",
                nbins=30,
                title="Daily Steps Distribution"
            )

            fig.update_layout(
                template="plotly_white",
                xaxis_title="Steps",
                yaxis_title="Days"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # -----------------------------------------------------
    # Steps vs Calories
    # -----------------------------------------------------

    if {
        "TotalSteps_x",
        "TotalDailyCalories"
    }.issubset(filtered_master.columns):

        color_column = (
            "ActivityLevel"
            if "ActivityLevel" in filtered_master.columns
            else None
        )

        fig = px.scatter(
            filtered_master,
            x="TotalSteps_x",
            y="TotalDailyCalories",
            color=color_column,
            hover_data=[
                "Id",
                "ActivityDate"
            ],
            title="Steps vs Calories Burned"
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# TAB 2 - ACTIVITY
# =========================================================

with tab2:

    st.markdown(
        '<div class="section-title">'
        '🏃 Activity Analysis'
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # Activity Minutes
    # -----------------------------------------------------

    activity_data = {}

    activity_mapping = {
        "Very Active": "VeryActiveMinutes",
        "Fairly Active": "FairlyActiveMinutes",
        "Lightly Active": "LightlyActiveMinutes",
        "Sedentary": "SedentaryMinutes"
    }

    for label, column in activity_mapping.items():

        if column in filtered_master.columns:

            activity_data[label] = (
                filtered_master[column].mean()
            )

    if activity_data:

        activity_minutes = pd.DataFrame(
            {
                "Activity Type": list(
                    activity_data.keys()
                ),
                "Average Minutes": list(
                    activity_data.values()
                )
            }
        )

        fig = px.bar(
            activity_minutes,
            x="Activity Type",
            y="Average Minutes",
            title="Average Daily Activity Minutes",
            text_auto=".0f"
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    col1, col2 = st.columns(2)


    # -----------------------------------------------------
    # Distance vs Calories
    # -----------------------------------------------------

    with col1:

        if {
            "TotalDistance",
            "TotalDailyCalories"
        }.issubset(filtered_master.columns):

            color_column = (
                "ActivityLevel"
                if "ActivityLevel" in filtered_master.columns
                else None
            )

            fig = px.scatter(
                filtered_master,
                x="TotalDistance",
                y="TotalDailyCalories",
                color=color_column,
                title="Distance vs Calories"
            )

            fig.update_layout(
                template="plotly_white"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # -----------------------------------------------------
    # Calories Distribution
    # -----------------------------------------------------

    with col2:

        if "TotalDailyCalories" in filtered_master.columns:

            fig = px.histogram(
                filtered_master,
                x="TotalDailyCalories",
                nbins=30,
                title="Daily Calories Distribution"
            )

            fig.update_layout(
                template="plotly_white"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # -----------------------------------------------------
    # Correlation
    # -----------------------------------------------------

    correlation_columns = [
        "TotalSteps_x",
        "TotalDistance",
        "TotalDailyCalories",
        "VeryActiveMinutes",
        "FairlyActiveMinutes",
        "LightlyActiveMinutes",
        "SedentaryMinutes",
        "TotalIntensity",
        "AverageIntensity"
    ]

    available_corr_columns = [
        col
        for col in correlation_columns
        if col in filtered_master.columns
    ]

    if len(available_corr_columns) >= 2:

        corr = filtered_master[
            available_corr_columns
        ].corr()

        fig = px.imshow(
            corr,
            text_auto=".2f",
            aspect="auto",
            title="Fitness Metrics Correlation"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =========================================================
# TAB 3 - SLEEP
# =========================================================

with tab3:

    st.markdown(
        '<div class="section-title">'
        '😴 Sleep Analysis'
        '</div>',
        unsafe_allow_html=True
    )


    if {
        "SleepHours",
        "TimeInBedHours"
    }.issubset(sleep_data.columns):

        sleep_col1, sleep_col2 = st.columns(2)


        # -------------------------------------------------
        # Sleep Distribution
        # -------------------------------------------------

        with sleep_col1:

            fig = px.histogram(
                sleep_data,
                x="SleepHours",
                nbins=20,
                title="Sleep Duration Distribution"
            )

            fig.update_layout(
                template="plotly_white",
                xaxis_title="Sleep Hours",
                yaxis_title="Records"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


        # -------------------------------------------------
        # Sleep Statistics
        # -------------------------------------------------

        with sleep_col2:

            sleep_stats = pd.DataFrame(
                {
                    "Metric": [
                        "Average Sleep",
                        "Average Time in Bed"
                    ],
                    "Hours": [
                        sleep_data["SleepHours"].mean(),
                        sleep_data["TimeInBedHours"].mean()
                    ]
                }
            )

            fig = px.bar(
                sleep_stats,
                x="Metric",
                y="Hours",
                title="Average Sleep vs Time in Bed",
                text_auto=".2f"
            )

            fig.update_layout(
                template="plotly_white"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )


    st.markdown(
        "### 🛌 Sleep Data"
    )

    st.dataframe(
        sleep_data.head(20),
        use_container_width=True
    )


# =========================================================
# TAB 4 - HEART RATE
# =========================================================

with tab4:

    st.markdown(
        '<div class="section-title">'
        '❤️ Heart Rate Analysis'
        '</div>',
        unsafe_allow_html=True
    )


    if "AverageHeartRate" in heart_data.columns:

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Average BPM",
                f"{heart_data['AverageHeartRate'].mean():.0f}"
            )


        with col2:

            if "MinimumHeartRate" in heart_data.columns:

                st.metric(
                    "Minimum BPM",
                    f"{heart_data['MinimumHeartRate'].min():.0f}"
                )


        with col3:

            if "MaximumHeartRate" in heart_data.columns:

                st.metric(
                    "Maximum BPM",
                    f"{heart_data['MaximumHeartRate'].max():.0f}"
                )


        # -------------------------------------------------
        # Heart Rate Distribution
        # -------------------------------------------------

        fig = px.histogram(
            heart_data,
            x="AverageHeartRate",
            nbins=30,
            title="Average Heart Rate Distribution"
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


        # -------------------------------------------------
        # Heart Rate Box Plot
        # -------------------------------------------------

        fig = px.box(
            heart_data,
            y="AverageHeartRate",
            title="Average Heart Rate — Box Plot"
        )

        fig.update_layout(
            template="plotly_white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.warning(
            "AverageHeartRate column is not available."
        )


# =========================================================
# TAB 5 - USERS
# =========================================================

with tab5:

    st.markdown(
        '<div class="section-title">'
        '👤 User Analysis'
        '</div>',
        unsafe_allow_html=True
    )


    if {
        "Id",
        "AverageSteps"
    }.issubset(user_data.columns):

        top_users = (
            user_data
            .sort_values(
                "AverageSteps",
                ascending=False
            )
            .head(10)
        )


        # -------------------------------------------------
        # Top Users Chart
        # -------------------------------------------------

        fig = px.bar(
            top_users,
            x="Id",
            y="AverageSteps",
            title="Top 10 Users by Average Daily Steps",
            text_auto=".0f"
        )

        fig.update_layout(
            template="plotly_white",
            xaxis_title="User ID",
            yaxis_title="Average Steps"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    st.markdown(
        "### 📋 User Activity Table"
    )

    st.dataframe(
        user_data,
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#6b7280;">
        <b>FitTrack Analytics Dashboard</b><br>
        Fitness Data Analytics Project |
        Python • Pandas • Plotly • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
