import os
import streamlit as st
import numpy as np
from PIL import  Image
import pandas as pd
from utils.cassandra_helper import CassandraHelper
# Custom imports 
from multipage import MultiPage
from pages import addnewProject,dashboard,eda,datapreprocessing,featureengineering
import time

@st.cache
def load_data():
    try:
        # query_params = st.experimental_get_query_params()
        # project_name="new_table"
        
        # if query_params and query_params["project"][0]:
        #     project_name=query_params["project"][0]
        
        # if project_name:
        #     cassandra=CassandraHelper()
        #     df=cassandra.retrive_dataset(project_name)
        df=pd.read_csv('data/train.csv')
        lowercase = lambda x: str(x).lower()
        df.rename(lowercase, axis='columns', inplace=True)
        # if 'data' not in st.session_state:
        #     st.session_state['data'] = df
        return df
        
    except Exception as e:
        print(e)
    finally:
        pass



