import streamlit as st
import pandas_datareader as pdr
from datetime import *

stocks = {
    '애플': {'market': 'NASDAQ', 'code': 'AAPL'},
    '보잉': {'market': 'NYSE', 'code': 'BA'},
    '나이키': {'market': 'NYSE', 'code': 'NKE'}
}

terms = {
    '1개월': timedelta(days=-30),
    '3개월': timedelta(days=-91),
    '6개월': timedelta(days=-182),
    '1년': timedelta(days=-365),
    '2년': timedelta(days=-730),
    '5년': timedelta(days=-1461),
    '10년': timedelta(days=-3652)
}

st.write('# 부자가 되고싶니')

st.sidebar.header('Menu')
stock = st.sidebar.selectbox('Stocks', list(stocks.keys()))
print(stock)

term = st.sidebar.selectbox('Terms', list(terms.keys()))

df = pdr.get_data_yahoo(stocks[stock]['code'],
                        datetime.today() + terms[term], datetime.today())

st.line_chart(df.Close)
st.line_chart(df.Volume)
