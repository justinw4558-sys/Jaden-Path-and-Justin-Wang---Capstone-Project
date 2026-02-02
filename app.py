import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="Portfolio Analytics", layout="wide")

# Session state for data persistence
if "properties_df" not in st.session_state:
    st.session_state.properties_df = None

def calculate_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate core KPIs: NOI, Occupancy, Revenue/Unit, Expense Ratio."""
    kpis = df.copy()

    # NOI = Revenue - Operating Expenses
    if "revenue" in kpis.columns and "operating_expenses" in kpis.columns:
        kpis["noi"] = kpis["revenue"] - kpis["operating_expenses"]

    # Occupancy Rate = Occupied Units / Total Units
    if "occupied_units" in kpis.columns and "total_units" in kpis.columns:
        kpis["occupancy_rate"] = (kpis["occupied_units"] / kpis["total_units"] * 100).round(1)

    # Revenue per Unit = Revenue / Total Units
    if "revenue" in kpis.columns and "total_units" in kpis.columns:
        kpis["revenue_per_unit"] = (kpis["revenue"] / kpis["total_units"]).round(2)

    # Expense Ratio = Operating Expenses / Revenue
    if "operating_expenses" in kpis.columns and "revenue" in kpis.columns:
        kpis["expense_ratio"] = (kpis["operating_expenses"] / kpis["revenue"] * 100).round(1)

    return kpis


def main():
    st.title("Portfolio Analytics Platform")

    # Sidebar: File Upload
    with st.sidebar:
        st.header("Data Upload")
        uploaded_file = st.file_uploader(
            "Upload property data (Excel/CSV)",
            type=["xlsx", "xls", "csv"]
        )

        if uploaded_file:
            try:
                if uploaded_file.name.endswith(".csv"):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)

                st.session_state.properties_df = calculate_kpis(df)
                st.success(f"Loaded {len(df)} properties")
            except Exception as e:
                st.error(f"Error loading file: {e}")

    # Main content
    if st.session_state.properties_df is None:
        st.info("Upload a property spreadsheet to get started.")
        st.markdown("""
        ### Expected columns:
        - `property_name` - Property identifier
        - `property_type` - e.g., Multifamily, Office, Retail
        - `submarket` - Geographic area
        - `total_units` - Number of units
        - `occupied_units` - Currently occupied units
        - `revenue` - Total revenue
        - `operating_expenses` - Total operating expenses
        - `date` - Period date (optional, for trends)
        """)
        return

    df = st.session_state.properties_df

    # Filters
    st.sidebar.header("Filters")

    # Property type filter
    if "property_type" in df.columns:
        property_types = ["All"] + list(df["property_type"].dropna().unique())
        selected_type = st.sidebar.selectbox("Property Type", property_types)
        if selected_type != "All":
            df = df[df["property_type"] == selected_type]

    # Submarket filter
    if "submarket" in df.columns:
        submarkets = ["All"] + list(df["submarket"].dropna().unique())
        selected_submarket = st.sidebar.selectbox("Submarket", submarkets)
        if selected_submarket != "All":
            df = df[df["submarket"] == selected_submarket]

    # Portfolio Summary
    st.header("Portfolio Summary")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if "noi" in df.columns:
            total_noi = df["noi"].sum()
            st.metric("Total NOI", f"${total_noi:,.0f}")

    with col2:
        if "occupancy_rate" in df.columns:
            avg_occupancy = df["occupancy_rate"].mean()
            st.metric("Avg Occupancy", f"{avg_occupancy:.1f}%")

    with col3:
        if "revenue_per_unit" in df.columns:
            avg_rev_unit = df["revenue_per_unit"].mean()
            st.metric("Avg Revenue/Unit", f"${avg_rev_unit:,.0f}")

    with col4:
        if "expense_ratio" in df.columns:
            avg_expense_ratio = df["expense_ratio"].mean()
            st.metric("Avg Expense Ratio", f"{avg_expense_ratio:.1f}%")

    # Property KPI Table
    st.header("Property KPIs")
    display_cols = ["property_name"]
    for col in ["property_type", "submarket", "noi", "occupancy_rate", "revenue_per_unit", "expense_ratio"]:
        if col in df.columns:
            display_cols.append(col)

    st.dataframe(df[display_cols], use_container_width=True)

    # Trend Charts (if date column exists)
    if "date" in df.columns and "property_name" in df.columns:
        st.header("KPI Trends")

        selected_property = st.selectbox(
            "Select property for trend analysis",
            df["property_name"].unique()
        )

        property_data = df[df["property_name"] == selected_property].sort_values("date")

        if len(property_data) > 1:
            metric_options = [c for c in ["noi", "occupancy_rate", "revenue_per_unit", "expense_ratio"] if c in property_data.columns]
            selected_metric = st.selectbox("Select metric", metric_options)

            fig = px.line(
                property_data,
                x="date",
                y=selected_metric,
                title=f"{selected_metric.replace('_', ' ').title()} - {selected_property}"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Need multiple periods for trend analysis")


if __name__ == "__main__":
    main()
