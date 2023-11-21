import numpy as np
import pandas as pd
import streamlit as st
import pickle
import nltk
import string


# Function for preproccing of the data
def preprocess(s):
    s = s.lower()
    s = pd.Series(nltk.word_tokenize(s))
    s = s.unique()
    y = []
    for i in s:
        if not(i.isnumeric()) and i not in string.punctuation:
            y.append(i)

    s = " ".join(y)
    y.clear()
    return s

# Function for predicting
def prediction(s):
    s = preprocess(s)
    p = model.predict([s])
    return p[0]

# Key-Value Pairs for Languages
lang_dict = {
    'English'   : 0, 
    'French'    : 1, 
    'Spanish'   : 2, 
    'Portugeese': 3, 
    'Italian'   : 4, 
    'Russian'   : 5,
    'Sweedish'  : 6, 
    'Malayalam' : 7, 
    'Dutch'     : 8, 
    'Arabic'    : 9, 
    'Turkish'   : 10, 
    'German'    : 11,
    'Tamil'     : 12, 
    'Danish'    : 13, 
    'Kannada'   : 14, 
    'Greek'     : 15
}

# Function to get Language for key
def get_key(val):
    for key, value in lang_dict.items():
        if val == value:
            return key
 
# loading the model we have trained
model = pickle.load(open('langpredict.pkl', 'rb'))


# Bulding the web app on streamlit 

st.header("Language Predicter",divider='blue')

text = st.text_area("Enter the Text : ")

if st.button("Predict",type="primary"):
    a = prediction(text)
    st.subheader(get_key(a))

    with open("input.txt",'a',encoding="utf-8") as f:
        f.write(f'"{text}",{get_key(a)}\n')
    


