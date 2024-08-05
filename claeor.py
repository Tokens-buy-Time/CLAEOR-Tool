
import pandas as pd
import streamlit as st

# Function to read default data from Assumptions.txt
def load_assumptions():
    assumptions = {}
    with open('Assumptions.txt', 'r') as file:
        lines = file.readlines()
        assumptions["fixed_costs"] = float(lines[0].strip())
        assumptions["variable_costs_per_hour"] = float(lines[1].strip())
        assumptions["hours_per_year"] = int(lines[2].strip())
        assumptions["aircraft_acquisition_cost"] = float(lines[3].strip())
        assumptions["no_of_aircraft_in_fleet"] = int(lines[4].strip())
        assumptions["no_of_aircraft_sold_per_year"] = int(lines[5].strip())
        assumptions["gross_margin_percent"] = float(lines[6].strip())
        assumptions["debt_to_equity_ratio"] = float(lines[7].strip())
        assumptions["capital_supplied"] = float(lines[8].strip())
    return assumptions

# Function to read default data from Operations-Data.txt
def load_operations_data():
    operations_data = {}
    with open('Operations-Data.txt', 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 8):
            year = int(lines[i].strip())
            operations_data[year] = {
                "mro_services_revenue": float(lines[i + 1].strip()),
                "partnership_revenue": float(lines[i + 2].strip()),
                "operating_expenses": float(lines[i + 3].strip()),
                "no_of_aircraft_in_fleet": int(lines[i + 4].strip()),
                "no_of_aircraft_sold_per_year": int(lines[i + 5].strip()),
                "gross_margin_percent": float(lines[i + 6].strip()),
                "debt_to_equity_ratio": float(lines[i + 7].strip())
            }
    return operations_data

def start_claeor_tool():
    st.title("CLAEOR Tool")

    # Load default data
    assumptions = load_assumptions()
    operations_data = load_operations_data()

    # Display and modify assumptions
    st.header("Assumptions")
    fixed_costs = st.number_input("Fixed Costs", value=assumptions["fixed_costs"])
    variable_costs_per_hour = st.number_input("Variable Costs per Hour", value=assumptions["variable_costs_per_hour"])
    hours_per_year = st.number_input("Hours per Year", value=assumptions["hours_per_year"])
    aircraft_acquisition_cost = st.number_input("Aircraft Acquisition Cost", value=assumptions["aircraft_acquisition_cost"])
    capital_supplied = st.number_input("Capital Supplied by Investors", value=assumptions["capital_supplied"])

    if st.button("Save Assumptions"):
        assumptions["fixed_costs"] = fixed_costs
        assumptions["variable_costs_per_hour"] = variable_costs_per_hour
        assumptions["hours_per_year"] = hours_per_year
        assumptions["aircraft_acquisition_cost"] = aircraft_acquisition_cost
        assumptions["capital_supplied"] = capital_supplied
        st.success("Assumptions saved successfully!")

    # Display and modify operations data
    st.header("Operational Data")
    all_operational_data = {}
    for year in range(1, 11):
        st.subheader(f"Year {year}")
        mro_services_revenue = st.number_input(f"MRO Services Revenue (Year {year})", value=operations_data[year]["mro_services_revenue"])
        partnership_revenue = st.number_input(f"Partnership Revenue (Year {year})", value=operations_data[year]["partnership_revenue"])
        operating_expenses = st.number_input(f"Operating Expenses (Year {year})", value=operations_data[year]["operating_expenses"])
        no_of_aircraft_in_fleet = st.number_input(f"No. of Aircraft in Fleet (Year {year})", value=operations_data[year]["no_of_aircraft_in_fleet"])
        no_of_aircraft_sold_per_year = st.number_input(f"No. of Aircraft Sold per Year (Year {year})", value=operations_data[year]["no_of_aircraft_sold_per_year"])
        gross_margin_percent = st.number_input(f"Gross Margin % (Year {year})", value=operations_data[year]["gross_margin_percent"])
        debt_to_equity_ratio = st.number_input(f"Debt to Equity Ratio (Year {year})", value=operations_data[year]["debt_to_equity_ratio"])

        all_operational_data[year] = {
            "mro_services_revenue": mro_services_revenue,
            "partnership_revenue": partnership_revenue,
            "operating_expenses": operating_expenses,
            "no_of_aircraft_in_fleet": no_of_aircraft_in_fleet,
            "no_of_aircraft_sold_per_year": no_of_aircraft_sold_per_year,
            "gross_margin_percent": gross_margin_percent,
            "debt_to_equity_ratio": debt_to_equity_ratio
        }

    if st.button("Save Operational Data"):
        st.success("Operational data saved successfully!")

    # Execute calculations
    if st.button("Execute Calculations"):
        all_financials = {}
        total_capital_supplied = 0

        for year in range(1, 11):
            financials = calculate_financials(
                year,
                assumptions["fixed_costs"],
                assumptions["variable_costs_per_hour"],
                assumptions["hours_per_year"],
                assumptions["aircraft_acquisition_cost"],
                all_operational_data[year]["no_of_aircraft_in_fleet"],
                all_operational_data[year]["no_of_aircraft_sold_per_year"],
                all_operational_data[year]["gross_margin_percent"],
                all_operational_data[year]["debt_to_equity_ratio"],
                all_operational_data[year]["mro_services_revenue"],
                all_operational_data[year]["partnership_revenue"],
                all_operational_data[year]["operating_expenses"]
            )
            all_financials[year] = financials
            total_capital_supplied += assumptions["capital_supplied"]

        df_financials = pd.DataFrame(all_financials).T

        st.write("Metrics at Fund's Exit (End of Year 10)")
        total_revenue_10 = df_financials["revenue"].sum()
        total_net_profit_10 = df_financials["net_profit"].sum()
        total_assets_10 = df_financials["assets"].sum()
        total_liabilities_10 = df_financials["liabilities"].sum()
        total_equity_10 = df_financials["equity"].sum()

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

if __name__ == '__main__':
    start_claeor_tool()
