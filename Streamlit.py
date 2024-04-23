{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6deac1fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pickle\n",
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "fe50cdcc",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-04-23 12:07:05.836 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Tanaya\\anaconda3\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pickle\n",
    "import streamlit as st\n",
    "\n",
    "pickle_in = open(\"random_forest.pkl\", \"rb\")\n",
    "random_forest = pickle.load(pickle_in)\n",
    "\n",
    "def welcome():\n",
    "    return \"Welcome All\"\n",
    "\n",
    "def predict_note_authentication(Gender, Age, Occupation, Sleep_Duration, BMI_Category, Heart_Rate, Daily_Steps, Systolic_BP):\n",
    "    # Concatenate the input variables into a list or array\n",
    "    features = [[Gender, Age, Occupation, Sleep_Duration, BMI_Category, Heart_Rate, Daily_Steps, Systolic_BP]]\n",
    "    # Make prediction\n",
    "    prediction = random_forest.predict(features)\n",
    "    return prediction\n",
    "\n",
    "def main():\n",
    "    st.title(\"Stress Level Detection\")\n",
    "    html_temp = \"\"\"\n",
    "    <div style=\"background-color:tomato;padding:10px\">\n",
    "    <h2 style=\"color:white;text-align:center;\">Streamlit Stress Level Detection ML App </h2>\n",
    "    </div>\n",
    "    \"\"\"\n",
    "    st.markdown(html_temp, unsafe_allow_html=True)\n",
    "    Gender = st.text_input(\"Gender\", \"Type Here\")\n",
    "    Age = st.text_input(\"Age\", \"Type Here\")\n",
    "    Occupation = st.text_input(\"Occupation\", \"Type Here\")\n",
    "    Sleep_Duration = st.text_input(\"Sleep Duration\", \"Type Here\")\n",
    "    BMI_Category = st.text_input(\"BMI Category\", \"Type Here\")\n",
    "    Heart_Rate = st.text_input(\"Heart Rate\", \"Type Here\")\n",
    "    Daily_Steps = st.text_input(\"Daily Steps\", \"Type Here\")\n",
    "    Systolic_BP = st.text_input(\"Systolic BP\", \"Type Here\") \n",
    "    result = \"\"\n",
    "    if st.button(\"Detect\"):\n",
    "        # Pass the input values to the prediction function\n",
    "        result = predict_note_authentication(Gender, Age, Occupation, Sleep_Duration, BMI_Category, Heart_Rate, Daily_Steps, Systolic_BP)\n",
    "        st.success('The output is {}'.format(result))\n",
    "\n",
    "    if st.button(\"About\"):\n",
    "        st.text(\"Let's Learn\")\n",
    "        st.text(\"Built with Streamlit\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
