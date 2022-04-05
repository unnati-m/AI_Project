import streamlit as st
import pickle
import regex

def custom_analyzer(text):
    words = regex.findall(r'\w{2,}', text) # extract words of at least 2 letters
    for w in words:
        yield w

st.sidebar.header('Language Select')
lang=st.sidebar.selectbox('Language',('Home','English','Hindi','Details'))

if(lang=='Home'):
    st.header('Multi-lingual Undesired Speech Detection')
    st.subheader('Welcome to the app')
    st.write('You may choose the language from the sidebar')
    st.image('logo.jpeg')

if(lang=='English'):
    model = pickle.load(open('final_model.pkl', 'rb'))
    vectorizer=pickle.load(open('tfidf.pkl','rb'))
    st.write('Please write your text below')
    input_english=st.text_input('')
    if(input!=''):
        text_en=vectorizer.transform([input_english])
        prediction_eng=model.predict(text_en)
        if(prediction_eng==1):
            st.write('Undesired Speech Detected')
        elif(prediction_eng==0):
            st.write('No Undesirable Text Found')


if(lang=='Hindi'):
    hindi_model=pickle.load(open('hindi_model.pkl','rb'))
    hindi_vectorizer=pickle.load(open('hindi_vectorizer.pkl','rb'))
    st.write('Please write your text below')
    input_hindi=st.text_input('')
    if(input!=''):
        text_hin=hindi_vectorizer.transform([input_hindi])
        prediction_hin=hindi_model.predict(text_hin)
        st.write('The Above language is '+prediction_hin)

if(lang=='Details'):
    expander_bar = st.expander("About")
    expander_bar.markdown("""
    * **Python libraries:** pandas, Numpy, streamlit, numpy, support Vector Machines, Pickle.
    * **Data source:** Various Online Data Repositories.
    """)
