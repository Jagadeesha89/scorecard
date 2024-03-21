import pandas as pd
import numpy as np
import streamlit as st
from optbinning import OptimalBinning,scorecard,BinningProcess
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.pipeline import Pipeline
import pickle

score_card=pickle.load(open('scorecard.pkl','rb'))

def predit_score(data):
    predict=score_card.score(data)
    return predict

st.set_page_config(page_title="Loan application Scoring")
title=st.title("ScoreMe")

def main():
    data=st.file_uploader("Choose only CSV/Excel file")

    if data is not None:
        file_extention=data.name.split(".")[-1].lower()

        if file_extention == "csv":
            data1=pd.read_csv(data)
        elif file_extention in ["xls","xlsx"]:
            data1=pd.read_excel(data)
        else:
            st.write("Error:Unsupported file format")
            data1=None

        if data1 is not None and not data1.empty:
            ok=st.button("Genrate Score")

            if ok:
                score=predit_score(data1)
                with st.spinner("Genrating score...."):
                    st.success('Score genrated sucessfully')
                data1['Score']=score
                csv = data1.to_csv(index=False).encode('utf-8')  # Convert DataFrame to CSV string
                st.download_button("Download your data", csv, file_name="Score_updated_file.csv", mime='text/csv')

if __name__=='__main__':
    main()

    
    
    