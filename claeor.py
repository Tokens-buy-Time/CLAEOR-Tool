
import streamlit as st
import pandas as pd
import math
import matplotlib.pyplot as plt

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
if "operations_data_1" not in st.session_state:
    st.session_state["operations_data_1"] = [
        1, # Year
        250, # Billable hours
        20, # Number of fleet aircraft
        25, # Number of aircraft sold
        50.0, # Gross Margin percentage
        0.33,  # Debt-Equity ratio
        500000, # MRO & FBO Revenue
        100000, # Partnership Revenue
        1000000, # Expenses
        23000000 # Capital Calls
    ]
    
# Initialize session state variables for operations data if they don't exist
if "operations_data_2" not in st.session_state:
    st.session_state["operations_data_2"] = [      
        2, 
        250, 
        20, 
        35, 
        50.0,  
        0.33,  
        750000, 
        500000, 
        1100000, 
        0
    ]

# Initialize session state variables for operations data if they don't exist
if "operations_data_3" not in st.session_state:
    st.session_state["operations_data_3"] = [
        3, 
        500, 
        20, 
        40, 
        50.0,  
        0.33, 
        1000000, 
        1000000, 
        1200000, 
        0
    ]

# Initialize session state variables for operations data if they don't exist
if "operations_data_4" not in st.session_state:
    st.session_state["operations_data_4"] = [
        4, 
        500, 
        20, 
        42, 
        50.0,  
        0.33, 
        1250000, 
        1000000, 
        1300000,
        0
    ]

# Initialize session state variables for operations data if they don't exist
if "operations_data_5" not in st.session_state:
    st.session_state["operations_data_5"] = [
        5, 
        500, 
        20, 
        45,
        50.0,  
        0.33, 
        1500000, 
        1000000, 
        1400000, 
        0
    ]

# Initialize session state variables for operations data if they don't exist
if "operations_data_6" not in st.session_state:
    st.session_state["operations_data_6"] = [    
        6, 
        500, 
        20, 
        45, 
        50.0,  
        0.33, 
        1600000, 
        1000000, 
        1500000, 
        0
    ]

# Initialize session state variables for operations data if they don't exist
if "operations_data_7" not in st.session_state:
    st.session_state["operations_data_7"] = [
        7, 
        500, 
        20, 
        43, 
        50.0,  
        0.33, 
        1700000, 
        1000000, 
        1500000, 
        0
    ]

# Initialize session state variables for operations data if they don't exist
if "operations_data_8" not in st.session_state:
    st.session_state["operations_data_8"] = [
        8, 
        500, 
        20, 
        41, 
        50.0,  
        0.33, 
        1800000, 
        1000000, 
        1500000, 
        0
    ]

# Initialize session state variables for operations data if they don't exist
if "operations_data_9" not in st.session_state:
    st.session_state["operations_data_9"] = [
        9, 
        500, 
        20, 
        40, 
        50.0,  
        0.33, 
        1900000, 
        1000000, 
        1500000, 
        0
    ]

