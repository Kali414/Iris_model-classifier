import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

model=joblib.load('iris_model.joblib')


from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

target=np.array(load_iris().target_names)
st.title('Flower classification')


#   'sepal length (cm)',
#   'sepal width (cm)',
#   'petal length (cm)',
#   'petal width (cm)'
#    st.write(target[0])


sepal_length = st.sidebar.slider(
    "Enter Sepal Length (cm)",
    min_value=float(0),
    max_value=float(iris_df['sepal length (cm)'].max()),
    value=float(iris_df['sepal length (cm)'].min())
)

sepal_width=st.sidebar.slider(
    "Enter Sepal Width (cm)",
    max_value=float(iris_df['sepal width (cm)'].max()),
    min_value=float(0),
    value=float(iris_df['sepal width (cm)'].mean())
)

petal_length=st.sidebar.slider(
    "Enter Petal Length (cm)",
    max_value=float(iris_df['petal length (cm)'].max()),
    min_value=float(0),
    value=float(iris_df['petal length (cm)'].mean())
)

petal_width=st.sidebar.slider(
    "Enter Petal Width (cm)",
    max_value=float(iris_df['petal width (cm)'].max()),
    min_value=float(0),
    value=float(iris_df['petal width (cm)'].mean())
)

features=[[sepal_length,sepal_width,petal_length,petal_width]]

prediction=model.predict(features)

predicted_species=target[prediction[0]]

st.markdown('The predicted species:')

st.write(predicted_species.title())
image_path=f"images/{predicted_species}.jpeg"
if(os.path.exists(image_path)):
    st.image(image_path)

else:
    st.write("Image not found")