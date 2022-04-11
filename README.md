## AI_Project
## MultiLingual Undesired Speech Detection
- This is a Natural Language Processing project which detects hate speech on Online forums. This project uses Support Vector Machine(SVM) for the classiification of the hate speech.
- This model can be used by any online forums and discussions websites so that a clean and disciplined environment can be maintained.

## Features
- Easy to use GUI
- Supports multi language
- Uses machine learning for detection
- Cross platform

# Technologies Used
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![Numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)]()
[![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)]()
[![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)]()
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)]()


# Dataset
The Dataset for the model development contains more than 50k comments lablelled as fine or toxic. This is same for both english and hindi language. We had to clean the data to remove the special characters and include padding to maintain a certain length. Then Using the nltk library we used countVectorizer for the vectorization of our text data. Further using the data we trained the SVM model.

# Machine Learning Model
Support Vector Machine(SVM) is a supervised machine Learning algorithm used for classification problems. SVM is also called as large margin classifiers. The objective of SVM algorithm is to find a hyperplane in an N-dimensional space that distinctly classifies the data points. The dimension of the hyperplane depends upon the number of features. If the number of input features is two, then the hyperplane is just a line. If the number of input features is three, then the hyperplane becomes a 2-D plane. It becomes difficult to imagine when the number of features exceeds three.

# Idea Behind
The Basic Thought behind this project was to develop something which is very easy to use and easy to develop as well, cause as students we have some financial as well as time constraints if we are taking up any project. So we used one of the best classification algorithm SVM for the job and the results were highly satisfactory. After successful development of the algorithm came the GUI so we selected streamlit which is currently the favourite GUI tool for the job. 

## Authors 
- [@Unnati Mishra](https://github.com/unnati-m)
- [@Shweta Rajan](https://github.com/Shweta2762)
- [@Bezawada Sai Satwika](https://github.com/bvssatwika)
