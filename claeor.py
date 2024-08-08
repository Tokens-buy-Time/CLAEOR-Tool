
import streamlit as st
import math

# Initialize session state variables for assumptions if they don't exist
if "assumptions" not in st.session_state:
    st.session_state["assumptions"] = [
        169.50,  # Hourly Rental Rate
        113.00,  # Variable cost per hour
        24200.00, # Fixed Cost
        0.0833,  # Amortization rate
        0.06,    # Interest rate
        0.25,    # Tax Rate
        386000.00 # Acquisition cost per aircraft
    ]

# Initialize session state variables for operations data if they don't exist
if "operations_data" not in st.session_state:
    st.session_state["operations_data"] = [
        1, 
        250, 
        20, 
        10, 
        50.0,  
        0.33,  
        300000, 
        100000, 
        3000000, 
        60000000,
        2, 
        250, 
        20, 
        10, 
        50.0,  
        0.33,  
        400000, 
        500000, 
        3000000, 
        0,
        3, 
        500, 
        20, 
        10, 
        50.0,  
        0.33, 
        1000000, 
        1000000, 
        3000000, 
        0,
        4, 
        500, 
        20, 
        10, 
        50.0,  
        0.33, 
        1000000, 
        1000000, 
        3000000,
        0,
        5, 
        500, 
        20, 
        10, 
        50.0,  
        0.33, 
        1000000, 
        1000000, 
        3000000, 
        0,
        6, 
        500, 
        20, 
        10, 
        50.0,  
        0.33, 
        1000000, 
        1000000, 
        3000000, 
        0,
        7, 
        500, 
        20, 
        10, 
        50.0,  
        0.33, 
        1000000, 
        1000000, 
        3000000, 
        0,
        8, 
        500, 
        20, 
        10, 
        50.0,  
        0.33, 
        1000000, 
        1000000, 
        3000000, 
        0,
        9, 
        500, 
        20, 
        10, 
        50.0,  
        0.33, 
        1000000, 
        1000000, 
        3000000, 
        0,
        10, 
        500, 
        20, 
        10, 
        50.0, 
        0.33, 
        1000000, 
        1000000, 
        3000000, 
        0
    ]

# Function to display and save assumptions
def assumptions_screen():
    st.header("Assumptions")
    assumption_labels = [
        "Hourly Rental Rate",
        "Variable Cost per Hour",
        "Fixed Cost",
        "Amortization Rate",
        "Interest Rate",
        "Tax Rate",
        "Acquisition Cost per Aircraft"
    ]
    
    for i, label in enumerate(assumption_labels):
        st.session_state["assumptions"][i] = st.number_input(label, value=st.session_state["assumptions"][i])
    
    if st.button("Save Assumptions"):
        st.success("Assumptions saved!")


# Year 1 Screen 
# Function to display and save operations data
def operations_screen_1(rerun_1):
    st.header("Operations Data")
    Ops_labels = [
        "Year", 
        "Target Rental hrs", 
        "Size of fleet", 
        "Number of aircraft sold", 
        "Gross Margin %",
        "Debt to Equity ratio", 
        "MRO services Revenue $", 
        "Partnership Revenue $", 
        "Operating Expenses $", 
        "Investor Capital Calls $"
    ]
    
    Year_n = 1
    st.subheader(f"Year {Year_n}")

    for i in range(0,9):
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data"][i])
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
#           rerun_1=0
#       elif 
#           rerun_1=1



# Year 2 Screen
# Function to display and save operations data
def operations_screen_2(rerun_2):
    st.header("Operations Data")
    Ops_labels = [
        "Year", 
        "Target Rental hrs", 
        "Size of fleet", 
        "Number of aircraft sold", 
        "Gross Margin %", 
        "Debt to Equity ratio", 
        "MRO services Revenue $", 
        "Partnership Revenue $", 
        "Operating Expenses $", 
        "Investor Capital Calls $"
    ]
    
    Year_n = 2
    st.subheader(f"Year {Year_n}")

    for i in range(10,19):
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data"][i])
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")# rerun_1=0
#           rerun_2=0
#       elif 
#           rerun_2=1


# Year 3 Screen
# Function to display and save operations data
def operations_screen_3(rerun_3):
    st.header("Operations Data")
    Ops_labels = [
        "Year", 
        "Target Rental hrs", 
        "Size of fleet", 
        "Number of aircraft sold", 
        "Gross Margin %", 
        "Debt to Equity ratio", 
        "MRO services Revenue $", 
        "Partnership Revenue $", 
        "Operating Expenses $", 
        "Investor Capital Calls $"
    ]

    Year_n = 3
    st.subheader(f"Year {Year_n}")

    for i in range(20,29):
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data"][i])
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
#           rerun_3=0
#       elif 
#           rerun_3=1


