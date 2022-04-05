# AI_Project
# Undesired Speech Detection
This is a Natural Language Processing project which detects hate speech on Online forums. This project uses Support Vector Machine(SVM) for the classiification of the hate speech.
This model can be used by any online forums and discussions websites so that a clean and disciplined environment can be maintained.

# Features
Easy to use GUI
Supports multi language
Uses machine learning for detection
Cross platform

# Dataset
The Dataset for the model development contains more than 50k comments lablelled as fine or toxic. This is same for both english and hindi language. We had to clean the data to remove the special characters and include padding to maintain a certain length. Then Using the nltk library we used countVectorizer for the vectorization of our text data. Further using the data we trained the SVM model.

# Idea Behind
The Basic Thought behind this project was to develop something which is very easy to use and easy to develop as well, cause as students we have some financial as well as time constraints if we are taking up any project. So we used one of the best classification algorithm SVM for the job and the results were highly satisfactory. After successful development of the algorithm came the GUI so we selected streamlit which is currently the favourite GUI tool for the job. 
