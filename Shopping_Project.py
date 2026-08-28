
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title = 'Ecommerce EDA',layout = 'wide')

st.markdown("<h1 style='text-align: center; color: black;'>Shopping analysis</h1>", unsafe_allow_html= True)

st.image('https://marketplace.canva.com/EAGkJu6RBag/1/0/1600w/canva-pink-and-white-minimalist-e-commerce-presentation-pUrMakjsI6U.jpg')

df = pd.read_csv('Cleaned_df.csv',index_col = 0)

# st.dataframe(df)

total_Revenue = df['total_price'].sum()

total_orders = df['sales_id'].nunique()

total_customers = df['customer_name'].nunique()

avg_order_value = df['total_price'].mean()

col1,col2,col3,col4 = st.columns(4)

with col1 :
    st.metric('Total Revenue',total_Revenue)

with col2 :
    st.metric('Total Orders',total_orders)

with col3 :
    st.metric('Total Customers',total_customers)

with col4 :
    st.metric('Average Order Value',avg_order_value)

df_sorted = df.sort_values(by= 'order_date')
plot_df = df_sorted.groupby('month')['total_price'].sum().reset_index()
st.plotly_chart(px.line(data_frame= plot_df, x= 'month', y= 'total_price',
        labels= {'month' : 'Month', 'total_price' : 'Total Revenue'},
        title= 'Total Revenue per month',
        text= 'total_price',
        line_shape= 'spline').update_traces(textposition= 'top center'))



df_sorted['cum_revenue'] = df_sorted['total_price'].cumsum()
st.plotly_chart(px.line(data_frame= df_sorted, x= 'order_date', y= 'cum_revenue'))


col1,col2 = st.columns(2)

with col1:
    st.plotly_chart(px.pie(data_frame= df, names= 'product_type'))


with col2 :
    plot_df = df.groupby(['state', 'product_type'])['delivery_days'].mean().round(2).reset_index()
    st.plotly_chart(px.bar(data_frame= plot_df, y= 'state', x= 'delivery_days',
       color= 'product_type',
       barmode= 'group',
       labels= {'delivery_days' : 'Average delivery days'},
       text_auto= True))