# Initialize session state variables for operations data if they don't exist
if "operations_data_10" not in st.session_state:
    st.session_state["operations_data_10"] = [
        10, 
        500, 
        20, 
        40, 
        50.0, 
        0.33, 
        2000000, 
        1000000, 
        1500000, 
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
def operations_screen_1():
    st.header("Operations Data")
    Ops_labels_1 = [
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

    for i, label_1 in enumerate(Ops_labels_1):
        i=i+1
        st.session_state["operations_data_1"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data_1"][i])
        i=i+1
        st.session_state["operations_data_1"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data_1"][i])
        i=i+1
        st.session_state["operations_data_1"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data_1"][i])
        i=i+1
        st.session_state["operations_data_1"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data_1"][i])
        i=i+1
        st.session_state["operations_data_1"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data_1"][i])
        i=i+1
        st.session_state["operations_data_1"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data_1"][i])
        i=i+1
        st.session_state["operations_data_1"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data_1"][i])
        i=i+1
        st.session_state["operations_data_1"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data_1"][i])
        i=i+1
        st.session_state["operations_data_1"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data_1"][i])

        st.write(" ")
        st.write("press button below to save above entries")
        st.write(" ")
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
        break

# Year 2 Screen
# Function to display and save operations data
def operations_screen_2():
    st.header("Operations Data")
    Ops_labels_2 = [
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

    for i, label_2 in enumerate(Ops_labels_2):
        i=i+1
        st.session_state["operations_data_2"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data_2"][i])
        i=i+1
        st.session_state["operations_data_2"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data_2"][i])
        i=i+1
        st.session_state["operations_data_2"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data_2"][i])
        i=i+1
        st.session_state["operations_data_2"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data_2"][i])
        i=i+1
        st.session_state["operations_data_2"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data_2"][i])
        i=i+1
        st.session_state["operations_data_2"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data_2"][i])
        i=i+1
        st.session_state["operations_data_2"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data_2"][i])
        i=i+1
        st.session_state["operations_data_2"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data_2"][i])
        i=i+1
        st.session_state["operations_data_2"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data_2"][i])
  
        st.write(" ")
        st.write("press button below to save above entries")
        st.write(" ")
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
        break


# Year 3 Screen
# Function to display and save operations data
def operations_screen_3():
    st.header("Operations Data")
    Ops_labels_3 = [
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

    for i, label_3 in enumerate(Ops_labels_3):
        i=i+1
        st.session_state["operations_data_3"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data_3"][i])
        i=i+1
        st.session_state["operations_data_3"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data_3"][i])
        i=i+1
        st.session_state["operations_data_3"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data_3"][i])
        i=i+1
        st.session_state["operations_data_3"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data_3"][i])
        i=i+1
        st.session_state["operations_data_3"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data_3"][i])
        i=i+1
        st.session_state["operations_data_3"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data_3"][i])
        i=i+1
        st.session_state["operations_data_3"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data_3"][i])
        i=i+1
        st.session_state["operations_data_3"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data_3"][i])
        i=i+1
        st.session_state["operations_data_3"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data_3"][i])
  
        st.write(" ")
        st.write("press button below to save above entries")
        st.write(" ")
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
        break


# Year 4 Screen
# Function to display and save operations data
def operations_screen_4():
    st.header("Operations Data")
    Ops_labels_4 = [
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
    
    for i, label_4 in enumerate(Ops_labels_4):
        i=i+1
        st.session_state["operations_data_4"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data_4"][i])
        i=i+1
        st.session_state["operations_data_4"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data_4"][i])
        i=i+1
        st.session_state["operations_data_4"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data_4"][i])
        i=i+1
        st.session_state["operations_data_4"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data_4"][i])
        i=i+1
        st.session_state["operations_data_4"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data_4"][i])
        i=i+1
        st.session_state["operations_data_4"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data_4"][i])
        i=i+1
        st.session_state["operations_data_4"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data_4"][i])
        i=i+1
        st.session_state["operations_data_4"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data_4"][i])
        i=i+1
        st.session_state["operations_data_4"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data_4"][i])
  
        st.write(" ")
        st.write("press button below to save above entries")
        st.write(" ")
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
        break


# Year 5 Screen
# Function to display and save operations data
def operations_screen_5():
    st.header("Operations Data")
    Ops_labels_5 = [
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
    
    for i, label_5 in enumerate(Ops_labels_5):
        i=i+1
        st.session_state["operations_data_5"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data_5"][i])
        i=i+1
        st.session_state["operations_data_5"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data_5"][i])
        i=i+1
        st.session_state["operations_data_5"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data_5"][i])
        i=i+1
        st.session_state["operations_data_5"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data_5"][i])
        i=i+1
        st.session_state["operations_data_5"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data_5"][i])
        i=i+1
        st.session_state["operations_data_5"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data_5"][i])
        i=i+1
        st.session_state["operations_data_5"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data_5"][i])
        i=i+1
        st.session_state["operations_data_5"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data_5"][i])
        i=i+1
        st.session_state["operations_data_5"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data_5"][i])
  
        st.write(" ")
        st.write("press button below to save above entries")
        st.write(" ")
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
        break


# Year 6 Screen
# Function to display and save operations data
def operations_screen_6():
    st.header("Operations Data")
    Ops_labels_6 = [
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

    for i, label_6 in enumerate(Ops_labels_6):
        i=i+1
        st.session_state["operations_data_6"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data_6"][i])
        i=i+1
        st.session_state["operations_data_6"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data_6"][i])
        i=i+1
        st.session_state["operations_data_6"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data_6"][i])
        i=i+1
        st.session_state["operations_data_6"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data_6"][i])
        i=i+1
        st.session_state["operations_data_6"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data_6"][i])
        i=i+1
        st.session_state["operations_data_6"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data_6"][i])
        i=i+1
        st.session_state["operations_data_6"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data_6"][i])
        i=i+1
        st.session_state["operations_data_6"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data_6"][i])
        i=i+1
        st.session_state["operations_data_6"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data_6"][i])
 
        st.write(" ")
        st.write("press button below to save above entries")
        st.write(" ")
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
        break


# Year 7 Screen
# Function to display and save operations data
def operations_screen_7():
    st.header("Operations Data")
    Ops_labels_7 = [
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
    
    for i, label_7 in enumerate(Ops_labels_7):
        i=i+1
        st.session_state["operations_data_7"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data_7"][i])
        i=i+1
        st.session_state["operations_data_7"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data_7"][i])
        i=i+1
        st.session_state["operations_data_7"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data_7"][i])
        i=i+1
        st.session_state["operations_data_7"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data_7"][i])
        i=i+1
        st.session_state["operations_data_7"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data_7"][i])
        i=i+1
        st.session_state["operations_data_7"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data_7"][i])
        i=i+1
        st.session_state["operations_data_7"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data_7"][i])
        i=i+1
        st.session_state["operations_data_7"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data_7"][i])
        i=i+1
        st.session_state["operations_data_7"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data_7"][i])
  
        st.write(" ")
        st.write("press button below to save above entries")
        st.write(" ")
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
        break


# Year 8 Screen
# Function to display and save operations data
def operations_screen_8():
    st.header("Operations Data")
    Ops_labels_8 = [
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
    
    for i, label_8 in enumerate(Ops_labels_8):
        i=i+1
        st.session_state["operations_data_8"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data_8"][i])
        i=i+1
        st.session_state["operations_data_8"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data_8"][i])
        i=i+1
        st.session_state["operations_data_8"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data_8"][i])
        i=i+1
        st.session_state["operations_data_8"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data_8"][i])
        i=i+1
        st.session_state["operations_data_8"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data_8"][i])
        i=i+1
        st.session_state["operations_data_8"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data_8"][i])
        i=i+1
        st.session_state["operations_data_8"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data_8"][i])
        i=i+1
        st.session_state["operations_data_8"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data_8"][i])
        i=i+1
        st.session_state["operations_data_8"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data_8"][i])
  
        st.write(" ")
        st.write("press button below to save above entries")
        st.write(" ")
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
        break


# Year 9 Screen
# Function to display and save operations data
def operations_screen_9():
    st.header("Operations Data")
    Ops_labels_9 = [
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

    for i, label_9 in enumerate(Ops_labels_9):
        i=i+1
        st.session_state["operations_data_9"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data_9"][i])
        i=i+1
        st.session_state["operations_data_9"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data_9"][i])
        i=i+1
        st.session_state["operations_data_9"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data_9"][i])
        i=i+1
        st.session_state["operations_data_9"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data_9"][i])
        i=i+1
        st.session_state["operations_data_9"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data_9"][i])
        i=i+1
        st.session_state["operations_data_9"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data_9"][i])
        i=i+1
        st.session_state["operations_data_9"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data_9"][i])
        i=i+1
        st.session_state["operations_data_9"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data_9"][i])
        i=i+1
        st.session_state["operations_data_9"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data_9"][i])
   
        st.write(" ")
        st.write("press button below to save above entries")
        st.write(" ")
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
        break


# Year 10 Screen
# Function to display and save operations data
def operations_screen_10():
    st.header("Operations Data")
    Ops_labels_10 = [
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
    
    for i, label_10 in enumerate(Ops_labels_10):
        i=i+1
        st.session_state["operations_data_10"][i] = st.number_input(label="Target Rental hrs", value=st.session_state["operations_data_10"][i])
        i=i+1
        st.session_state["operations_data_10"][i] = st.number_input(label="Size of fleet", value=st.session_state["operations_data_10"][i])
        i=i+1
        st.session_state["operations_data_10"][i] = st.number_input(label="Number of aircraft sold", value=st.session_state["operations_data_10"][i])
        i=i+1
        st.session_state["operations_data_10"][i] = st.number_input(label="Gross Margin %", value=st.session_state["operations_data_10"][i])
        i=i+1
        st.session_state["operations_data_10"][i] = st.number_input(label="Debt to Equity ratio", value=st.session_state["operations_data_10"][i])
        i=i+1
        st.session_state["operations_data_10"][i] = st.number_input(label="MRO services Revenue $", value=st.session_state["operations_data_10"][i])
        i=i+1
        st.session_state["operations_data_10"][i] = st.number_input(label="Partnership Revenue $", value=st.session_state["operations_data_10"][i])
        i=i+1
        st.session_state["operations_data_10"][i] = st.number_input(label="Operating Expenses $", value=st.session_state["operations_data_10"][i])
        i=i+1
        st.session_state["operations_data_10"][i] = st.number_input(label="Investor Capital Calls $", value=st.session_state["operations_data_10"][i])
  
        st.write(" ")
        st.write("press button below to save above entries")
        st.write(" ")
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
        break



# Function to calculate and display financial statements
def financial_statements_screen(Year_n, assumptions, operations_data):
    st.header("Financial Statements")    
    st.write(" ")
    st.write("Each year's Income, Balance, and Cash Flow Statement uses the last saved data for the particular year. The respective statements appear directly below and they reflect the saved operations data for the year in question, as well as the general assumptions supplied.")
    
    # Basic Financial performance Data
    financials = calculate_financials(Year_n, assumptions, operations_data)
 
    # Calculations to display the Income Statement, Balance Sheet & Cash flow Statement
    Income_Year(financials)
    Balance_Sheet_Year(financials)
    Cash_Flow_Year(financials)
    

def calculate_financials(Year_n, assumptions, operations_data):
    # Extract relevant data
    billable_hours = operations_data[1]
    num_aircraft = operations_data[2]
    aircraft_sold = operations_data[3]
    gross_margin = operations_data[4]
    debt_equity_ratio = operations_data[5]
    mro_revenue = operations_data[6]
    partnership_revenue = operations_data[7]
    operating_expenses = operations_data[8]
    capital_supplied = operations_data[9]
    rental_revenue_rate = assumptions[0]
    variable_cost_per_hour = assumptions[1]
    fixed_cost = assumptions[2]
    amortization_rate = assumptions[3]
    interest_rate = assumptions[4]
    tax_rate = assumptions[5]
    aircraft_price = assumptions[6]
    
    # Calculate various financials
    revenue = rental_revenue_rate * billable_hours * num_aircraft
    aircraft_sales_revenue = aircraft_price * aircraft_sold
    total_revenue = revenue + mro_revenue + partnership_revenue + aircraft_sales_revenue

    aircraft_purchase_price = (aircraft_price / (1 + (gross_margin / 100)))
    aircraft_order_cost = num_aircraft * aircraft_purchase_price
    
    depreciation_rate = (amortization_rate + interest_rate) / 2 
    depreciation_expense = depreciation_rate * capital_supplied  # Capital Supplied used to purchase long-term assets only
    operating_expenses = fixed_cost + depreciation_expense  # fixed_cost are non-capital expenditures

    cogs = variable_cost_per_hour * billable_hours * num_aircraft
    gross_profit = total_revenue * (gross_margin / 100)
    
    operating_profit = gross_profit - fixed_cost - operating_expenses
    interest_expense = fixed_cost * interest_rate
    tax = operating_profit * tax_rate
    net_profit = operating_profit - interest_expense - tax
    
    assets = gross_profit - (interest_expense + tax) + capital_supplied
    liabilities = fixed_cost * debt_equity_ratio
    equity = net_profit

    cash_flow_operating = net_profit
    cash_flow_investing = -depreciation_expense
    cash_flow_financing = fixed_cost - interest_expense + capital_supplied
    net_cash_flow = cash_flow_operating + cash_flow_investing + cash_flow_financing

    return {
        "Year_n": Year_n,
        "total_revenue": total_revenue,
        "cogs": cogs,
        "gross_profit": gross_profit,
        "depreciation": depreciation_expense,
        "operating_profit": operating_profit,
        "interest_expense": interest_expense,
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


# Function to display Income Statement
def Income_Year(financials):
    st.write(" ")
    st.subheader("Income Statement")
    st.write("Income Statement for Year  ", Year_n) 
    st.write(" ")
    st.write(f"Revenue: ${financials['total_revenue']:.2f}")
    st.write(f"COGS: ${financials['cogs']:.2f}")
    st.write(f"Gross Profit: ${financials['gross_profit']:.2f}")

    st.write(f"Operating Expenses: ${assumptions[2] + financials['depreciation']:.2f}")
    st.write(f"Operating Profit: ${financials['operating_profit']:.2f}")
            
    st.write(f"Interest Expense: ${financials['interest_expense']:.2f}")
    st.write(f"Taxes: ${financials['tax']:.2f}")
            
    st.write(f"Net Profit: ${financials['net_profit']:.2f}")
    st.write(" ")


# Function to display Balance Sheet Statement
def Balance_Sheet_Year(financials):
    st.write(" ")
    st.subheader("Balance Sheet")
    st.write("Balance Sheet for Year ", Year_n)  
    st.write(" ")
    st.write(f"Assets: ${financials['assets']:.2f}")
    st.write(f"Liabilities: ${financials['liabilities']:.2f}")
    st.write(f"Equity: ${financials['equity']:.2f}")
    st.write(" ")


# Function to display Cash Flow Statement
def Cash_Flow_Year(financials): 
    st.write(" ")    
    st.subheader("Cash Flow Statement")
    st.write("Cash Flow Statement for Year ", Year_n)
    st.write(" ")
    st.write(f"Operating Cash Flow: ${financials['cash_flow_operating']:.2f}")
    st.write(f"Investing Cash Flow: ${financials['cash_flow_investing']:.2f}")
    st.write(f"Financing Cash Flow: ${financials['cash_flow_financing']:.2f}")
    st.write(f"Net Cash Flow: ${financials['net_cash_flow']:.2f}")
    st.write(" ")



# Function to display performance metrics
def performance_metrics_screen(assumptions, *operations_data):
    st.write(" ")
    st.header("Performance Metrics")
    st.write("Metrics calculated and displayed here are based upon all of the input data.")
    st.write(" ")

    # Aggregate all operational data for each year
    all_operational_data = [data for data in operations_data]

    # Initialize the financials storage
    all_financials = {}

    # Loop through each year's operational data
    for year, data in enumerate(all_operational_data, start=1):
        financials = calculate_financials(year, assumptions, data)
        all_financials[year] = financials
    
    # Create a DataFrame from the financials
    df_financials = pd.DataFrame(all_financials).T
    
    st.write("Financial Data Year 1-10:", df_financials)
    
    # Calculate metrics over 10 years
    st.write("Metrics at Fund Exit end of Year 10")
    st.write(" ")
    
    total_revenue_10 = df_financials["total_revenue"].sum()
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
    st.write(f"Total Capital Supplied by Investors over 10 years: ${total_capital_supplied_10:.2f}")

    # Calculate IRR and ROI
    irr = ((total_net_profit_10 / total_capital_supplied_10) ** (1 / 10)) - 1
    roi = (total_net_profit_10 / total_capital_supplied_10) * 100

    st.write(f"Internal Rate of Return (IRR) over 10 years: {irr:.2%}")
    st.write(f"Return on Investment (ROI) over 10 years: {roi:.2f}%")

    # Visualization
    years = list(all_financials.keys())
    net_revenue = df_financials["total_revenue"].tolist()
    aircraft_sold = [data[3] for data in all_operational_data]  # Assuming aircraft sold is the 4th item in operations_data
    operating_expenses = [data[8] for data in all_operational_data] # Assuming operating expenses is the 8th item in operations_data
    
    plot_net_revenue(years, net_revenue)
    plot_aircraft_sold(years, aircraft_sold)
    plot_facility_expenses(years, operating_expenses)



# Function to plot Net Revenue versus time
def plot_net_revenue(years, net_revenue):
    plt.figure(figsize=(10, 6))

    # Plot Net Revenue
    plt.plot(years, net_revenue, marker='o', linestyle='-', color='blue', label='Net Revenue')

    # Adding titles and labels
    plt.title('Net Revenue over 10 Years')
    plt.xlabel('Years')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)

    # Show the plot using Streamlit
    st.pyplot(plt)



# Function to plot aircraft sales target variation with time
def plot_aircraft_sold(years, aircraft_sold):
    plt.figure(figsize=(10, 6))

    # Plot Aircraft Sold
    plt.plot(years, aircraft_sold, marker='o', linestyle='--', color='orange', label='Aircraft Sold')

    # Adding titles and labels
    plt.title('Aircraft Sold over 10 Year period')
    plt.xlabel('Years')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)

    # Show the plot using Streamlit
    st.pyplot(plt)



# Function to plot MRO/FBO/Dealership Expenses versus time
def plot_facility_expenses(years, operating_expenses):
    plt.figure(figsize=(10, 6))

    # Plot Facility Expenses
    plt.plot(years, operating_expenses, marker='*', linestyle='-', color='red', label='Facility Expenses')

    # Adding titles and labels
    plt.title('Facility Expenses over 10 Years')
    plt.xlabel('Years')
    plt.ylabel('Values')
    plt.legend()
    plt.grid(True)

    # Show the plot using Streamlit
    st.pyplot(plt)
                                   

# Home screen function
def home_screen():
    st.image("IconA5-ExportModel.JPG", caption="The perfect Aerial Adventure Experience vehicle", use_column_width=True)
    st.title("CLAEOR Tool")
    st.write("""
        Welcome to the CLAEOR Tool. This application allows you to input and save assumptions and operational data 
        for a General Aviation business venture, comprised of a Luxury style FBO, a MRO and an aircraft Dealership, all part of a combined facility for which franchises are to be established, in order to deliver services directly to numerious regional locations. You can then view the financial statements and performance metrics based on the provided 
        data. Use the sidebar to navigate through different sections of the tool. It is recommended that you select and review the "Instructions" menu option prior to using the App.
    """)

# Instructions function
def instructions_screen():
    st.title("Instructions")
    st.write("""
        To execute this App's functions, mobile users will notice an arrow (greater than equal character) at the top left hand corner of the screen when the device is being held in portrait mode.
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

menu = st.sidebar.selectbox("Navigation", ["Home", "Instructions", "Assumptions", "Operations - Year 1", "Operations - Year 2", "Operations - Year 3", "Operations - Year 4", "Operations - Year 5", "Operations - Year 6", "Operations - Year 7", "Operations - Year 8", "Operations - Year 9", "Operations - Year 10", "Financial Statements", "Performance Metrics"])

# Access the session state variables
assumptions = st.session_state["assumptions"]
operations_data_1 = st.session_state["operations_data_1"]
operations_data_2 = st.session_state["operations_data_2"]
operations_data_3 = st.session_state["operations_data_3"]
operations_data_4 = st.session_state["operations_data_4"]
operations_data_5 = st.session_state["operations_data_5"]
operations_data_6 = st.session_state["operations_data_6"]
operations_data_7 = st.session_state["operations_data_7"]
operations_data_8 = st.session_state["operations_data_8"]
operations_data_9 = st.session_state["operations_data_9"]
operations_data_10 = st.session_state["operations_data_10"]

if menu == "Home":
    home_screen()
elif menu == "Instructions":
    instructions_screen()
elif menu == "Assumptions":
    assumptions_screen()
elif menu == "Operations - Year 1":
    operations_screen_1()
elif menu == "Operations - Year 2":
    operations_screen_2()
elif menu == "Operations - Year 3":
    operations_screen_3()
elif menu == "Operations - Year 4":
    operations_screen_4()
elif menu == "Operations - Year 5":
    operations_screen_5()
elif menu == "Operations - Year 6":
    operations_screen_6()
elif menu == "Operations - Year 7":
    operations_screen_7()
elif menu == "Operations - Year 8":
    operations_screen_8()
elif menu == "Operations - Year 9":
    operations_screen_9()
elif menu == "Operations - Year 10":
    operations_screen_10()
elif menu == "Financial Statements":    
    Year_n = st.sidebar.selectbox("Financial Statement Year ", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    if Year_n == "1":
        operations_data = operations_data_1
    if Year_n == "2":
        operations_data = operations_data_2
    if Year_n == "3":
        operations_data = operations_data_3
    if Year_n == "4":
        operations_data = operations_data_4
    if Year_n == "5":
        operations_data = operations_data_5
    if Year_n == "6":
        operations_data = operations_data_6
    if Year_n == "7":
        operations_data = operations_data_7
    if Year_n == "8":
        operations_data = operations_data_8
    if Year_n == "9":
        operations_data = operations_data_9
    if Year_n == "10":
        operations_data = operations_data_10
    financial_statements_screen(Year_n, assumptions, operations_data)
elif menu == "Performance Metrics":
    performance_metrics_screen(assumptions, operations_data_1, operations_data_2, operations_data_3, operations_data_4, operations_data_5, operations_data_6, operations_data_7, operations_data_8, operations_data_9, operations_data_10)

