import streamlit as st

# Function for length conversion
def length_converter(value, from_unit, to_unit):
    length_units = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254,
    }
    
    # Convert to meters first
    meters = value * length_units[from_unit]
    # Convert from meters to the target unit
    return meters / length_units[to_unit]

# Function for weight conversion
def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'grams': 1.0,
        'kilograms': 1000.0,
        'pounds': 453.592,
        'ounces': 28.3495,
    }

    # Convert to grams first
    grams = value * weight_units[from_unit]
    # Convert from grams to the target unit
    return grams / weight_units[to_unit]

# Function for temperature conversion
def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return value * 9/5 + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value # same unit

# Streamlit app layout
st.title("Unit Converter App")

# Length conversion
st.header("Length Converter")
length_value = st.number_input("Enter length value:", value=0.0)
length_from_unit = st.selectbox("From unit:", options=['meters', 'kilometers', 'miles', 'feet', 'inches'])
length_to_unit = st.selectbox("To unit:", options=['meters', 'kilometers', 'miles', 'feet', 'inches'])

if st.button("Convert Length"):
    length_result = length_converter(length_value, length_from_unit, length_to_unit)
    st.write(f"{length_value} {length_from_unit} is {length_result} {length_to_unit}")

# Weight conversion
st.header("Weight Converter")
weight_value = st.number_input("Enter weight value:", value=0.0)
weight_from_unit = st.selectbox("From unit:", options=['grams', 'kilograms', 'pounds', 'ounces'])
weight_to_unit = st.selectbox("To unit:", options=['grams', 'kilograms', 'pounds', 'ounces'])

if st.button("Convert Weight"):
    weight_result = weight_converter(weight_value, weight_from_unit, weight_to_unit)
    st.write(f"{weight_value} {weight_from_unit} is {weight_result} {weight_to_unit}")

# Temperature conversion
st.header("Temperature Converter")
temperature_value = st.number_input("Enter temperature value:", value=0.0)
temperature_from_unit = st.selectbox("From unit:", options=['Celsius', 'Fahrenheit', 'Kelvin'])
temperature_to_unit = st.selectbox("To unit:", options=['Celsius', 'Fahrenheit', 'Kelvin'])

if st.button("Convert Temperature"):
    temperature_result = temperature_converter(temperature_value, temperature_from_unit, temperature_to_unit)
    st.write(f"{temperature_value} {temperature_from_unit} is {temperature_result} {temperature_to_unit}")
