#!/usr/bin/env python
# coding: utf-8

# In[1]:


#IMPORTING LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# In[2]:


def main():
    html_temp = """
    <div style="background-color:lightblue;padding:70px; opacity:0.8">
    <h2 style="color:black;font-style:italic;font-weight:700;text-align:center;">SEMI-AUTOMATED DATA ANALYSIS AND VISUALIZATION </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    activities = ["EDA","PLOT"]
    
    choice = st.sidebar.selectbox("SELECT ACTIVITY", activities)
    
    if choice == 'EDA':
        st.subheader("EXPLORATORY DATA ANALYSIS")
        #to upload file from your device
        data = st.file_uploader("UPLOAD DATASET", type=["csv", "txt"])
        
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())
            
        if st.checkbox("SHAPE OF DATASET"):
            st.write(df.shape)
            
        if st.checkbox("COLUMNS"):
            all_columns = df.columns.to_list()
            st.write(all_columns)
            
        if st.checkbox("SUMMARY"):
            st.write(df.describe())
            
        if st.checkbox("SHOW SELECTED COLUMNS"):
            selected_columns = st.multiselect("SELECT COLUMNS",all_columns)
            new_df = df[selected_columns]
            st.dataframe(new_df)
            
        if st.checkbox("VALUE COUNTS"):
            st.write(df.iloc[:,-1].value_counts())
            
        if st.checkbox("CORRELATION PLOT"):
            st.write(sns.heatmap(df.corr(),annot=True))
            st.pyplot()
            
    elif choice == 'PLOT':
        st.subheader("VISUALIZATION")
        data = st.file_uploader("UPLOAD DATASET", type=["csv", "txt"])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())


        if st.checkbox("VALUE COUNTS"):
            st.write(df.iloc[:,-1].value_counts().plot(kind='bar'))
            st.pyplot()



        all_columns_names = df.columns.tolist()
        type_of_plot = st.selectbox("SELECT PLOT TYPE",["area","bar","line","hist","box","kde"])
        selected_columns_names = st.multiselect("SELECT COLUMNS TO PLOT ",all_columns_names)

        if st.button("GENERATE PLOT"):
            st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))


        if type_of_plot == 'area':
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot == 'bar':
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == 'line':
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)
 
        elif type_of_plot:
            cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()
            
if __name__ == '__main__':
    main()
    


# In[ ]:




