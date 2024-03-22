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

st.set_page_config(page_title="Loan application Scoring",page_icon=":bank:",
                   layout="wide",initial_sidebar_state='expanded')

title=st.markdown("# :rainbow[ScoreMate]")


st.header("About ScoreMate")

st.info('''Introducing our innovative front-end web application designed for loan application 
         scorecards powered by machine learning. Our application streamlines the lending process 
         by leveraging advanced algorithms to accurately assess applicant risk profiles. 
         With intuitive user interfaces and real-time decision-making capabilities, financial institutions can expedite 
         loan approvals while minimizing risk exposure. This solution not only enhances operational efficiency 
         but also ensures fair and transparent lending practices. 
         Experience the future of lending assessment with our cutting-edge platform, 
         revolutionizing how loans are processed and approved
         ''')

st.subheader("Once File upload is sucessfull Genrate the score here")

st.sidebar.subheader("This application used for genrating Loan applcation Score")

def main():
    data=st.sidebar.file_uploader("Upload the CSV/Excel file with all the data to Genrate the score")
    

    if data is not None:
        file_extention=data.name.split(".")[-1].lower()

        if file_extention == "csv":
            data1=pd.read_csv(data)
        elif file_extention in ["xls","xlsx"]:
            data1=pd.read_excel(data)
            
        else:
            st.write("Error:Unsupported file format")
            data1=None
        st.sidebar.success('File uploaded sucessfully Now you can genrate the score')    

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

    
    
    