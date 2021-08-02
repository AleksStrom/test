import streamlit as st

import numpy as np
import pandas as pd

st.title('Example HTML site')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# Brønn & Felt oversikt
st.write("Overview of wells present in the documents:")

map_data = pd.DataFrame(
    # np.random.randn(1, 2) / [40.59, 0.86] + [56.54, 3.4],
    #np.random.randn(1, 2) / [49.3, 48.7] + [71.36, 23.3],
    #np.array([[71.36493], [23.3387]]),
    [[71.3,23.3],[61.121344,2.162856]],
    columns=['lat', 'lon'])


to_append=[[66.1101,4.114279],[57.45202,4.22135]]
for i in to_append:
    la =pd.Series(i,index=map_data.columns)
    map_data= map_data.append(la,ignore_index=True)
# la =pd.Series(to_append,index=map_data.columns)
# map_data= map_data.append(la,ignore_index=True)
st.map(map_data)
if st.checkbox('Show MapData'):
    map_data
