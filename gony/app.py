import streamlit as st
import pandas as pd
import pandas_datareader as pdr
from datetime import *

stocks_df = pd.read_html(
    'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
stocks_df.종목코드 = stocks_df.종목코드.map('{:06d}'.format)
stocks_df = stocks_df[['회사명', '종목코드']]  # 한글로된 컬럼명을 영어로 바꿔준다
stocks_df = stocks_df.rename(columns={'회사명': 'name', '종목코드': 'code'})

# stocks_df = pd.DataFrame.from_dict(stocks, orient='index')
stocks = stocks_df.to_dict()
stocks_list = stocks_df['name'].tolist()

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
stock = st.sidebar.selectbox('Stocks', stocks_list)

term = st.sidebar.selectbox('Terms', list(terms.keys()))

df = pdr.get_data_yahoo(stocks_df.iloc[stocks_list.index(stock)].loc['code'] + '.KS',
                        datetime.today() + terms[term], datetime.today())

st.line_chart(df.Close)
st.line_chart(df.Volume)
