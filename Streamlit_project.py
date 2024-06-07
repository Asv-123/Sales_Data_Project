import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
@st.cache_data
def load_data():
    data = pd.read_csv('storeSalesData.csv')
    return data

def display_chart(data):
    sales = data['Product_Category'].value_counts()

    labels = sales.index.tolist()

    sizes = sales.values.tolist()
    fig,ax = plt.subplots()
    ax.pie(sizes,labels = labels , autopct='%1.1f%%',startangle=90)
    ax.set_title('Sales Data Pie Chart')

    return fig


def main():
    st.set_page_config(page_title = 'Sales Report app',page_icon= ":Bar chart:")

    st.title('Sales Report App')

    data = load_data()
    st.write('## Sales Data')
    st.write(data.head())
    st.write('Sales data pie chart')
    pie = display_chart(data)
    st.pyplot(pie)


main()

