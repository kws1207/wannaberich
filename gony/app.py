import streamlit as st
import pandas as pd
import pandas_datareader as pdr
from datetime import *
import FinanceDataReader as fdr

st.write("""# 부자가 되고싶니~?

""")

markets = ['S&P500', 'NYSE', 'NASDAQ', 'KOSPI', 'KOSDAQ', 'AMEX']

terms = {
    '1개월': timedelta(days=-30),
    '3개월': timedelta(days=-91),
    '6개월': timedelta(days=-182),
    '1년': timedelta(days=-365),
    '2년': timedelta(days=-730),
    '5년': timedelta(days=-1461),
    '10년': timedelta(days=-3652)
}

st.sidebar.header('아수라발발타...')

market = st.sidebar.selectbox('시장을 골라보렴', markets)

stocks_df = fdr.StockListing(market)
stocks_df = stocks_df[['Name', 'Symbol']]

# stocks_df = pd.DataFrame.from_dict(stocks, orient='index')
stocks = stocks_df.to_dict()
stocks_list = stocks_df['Name'].tolist()

stock = st.sidebar.selectbox('종목을 골라보렴', stocks_list)


term = st.sidebar.selectbox('기간을 골라보렴', list(terms.keys()))

df = pdr.get_data_yahoo(stocks_df.iloc[stocks_list.index(stock)].loc['Symbol'],
                        datetime.today() + terms[term], datetime.today())

st.line_chart(df.Close)
st.line_chart(df.Volume)
