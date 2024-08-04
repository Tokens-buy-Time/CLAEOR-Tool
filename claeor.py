
import streamlit as st
import pandas as pd

# Initialize Streamlit app
st.title("Caribbean Luxury Aerial Experience - Operations Research Tool")

# Navigation Menu
menu = ["Home", "Assumptions Input", "Operational Data Input", "Financial Statements", "Metrics and Analysis"]
choice = st.sidebar.selectbox("Menu", menu)

# Store inputs and results in session state
if "assumptions" not in st.session_state:
    st.session_state["assumptions"] = {}

if "operational_data" not in st.session_state:
    st.session_state["operational_data"] = {}

# Function to perform financial calculations for a given year
def calculate_financials(year, assumptions, billable_hours):
    revenue = assumptions["revenue_per_hour"] * billable_hours
    cogs = assumptions["variable_cost_per_hour"] * billable_hours
    gross_profit = revenue - cogs
    depreciation = assumptions["fixed_costs"] * assumptions["depreciation_rate"]
    operating_profit = gross_profit - assumptions["fixed_costs"] - depreciation
    interest = assumptions["fixed_costs"] * assumptions["interest_rate"]
    tax = operating_profit * assumptions["tax_rate"]
    net_profit = operating_profit - interest - tax

    assets = gross_profit - (interest + tax)
    liabilities = assumptions["fixed_costs"]
    equity = net_profit

    cash_flow_operating = net_profit
    cash_flow_investing = -depreciation
    cash_flow_financing = assumptions["fixed_costs"] - interest
    net_cash_flow = cash_flow_operating + cash_flow_investing + cash_flow_financing

    return {
        "revenue": revenue,
        "cogs": cogs,
        "gross_profit": gross_profit,
        "depreciation": depreciation,
        "operating_profit": operating_profit,
        "interest": interest,
        "tax": tax,
        "net_profit": net_profit,
        "assets": assets,
        "liabilities": liabilities,
        "equity": equity,
        "cash_flow_operating": cash_flow_operating,
        "cash_flow_investing": cash_flow_investing,
        "cash_flow_financing": cash_flow_financing,
        "net_cash_flow": net_cash_flow
    }

if choice == "Home":
    st.subheader("Welcome to the Caribbean Luxury Aerial Experience Operations Research Tool")
    st.write("Navigate through the menu to input assumptions, operational data, view financial statements, and perform sensitivity analysis.")

elif choice == "Assumptions Input":
    st.subheader("Input Assumptions")
    revenue_per_hour = st.number_input("Revenue per Hour", min_value=0.0)
    variable_cost_per_hour = st.number_input("Variable Cost per Hour", min_value=0.0)
    fixed_costs = st.number_input("Total Fixed Costs", min_value=0.0)
    depreciation_rate = st.number_input("Depreciation Rate", min_value=0.0, max_value=1.0)
    interest_rate = st.number_input("Interest Rate", min_value=0.0, max_value=1.0)
    tax_rate = st.number_input("Tax Rate", min_value=0.0, max_value=1.0)

    if st.button("Save Assumptions"):
        st.session_state["assumptions"] = {
            "revenue_per_hour": revenue_per_hour,
            "variable_cost_per_hour": variable_cost_per_hour,
            "fixed_costs": fixed_costs,
            "depreciation_rate": depreciation_rate,
            "interest_rate": interest_rate,
            "tax_rate": tax_rate
        }
        st.success("Assumptions saved!")

elif choice == "Operational Data Input":
    st.subheader("Input Operational Data")
    year = st.selectbox("Year", range(1, 11))
    billable_hours = st.number_input("Billable Hours", min_value=0)

    if st.button("Save Operational Data"):
        st.session_state["operational_data"][year] = billable_hours
        st.success(f"Operational data for Year {year} saved!")

elif choice == "Financial Statements":
    st.subheader("Financial Statements")
    statement_year = st.selectbox("Select Year", range(1, 11))

    if st.session_state["assumptions"] and statement_year in st.session_state["operational_data"]:
        assumptions = st.session_state["assumptions"]
        billable_hours = st.session_state["operational_data"][statement_year]

        financials = calculate_financials(statement_year, assumptions, billable_hours)

        # Display financial statements
        st.write(f"Income Statement for Year {statement_year}")
        st.write(f"Revenue: ${financials['revenue']:.2f}")
        st.write(f"COGS: ${financials['cogs']:.2f}")
        st.write(f"Gross Profit: ${financials['gross_profit']:.2f}")
        st.write(f"Operating Expenses: ${assumptions['fixed_costs'] + financials['depreciation']:.2f}")
        st.write(f"Operating Profit: ${financials['operating_profit']:.2f}")
        st.write(f"Interest Expense: ${financials['interest']:.2f}")
        st.write(f"Taxes: ${financials['tax']:.2f}")
        st.write(f"Net Profit: ${financials['net_profit']:.2f}")

        st.write(f"Balance Sheet for Year {statement_year}")
        st.write(f"Assets: ${financials['assets']:.2f}")
        st.write(f"Liabilities: ${financials['liabilities']:.2f}")
        st.write(f"Equity: ${financials['equity']:.2f}")

        st.write(f"Cash Flow Statement for Year {statement_year}")
        st.write(f"Operating Cash Flow: ${financials['cash_flow_operating']:.2f}")
        st.write(f"Investing Cash Flow: ${financials['cash_flow_investing']:.2f}")
        st.write(f"Financing Cash Flow: ${financials['cash_flow_financing']:.2f}")
        st.write(f"Net Cash Flow: ${financials['net_cash_flow']:.2f}")
    else:
        st.warning("Please input assumptions and operational data first.")

elif choice == "Metrics and Analysis":
    st.subheader("Metrics and Analysis")
    
    if st.session_state["assumptions"] and st.session_state["operational_data"]:
        assumptions = st.session_state["assumptions"]
        operational_data = st.session_state["operational_data"]

        all_financials = {}
        for year, billable_hours in operational_data.items():
            all_financials[year] = calculate_financials(year, assumptions, billable_hours)

        df_financials = pd.DataFrame(all_financials).T

        # Display key metrics
        st.write("Key Metrics")
        st.write(f"Total Revenue: ${df_financials['revenue'].sum():.2f}")
        st.write(f"Total Net Profit: ${df_financials['net_profit'].sum():.2f}")

        # Sensitivity Analysis: Varying Revenue per Hour
        sensitivity_results = []
        for revenue_adjustment in range(-20, 21, 5):  # Vary revenue by -20% to +20% in 5% increments
            adjusted_assumptions = assumptions.copy()
            adjusted_assumptions["revenue_per_hour"] *= (1 + revenue_adjustment / 100)
            total_net_profit = sum(calculate_financials(year, adjusted_assumptions, billable_hours)["net_profit"]
                                   for year, billable_hours in operational_data.items())
            sensitivity_results.append((revenue_adjustment, total_net_profit))

        sensitivity_df = pd.DataFrame(sensitivity_results, columns=["Revenue Adjustment (%)", "Total Net Profit"])

        st.write("Sensitivity Analysis: Varying Revenue per Hour")
        st.line_chart(sensitivity_df.set_index("Revenue Adjustment (%)"))

    else:
        st.warning("Please input assumptions and operational data first.")

st.write("Developed by ChatGPT")
