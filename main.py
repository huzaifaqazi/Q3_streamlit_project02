import streamlit as st

# 1 meter = 0.001 kilometer
# 1 kilometre = 1000 meters
# 1gram = 0.001 kilogram
# 1kilogram = 1000 grams

def main(value,from_unit,to_unit):
    conversions = {
        "meter_kilometer":0.001,
        "kilometer_meter":1000,
        "gram_kilometer":0.001,
        "kilometer_gram":1000,
    }

    key = f"{from_unit}_{to_unit}"

    if key in conversions:
        conversions = conversions[key]
        return value*conversions
    else:
        return "conversion not possible"
    
st.title("Unit Converter")
value = st.number_input("Enter the value")

from_unit = st.selectbox("From unit",["meter","kilometer","gram","kilogram"])
to_unit = st.selectbox("To unit",["meter","kilometer","gram","kilogram"])

if st.button("Convert"):
    result = main(value,from_unit,to_unit)
    st.write(f"The Result {result}")