# Year 4 Screen
# Function to display and save operations data
def operations_screen_4(rerun_4):
    st.header("Operations Data")
    Ops_labels = [
        "Year", 
        "Target Rental hrs", 
        "Size of fleet", 
        "Number of aircraft sold", 
        "Gross Margin %", 
        "Debt to Equity ratio", 
        "MRO services Revenue $", 
        "Partnership Revenue $", 
        "Operating Expenses $", 
        "Investor Capital Calls $"
    ]

    Year_n = 4
    st.subheader(f"Year {Year_n}")
    
    for i in range(30,39):
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data"][i])
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
#           rerun_4=0
#       elif 
#           rerun_4=1


# Year 5 Screen
# Function to display and save operations data
def operations_screen_5(rerun_5):
    st.header("Operations Data")
    Ops_labels = [
        "Year", 
        "Target Rental hrs", 
        "Size of fleet", 
        "Number of aircraft sold", 
        "Gross Margin %", 
        "Debt to Equity ratio", 
        "MRO services Revenue $", 
        "Partnership Revenue $", 
        "Operating Expenses $", 
        "Investor Capital Calls $"
    ]

    Year_n = 5
    st.subheader(f"Year {Year_n}")
    
    for i in range(40,49):
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data"][i])
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
#           rerun_5=0
#       elif 
#           rerun_5=1


# Year 6 Screen
# Function to display and save operations data
def operations_screen_6(rerun_6):
    st.header("Operations Data")
    Ops_labels = [
        "Year", 
        "Target Rental hrs", 
        "Size of fleet", 
        "Number of aircraft sold", 
        "Gross Margin %", 
        "Debt to Equity ratio", 
        "MRO services Revenue $", 
        "Partnership Revenue $", 
        "Operating Expenses $", 
        "Investor Capital Calls $"
    ]

    Year_n = 6
    st.subheader(f"Year {Year_n}")

    for i in range(50,59):
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data"][i])
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
#           rerun_6=0
#       elif 
#           rerun_6=1


# Year 7 Screen
# Function to display and save operations data
def operations_screen_7(rerun_7):
    st.header("Operations Data")
    Ops_labels = [
        "Year", 
        "Target Rental hrs", 
        "Size of fleet", 
        "Number of aircraft sold", 
        "Gross Margin %", 
        "Debt to Equity ratio", 
        "MRO services Revenue $", 
        "Partnership Revenue $", 
        "Operating Expenses $", 
        "Investor Capital Calls $"
    ]

    Year_n = 7
    st.subheader(f"Year {Year_n}")
    
    for i in range(60,69):
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data"][i])
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
#           rerun_7=0
#       elif 
#           rerun_7=1


# Year 8 Screen
# Function to display and save operations data
def operations_screen_8(rerun_8):
    st.header("Operations Data")
    Ops_labels = [
        "Year", 
        "Target Rental hrs", 
        "Size of fleet", 
        "Number of aircraft sold", 
        "Gross Margin %", 
        "Debt to Equity ratio", 
        "MRO services Revenue $", 
        "Partnership Revenue $", 
        "Operating Expenses $", 
        "Investor Capital Calls $"
    ]

    Year_n = 8
    st.subheader(f"Year {Year_n}")
    
    for i in range(70,79):
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data"][i])
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
#           rerun_8=0
#       elif 
#           rerun_8=1


# Year 9 Screen
# Function to display and save operations data
def operations_screen_9(rerun_9):
    st.header("Operations Data")
    Ops_labels = [
        "Year", 
        "Target Rental hrs", 
        "Size of fleet", 
        "Number of aircraft sold", 
        "Gross Margin %", 
        "Debt to Equity ratio", 
        "MRO services Revenue $", 
        "Partnership Revenue $", 
        "Operating Expenses $", 
        "Investor Capital Calls $"
    ]

    Year_n = 9
    st.subheader(f"Year {Year_n}")

    for i in range(80,89):
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data"][i])
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
#           rerun_9=0
#       elif 
#           rerun_9=1



