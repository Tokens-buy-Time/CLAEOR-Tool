

import streamlit as st

def start_claeor_tool():
    # Placeholder values for assumptions
    assumptions = [
        169.50,  # Variable cost per hour
        113.00,  # Fixed cost per hour
        24200.00, # Hourly rental rate
        0.0833,  # Interest rate
        0.06,    # Amortization rate
        0.25,    # Tax rate
        50.0,    # Number of employees
        33.0,    # Total working days per year
        386000.00 # Acquisition cost per aircraft
    ]

    # Placeholder values for operations data per year
    operations_data = [
        # Format: [Year, No. of aircraft in fleet, No. of aircraft sold per year, Gross Margin %, Debt to Equity ratio, MRO services Revenue, Partnership Revenue, Operating Expenses]
        [1, 250, 20, 10, 300000, 100000, 3000000, 60000000],
        [2, 250, 20, 10, 400000, 500000, 3000000, 0],
        [3, 500, 20, 10, 1000000, 1000000, 3000000, 0],
        [4, 500, 20, 10, 1000000, 1000000, 3000000, 0],
        [5, 500, 20, 10, 1000000, 1000000, 3000000, 0],
        [6, 500, 20, 10, 1000000, 1000000, 3000000, 0],
        [7, 500, 20, 10, 1000000, 1000000, 3000000, 0],
        [8, 500, 20, 10, 1000000, 1000000, 3000000, 0],
        [9, 500, 20, 10, 1000000, 1000000, 3000000, 0],
        [10, 500, 20, 10, 1000000, 1000000, 3000000, 0]
    ]

    # Display and allow modification of assumptions
    st.title("CLAEOR Tool")
    st.header("Assumptions")
    assumption_labels = [
        "Variable Cost per Hour",
        "Fixed Cost per Hour",
        "Hourly Rental Rate",
        "Interest Rate",
        "Amortization Rate",
        "Tax Rate",
        "Number of Employees",
        "Total Working Days per Year",
        "Acquisition Cost per Aircraft"
    ]
    
    for i, label in enumerate(assumption_labels):
        assumptions[i] = st.number_input(label, value=assumptions[i])

    if st.button("Save Assumptions"):
        st.success("Assumptions saved!")

    # Display and allow modification of operations data
    st.header("Operations Data")
    for year_data in operations_data:
        st.subheader(f"Year {year_data[0]}")
        year_data[1] = st.number_input(f"No. of Aircraft in Fleet (Year {year_data[0]})", value=year_data[1])
        year_data[2] = st.number_input(f"No. of Aircraft Sold per Year (Year {year_data[0]})", value=year_data[2])
        year_data[3] = st.number_input(f"Gross Margin % (Year {year_data[0]})", value=year_data[3])
        year_data[4] = st.number_input(f"Debt to Equity Ratio (Year {year_data[0]})", value=year_data[4])
        year_data[5] = st.number_input(f"MRO Services Revenue (Year {year_data[0]})", value=year_data[5])
        year_data[6] = st.number_input(f"Partnership Revenue (Year {year_data[0]})", value=year_data[6])
        year_data[7] = st.number_input(f"Operating Expenses (Year {year_data[0]})", value=year_data[7])

        if st.button(f"Save Year {year_data[0]} Data"):
            st.success(f"Year {year_data[0]} data saved!")

    if st.button("Run Analysis"):
        st.success("Analysis complete!")
        # Display performance metrics
        st.header("Performance Metrics")
        st.write("Metrics will be calculated and displayed here based on the input data.")

        # Display financial statements
        st.header("Financial Statements")
        st.subheader("Income Statement")
        st.write("Income statement details will be displayed here.")

        st.subheader("Balance Sheet")
        st.write("Balance sheet details will be displayed here.")

        st.subheader("Cash Flow Statement")
        st.write("Cash flow statement details will be displayed here.")

    # Add functionality to save inputs and continue execution
    st.button("Save and Continue")

# Run the app
if __name__ == "__main__":
    start_claeor_tool()


import streamlit as st
import pandas as pd

