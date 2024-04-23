import streamlit as st
import joblib


st.markdown(
    """
    <style>
    .main {
        background-color: #000033;
        color: white;
    }

    .stLabel, .stTextInput>div>div>div>input, .stTextInput>div>div>label, .st-emotion-cache-ue6h4q {
        color: white !important;
    }
    

    .st-emotion-cache-1umgz6k{
        background-color: rgb(49 49 194);
    }
    </style>
    """,
    unsafe_allow_html=True
)

#pickle_in = open("random_forest.pkl","rb")
random_forest = joblib.load('random_forest1.pkl')

# st.title("Stress Level Detection")
html_temp = """
    <div>
    <h2 style="color:white;text-align:center;"><img src ="https://cdn-icons-png.flaticon.com/512/2755/2755341.png" width="50" height="50" style="margin-right: 10px;">Stress Level Detection App </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
gender_options = ['Select Gender','Male', 'Female']
Gender = st.selectbox('Gender', gender_options, index=0)

Age = st.text_input("Age", placeholder="Type Here", key="age")

occupation_options = ['Select Occupation', 'Scientist', 'Doctor', 'Accountant', 'Teacher', 'Manager', 'Engineer', 'Sales Representative', 'Lawyer', 'Salesperson', 'Software Engineer', 'Nurse']
Occupation = st.selectbox('Occupation', occupation_options, index=0)


Sleep_Duration = st.text_input("Sleep Duration", placeholder="Type Here")

bmi_category_options = ['Select BMI Category', 'Underweight', 'Normal' ,'Overweight']
BMI_Category = st.selectbox('BMI Category', bmi_category_options, index=0)

Heart_Rate = st.text_input("Heart Rate", placeholder="Type Here")
Daily_Steps = st.text_input("Daliy Steps", placeholder="Type Here")
Systolic_BP = st.text_input("Systolic BP", placeholder="Type Here")

# Preprocessing the user inputs
Gender = 1 if Gender == 'Male' else 0
Occupation = occupation_options.index(Occupation) - 1
BMI_Category = bmi_category_options.index(BMI_Category) - 1


user_inputs = [[
    Gender,
    int(Age) if Age else 0,  # Use 0 if Age is an empty string
    Occupation,
    float(Sleep_Duration) if Sleep_Duration else 0,  # Use 0 if Sleep_Duration is an empty string
    BMI_Category,
    int(Heart_Rate) if Heart_Rate else 0,  # Use 0 if Heart_Rate is an empty string
    int(Daily_Steps) if Daily_Steps else 0,  # Use 0 if Daily_Steps is an empty string
    int(Systolic_BP) if Systolic_BP else 0  # Use 0 if Systolic_BP is an empty string
]]
# if st.button("Predict"):
#     result = random_forest.predict(user_inputs)

#     st.write(f"Predicted stress level: {result[0]}")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Predict", key="predict_button", use_container_width=True):
        result = random_forest.predict(user_inputs)
        # Center-align and bold the predicted stress level
        html_result = f"""
        <div style="text-align:center;">
            <p style="font-weight:bold;">Predicted stress level: {result[0]}</p>
        </div>
        """
        st.markdown(html_result, unsafe_allow_html=True)
    
