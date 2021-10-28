import streamlit as st

st.title("GUI for Machine Learning Model")

st.text("This is a sample user interface for the understanding of the GUI streamlit")
st.slider("Slide the bar",min_value=0,max_value=10)
st.file_uploader("Enter some value")
st.button("Hit me")

st.subheader("Please enter the number to add")
x = st.number_input("Enter the first number")
y = st.number_input("Enter the second number")
st.text("print the result")
st.checkbox("Please check the box if you are ready")



st.sidebar.selectbox("Select the option wanted",(1,2,3,4,5,6,7,8))


