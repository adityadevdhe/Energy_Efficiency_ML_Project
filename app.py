import streamlit as st
import pickle
pickle_in= open("energy.pkl",'rb')
model=pickle.load(pickle_in)
import pandas as pd

def user_input():
    X1=st.slider("Relative Compactness",0.7,1.0,0.7)
    X2=st.slider("Surface Area",635,710,686)
    X3=st.slider("Wall Area",315,350,318)
    X4=st.slider("Roof Area",110,220,220)
    X5=st.slider("Overall Height",3.5,7.0,7.0)
    X6=st.slider("Orientation",2.0,5.0,4.0)
    X7=st.slider("Glazing Area",0.20,0.30,0.23)
    X8=st.slider("Glazing Area Distribution",1.0,4.0,3.0)
    data={
        'X1':X1,
        'X2':X2,
        'X3':X3,
        'X4':X4,
        'X5':X5,
        'X6':X6,
        'X7':X7,
        'X8':X8

    }
    features=pd.DataFrame(data,index=[0])
    return features

def main():
    st.write("""
     # Energy Prediction App
"""
    )
    st.header("User Input Parameters")
    df=user_input()
    prediction=model.predict(df)
    st.write("Result")
    st.write(prediction)

if __name__=='__main__':
    main()
    