import streamlit as st
import pandas as pd

# Set up the page
st.set_page_config(page_title="Zaptron Financial Tracker", layout="wide")

# Sidebar navigation
st.sidebar.title("📊 Zaptron Financial Dashboard")
st.sidebar.markdown("Select a section to view details")

# Sample financial data
data = {
    "Category": ["Revenue", "Expenses", "Profit", "Upcoming Renewals"],
    "Amount ($)": [5000, 2000, 3000, 1500]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the dashboard
st.title("🚀 Zaptron Financial Dashboard")

st.subheader("💰 Financial Overview")
st.dataframe(df)

# Expense breakdown
st.subheader("📊 Expense Breakdown")
expenses = {
    "Software": ["GoHighLevel", "Zapier", "Instantly.ai", "Meta Ads", "Google Ads"],
    "Cost ($)": [97, 50, 100, 500, 300]
}
expenses_df = pd.DataFrame(expenses)
st.dataframe(expenses_df)

# Revenue tracking
st.subheader("📈 Client Payments")
clients = {
    "Client Name": ["Company A", "Company B", "Company C"],
    "Amount Paid ($)": [1500, 2000, 1500],
    "Payment Date": ["2025-03-10", "2025-03-05", "2025-03-07"]
}
clients_df = pd.DataFrame(clients)
st.dataframe(clients_df)

# Team spending breakdown
st.subheader("👥 Team Expenses")
team_expenses = {
    "Team Member": ["Ehsan", "Anita", "Dorsa"],
    "Expense Type": ["Business Lunch", "Ad Budget", "AI Development Tools"],
    "Cost ($)": [50, 300, 200]
}
team_df = pd.DataFrame(team_expenses)
st.dataframe(team_df)

st.subheader("🔄 Upcoming Payments & Renewals")
renewals = {
    "Software": ["GoHighLevel", "Zapier", "Google Ads"],
    "Renewal Date": ["2025-04-01", "2025-03-30", "2025-03-28"],
    "Amount ($)": [97, 50, 300]
}
renewals_df = pd.DataFrame(renewals)
st.dataframe(renewals_df)

st.success("✅ Financial tracking is live! Add more data for real-time insights.")

# Deployment note
st.info("🔗 This financial tracker will be deployed online for secure access.")
