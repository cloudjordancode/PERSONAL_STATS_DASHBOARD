"""
L8 — Personal Stats Dashboard  (STARTER)
==========================================
Run with:
    streamlit run starter.py

Your goal: build a wide-layout dashboard with sidebar controls,
metrics, tabs, and an expander.

Required features:
    1. st.set_page_config(layout="wide")
    2. Sidebar with at least 2 control widgets (selectbox, radio, etc.)
    3. 3-column metrics row using st.metric() — include delta values
    4. 2 tabs: "Overview" and "Details"
    5. 1 expander with extra content (raw data, methodology, etc.)
    6. Data can be hardcoded

Layout concepts:
    st.set_page_config(layout="wide")  — expands to full browser width
    st.sidebar.*                       — everything here goes in the sidebar
    col1, col2, col3 = st.columns(3)   — 3 equal columns; use `with col1:`
    st.metric(label, value, delta)     — big number + arrow; delta can be a string
    tab1, tab2 = st.tabs(["A", "B"])   — tabbed sections; use `with tab1:`
    with st.expander("Title"):         — collapsible section

When to use tabs vs expanders:
    Tabs      → mutually exclusive views (Overview vs Details)
    Expanders → optional detail that most users won't need
"""

import streamlit as st
import pandas as pd
import altair as alt
# ── Step 1: Page config ────────────────────────────────────────────────────
# TODO: Call st.set_page_config with layout="wide", a title, and an icon
# This must be the FIRST Streamlit call in the script.
st.set_page_config(
    page_title="Personal Stats Dashboard",
    page_icon="🗽",
    layout="wide"
)

# ── Step 2: Hardcoded data ────────────────────────────────────────────────
# TODO: Create some data to display.
# Suggestions:
#   WEEKLY_STUDY = {"Mon": 1.5, "Tue": 2.0, ...}
#   MODULES = {"Module 1": {"score": 88, "status": "Complete"}, ...}
#   SKILLS  = {"Python": 90, "SQL": 75, ...}

weekly_study = {"Mon": 1.5, "Tue": 2.0, "Wed": 3.5, "Thurs": 2.3, "Fri": 4.2}

# ── Step 3: Sidebar controls ──────────────────────────────────────────────
# TODO: Use `with st.sidebar:` to add:
#   - st.header("Dashboard Controls")
#   - A selectbox (e.g., choose a module to focus on)
#   - A radio button (e.g., choose chart type)
with st.sidebar:
    st.title("🕹️ Controls")

    selected_day = st.selectbox(
        "Select Study Day",
        list(weekly_study.keys())
    )

    chart_type = st.radio(
        "Chart Type",
        ["Bar Chart", "Line Chart"]
    )

# ── Step 4: Page title ────────────────────────────────────────────────────
# TODO: st.title() and st.caption()
st.title("👁️ My Dashboard")
st.write(f"Showing study data for **{selected_day}**")

# ── Step 5: Metrics row ───────────────────────────────────────────────────
# TODO: Create 3 columns: col1, col2, col3 = st.columns(3)
# In each column, display a st.metric() with a label, value, and delta.
# Example:
#   with col1:
#       st.metric("Study Hours", "10.5 hrs", "+1.5 hrs vs last week")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Selected Day Hours",
        f"{weekly_study[selected_day]} hrs",
        "+0.5 hrs"
    )

with col2:
    st.metric(
        "Weekly Study Hours",
        f"{sum(weekly_study.values()):.1f} hrs",
        "+2.0 hrs"
    )

with col3:
    st.metric(
        "Modules Completed",
        "5 / 9",
        "+1 module"
    )


# ── Step 6: Tabs ──────────────────────────────────────────────────────────
# TODO: Create 2 tabs: "Overview" and "Details"
# tab_overview, tab_details = st.tabs(["📈 Overview", "📋 Details"])
#
# In tab_overview:
#   - st.subheader and a chart (st.bar_chart / st.line_chart)
#
# In tab_details:
#   - Module progress table or list
#   - An st.expander with raw data or methodology notes
tab_overview, tab_details = st.tabs(
    ["📈 Overview", "📋 Details"]
)



with tab_overview:
    st.subheader("Weekly Study Progress")

    days = ["Mon", "Tue", "Wed", "Thurs", "Fri"]

    chart_data = pd.DataFrame({
        "Day": days,
        "Hours": [weekly_study[day] for day in days]
    })

    if chart_type == "Bar Chart":
        chart = alt.Chart(chart_data).mark_bar().encode(
            x=alt.X("Day:N", sort=days),
            y="Hours:Q"
        )
    else:
        chart = alt.Chart(chart_data).mark_line(point=True).encode(
            x=alt.X("Day:N", sort=days),
            y="Hours:Q"
        )

    st.altair_chart(chart, use_container_width=True)

with tab_details:
    st.subheader("Coding Temple Module Progress")

    modules = {
        "Module 1": "Complete",
        "Module 2": "Complete",
        "Module 3": "Complete",
        "Module 4": "Complete",
        "Module 5": "Complete",
        "Module 6": "In Progress",
        "Module 7": "Not Started",
        "Module 8": "Not Started",
        "Module 9": "Not Started"
    }

    st.table([
        {"Module": module, "Status": status}
        for module, status in modules.items()
    ])
# ── Step 7: Expander ──────────────────────────────────────────────────────
# TODO: Inside the Details tab (or below), add:
#   with st.expander("Raw Data & Methodology", expanded=False):
#       st.json(your_data)
#       st.markdown("Explanation of how values are calculated...")
with tab_details:
    with st.expander("📊 Study Data & Methodology"):
        st.write("Weekly study hours are currently sample data.")
        st.json(weekly_study)
        st.markdown(
            "Module completion is tracked across 9 Coding Temple modules. "
            "The graduation target is November 18, 2026."
        )   