def start_claeor_tool():
    st.title("Caribbean Luxury Aerial Experience - Operations Research Tool")

    menu = ["Home", "Assumptions Input", "Operational Data Input", "Financial Statements", "Metrics and Analysis"]
    choice = st.sidebar.selectbox("Menu", menu)

    if "assumptions" not in st.session_state:
        st.session_state["assumptions"] = {}

    if "operational_data" not in st.session_state:
        st.session_state["operational_data"] = {}

    def calculate_financials(year, assumptions, operational_data):
        billable_hours = operational_data["billable_hours"]
        num_aircraft = operational_data["num_aircraft"]
        aircraft_sold = operational_data["aircraft_sold"]
        mro_revenue = operational_data["mro_revenue"]
        partnership_revenue = operational_data["partnership_revenue"]
        operating_expenses = operational_data["operating_expenses"]
        capital_supplied = operational_data["capital_supplied"]

        revenue = assumptions["revenue_per_hour"] * billable_hours * num_aircraft
        aircraft_sale_revenue = assumptions["aircraft_price"] * aircraft_sold
        total_revenue = revenue + mro_revenue + partnership_revenue + aircraft_sale_revenue

        cogs = assumptions["variable_cost_per_hour"] * billable_hours * num_aircraft
        gross_profit = total_revenue * (assumptions["gross_margin"] / 100)

        depreciation = assumptions["fixed_costs"] * assumptions["depreciation_rate"]
        operating_profit = gross_profit - assumptions["fixed_costs"] - depreciation - operating_expenses
        interest = assumptions["fixed_costs"] * assumptions["interest_rate"]
        tax = operating_profit * assumptions["tax_rate"]
        net_profit = operating_profit - interest - tax

        assets = gross_profit - (interest + tax) + capital_supplied
        liabilities = assumptions["fixed_costs"] * (assumptions["debt_to_equity_ratio"] / 100)
        equity = net_profit

        cash_flow_operating = net_profit
        cash_flow_investing = -depreciation
        cash_flow_financing = assumptions["fixed_costs"] - interest + capital_supplied
        net_cash_flow = cash_flow_operating + cash_flow_investing + cash_flow_financing

        return {
            "revenue": total_revenue,
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
            "net_cash_flow": net_cash_flow,
            "capital_supplied": capital_supplied
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
        gross_margin = st.number_input("Gross Margin (%)", min_value=0.0, max_value=100.0)
        debt_to_equity_ratio = st.number_input("Debt to Equity Ratio (%)", min_value=0.0, max_value=100.0)
        aircraft_price = st.number_input("Price per Aircraft", min_value=0.0)

        if st.button("Save Assumptions"):
            st.session_state["assumptions"] = {
                "revenue_per_hour": revenue_per_hour,
                "variable_cost_per_hour": variable_cost_per_hour,
                "fixed_costs": fixed_costs,
                "depreciation_rate": depreciation_rate,
                "interest_rate": interest_rate,
                "tax_rate": tax_rate,
                "gross_margin": gross_margin,
                "debt_to_equity_ratio": debt_to_equity_ratio,
                "aircraft_price": aircraft_price
            }
            st.success("Assumptions saved!")

    elif choice == "Operational Data Input":
        st.subheader("Input Operational Data")
        year = st.selectbox("Year", range(1, 11))
        billable_hours = st.number_input("Billable Hours", min_value=0)
        num_aircraft = st.number_input("Number of Aircraft in Fleet", min_value=0)
        aircraft_sold = st.number_input("Number of Aircraft Sold", min_value=0)
        mro_revenue = st.number_input("MRO Services Revenue", min_value=0.0)
        partnership_revenue = st.number_input("Partnership Revenue", min_value=0.0)
        operating_expenses = st.number_input("Operating Expenses", min_value=0.0)
        capital_supplied = st.number_input("Capital Supplied by Investors", min_value=0.0)

        if st.button("Save Operational Data"):
            st.session_state["operational_data"][year] = {
                "billable_hours": billable_hours,
                "num_aircraft": num_aircraft,
                "aircraft_sold": aircraft_sold,
                "mro_revenue": mro_revenue,
                "partnership_revenue": partnership_revenue,
                "operating_expenses": operating_expenses,
                "capital_supplied": capital_supplied
            }
            st.success(f"Operational data for Year {year} saved!")

    elif choice == "Financial Statements":
        st.subheader("Financial Statements")
        statement_year = st.selectbox("Select Year", range(1, 11))

        if st.session_state["assumptions"] and statement_year in st.session_state["operational_data"]:
            assumptions = st.session_state["assumptions"]
            operational_data = st.session_state["operational_data"][statement_year]

            financials = calculate_financials(statement_year, assumptions, operational_data)

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
            total_capital_supplied = 0
            for year, data in operational_data.items():
                financials = calculate_financials(year, assumptions, data)
                all_financials[year] = financials 
                total_capital_supplied += financials["capital_supplied"]

        df_financials = pd.DataFrame(all_financials).T

        st.write("Metrics at Fund's Exit (End of Year 10)")
        total_revenue_10 = df_financials["revenue"].sum()
        total_net_profit_10 = df_financials["net_profit"].sum()
        total_assets_10 = df_financials["assets"].sum()
        total_liabilities_10 = df_financials["liabilities"].sum()
        total_equity_10 = df_financials["equity"].sum()
        total_capital_supplied_10 = df_financials["capital_supplied"].sum()

        st.write(f"Total Revenue over 10 years: ${total_revenue_10:.2f}")
        st.write(f"Total Net Profit over 10 years: ${total_net_profit_10:.2f}")
        st.write(f"Total Assets at Year 10: ${total_assets_10:.2f}")
        st.write(f"Total Liabilities at Year 10: ${total_liabilities_10:.2f}")
        st.write(f"Total Equity at Year 10: ${total_equity_10:.2f}")
        st.write(f"Total Capital Supplied by Investors over 10 years: ${total_capital_supplied:.2f}")

        irr = ((total_net_profit_10 / assumptions["fixed_costs"]) ** (1 / 10)) - 1
        roi = (total_net_profit_10 / assumptions["fixed_costs"]) * 100

        st.write(f"Internal Rate of Return (IRR) over 10 years: {irr:.2%}")
        st.write(f"Return on Investment (ROI) over 10 years: {roi:.2f}%")
    else:
        st.warning("Please input assumptions and operational data first.")

if __name__ == "__main__":
     start_claeor_tool()