# Year 10 Screen
# Function to display and save operations data
def operations_screen_10(rerun_10):
    st.header("Operations Data")
    Ops_labels = [
        "Year", 
        "Target Rental hrs", 
        "Size of fleet", 
        "Number of aircraft sold", 
        "Gross Margin %", 
        "Debt to Equity ratio", 
        "MRO services Revenue $", 
        "Partnership Revenue $", 
        "Operating Expenses $", 
        "Investor Capital Calls $"
    ]

    Year_n = 10
    st.subheader(f"Year {Year_n}")
    
    for i in range(90,99):
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data"][i])
        i=i+1
        st.session_state["operations_data"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data"][i])
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
#           rerun_10=0
#       elif 
#           rerun_10=1


# Function to display financial statements
def financial_statements_screen():
    st.header("Financial Statements")
    st.subheader("Income Statement")
    st.write("Income statement details will be displayed here.")
    
    st.subheader("Balance Sheet")
    st.write("Balance sheet details will be displayed here.")
    
    st.subheader("Cash Flow Statement")
    st.write("Cash flow statement details will be displayed here.")

# Function to display performance metrics
def performance_metrics_screen():
    st.header("Performance Metrics")
    st.write("Metrics will be calculated and displayed here based on the input data.")

# Home screen function
def home_screen():
    st.title("CLAEOR Tool")
    st.write("""
        Welcome to the CLAEOR Tool. This application allows you to input and save assumptions and operational data 
        for your business. You can then view the financial statements and performance metrics based on the provided 
        data. Use the sidebar to navigate through different sections of the tool.
    """)

# Indtructions function
def instructions_screen():
    st.title("Instructions")
    st.write("""
        To execute this App's functions, mobile users will notice an arrow (greater than equal character) at the top left hand corner of the screen when the device is being held in portrate mode.
        Click on the arrow to access a drop-down menu of available features.
        It is recommended that you adhere to the following sequence when operating the App.
        
        Start by :-
        
        (1) - Entering and saving Assumptions data.
        
        (2) - Following, enter and save operations data for each of the 10 years which the PE fund is to be in existence.
        
        (3) - Review Income statements, Balance Sheets, Cash flows and associated performance indicators for each of the 10 years.
        
        (4) - Review the key metrics at PE Fund exit; the end of year 10.
        

        You may change various parameter values within the assumptions and operations data, in order to assess the impact of the parameter, in context of other set parameter values, so as to assess, evaluate and draw insights.
        
        ⚠️ WARNING - 
        
           this app is NOT supported. It is for demonstration purposes only and must NOT be used to make any financial decisions or take any financial actions, based upon insights extracted as a direct or indirect result of its operation.

           Neither the author of this App nor the platform upon which it is being presented, accept any liability whatsoever, related to execution of this App. 
           
           It is the user's sole responsibility to exercise 'due diligence' and great prudence when it comes to matters of finance.

    """)

# Sidebar navigation
menu = st.sidebar.selectbox("Navigation", ["Home", "Instructions", "Assumptions", "Year 1 Operations", "Year 2 Operations", "Year 3 Operations", "Year 4 Operations", "Year 5 Operations", "Year 6 Operations", "Year 7 Operations", "Year 8 Operations", "Year 9 Operations", "Year 10 Operations", "Financial Statements", "Performance Metrics"])

if menu == "Home":
    home_screen()
elif menu == "Instructions":
    instructions_screen()
elif menu == "Assumptions":
    assumptions_screen()
elif menu == "Year 1 Operations":
#    rerun_1=0
#    operations_screen_1(rerun_1)
#    if rerun_1==1
#      rerun_1=0
#      operation_screen_1(rerun_1)
#    elif
elif menu == "Year 2 Operations":
#    rerun_2=0
# operations_screen_2(rerun_2)
#    if rerun_2==1
#      rerun_2=0
#      operation_screen_2(rerun_2)
#    elif
elif menu == "Year 3 Operations":
#    rerun_3=0
#    operations_screen_3(rerun_3)
#    if rerun_3==1
#      rerun_3=0
#      operation_screen_3(rerun_3)
#    elif
elif menu == "Year 4 Operations":
#    rerun_4=0
#    operations_screen_4(rerun_4)
#    if rerun_4==1
#      rerun_4=0
#      operation_screen_4(rerun_4)
#    elif
elif menu == "Year 5 Operations":
#    rerun_5=0
#    operations_screen_5(rerun_5)
#    if rerun_5==1
#      rerun_5=0
#      operation_screen_5(rerun_5)
#    elif
elif menu == "Year 6 Operations":
#    rerun_6=0
#    operations_screen_6(rerun_6)
#    if rerun_6==1
#      rerun_6=0
#      operation_screen_6(rerun_6)
#    elif
elif menu == "Year 7 Operations":
#    rerun_7=0
#    operations_screen_7(rerun_7)
#    if rerun_7==1
#      rerun_7=0
#      operation_screen_7(rerun_7)
#    elif
elif menu == "Year 8 Operations":
#    rerun_8=0
#    operations_screen_8(rerun_8)
#    if rerun_8==1
#      rerun_8=0
#      operation_screen_8(rerun_8)
#    elif
elif menu == "Year 9 Operations":
#    rerun_9=0
#    operations_screen_9(rerun_9)
#    if rerun_9==1
#      rerun_9=0
#      operation_screen_9(rerun_9)
#    elif
elif menu == "Year 10 Operations":
#    rerun_10=0
#    operations_screen_10(rerun_10)
#    if rerun_10==1
#      rerun_10=0
#      operation_screen_10(rerun_10)
#    elif
elif menu == "Financial Statements":
    financial_statements_screen()
elif menu == "Performance Metrics":
    performance_metrics_screen()

