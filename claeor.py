
import streamlit as st
import math

# Initialize session state variables for assumptions and operations data if they don't exist
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

# Function to display and save operations data
def operations_data_screen():
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
    
    for i in range(1,91):
        for j in range(i,i+10):
            Year_n = st.session_state["operations_data"][j]
            st.subheader(f"{Ops_labels[0]} {Year_n}")
            j=j+1
            Target_Rental_hrs = st.session_state["operations_data"][j]
            st.session_state["operations_data"][j] = st.number_input(Ops_labels, value={Target_hours})
            j=j+1
            Size_of_fleet = st.session_state["operations_data"][j]
            st.session_state["operations_data"][j] = st.number_input(Ops_labels, value=Size_of_fleet)
            j=j+1
            Number_of_aircraft_sold = st.session_state["operations_data"][j]
            st.session_state["operations_data"][j] = st.number_input(Ops_labels, value={Number_of_aircraft_sold})
            j=j+1
            Gross_Margin = st.session_state["operations_data"][j]
            st.session_state["operations_data"][j] = st.number_input(Ops_labels, value={Gross_Margin})
            j=j+1
            Debt_to_Equity_ratio = st.session_state["operations_data"][j]
            st.session_state["operations_data"][j] = st.number_input(Ops_labels, value={Debt_to_Equity_ratio})
            j=j+1
            MRO_services_Revenue = st.session_state["operations_data"][j]
            st.session_state["operations_data"][j] = st.number_input(Ops_labels, value={MRO_services_Revenue})
            j=j+1
            Partnership_Revenue = st.session_state["operations_data"][j]
            st.session_state["operations_data"][j] = st.number_input(Ops_labels, value={Partnership_Revenue})
            j=j+1
            Operating_Expenses = st.session_state["operations_data"][j]
            st.session_state["operations_data"][j] = st.number_input(Ops_labels, value={Operating_Expenses})
            j=j+1
            Investor_Capital_Calls = st.session_state["operations_data"][j]
            st.session_state["operations_data"][j] = st.number_input(Ops_labels, value={Investor_Capital_Calls})
        
        if st.button(f"Save year's input data"):
            st.success(f"Year's input data saved!")
            i=i+10


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
menu = st.sidebar.selectbox("Navigation", ["Home", "Instructions",  "Assumptions", "Operations Data", "Financial Statements", "Performance Metrics"])

if menu == "Home":
    home_screen()
elif menu == "Instructions":
    instructions_screen()
elif menu == "Assumptions":
    assumptions_screen()
elif menu == "Operations Data":
    operations_data_screen()
elif menu == "Financial Statements":
    financial_statements_screen()
elif menu == "Performance Metrics":
    performance_metrics_screen()

