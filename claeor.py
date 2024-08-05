

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

    # Add functionality to save inputs and continue execution
    st.button("Run Analysis")

    # Code to process the data and display performance metrics will go here

# Run the app
if __name__ == "__main__":
    start_claeor_tool()
