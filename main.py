import streamlit as st
import yfinance as yf
import datetime

# This is for title
st.title('Welcome to Stock Price Analyser.')


col1, col2, col3 = st.columns(3)

with col1:
    input_ticker = st.text_input("Please select the stock (ticker).",'MSFT')
    ticker_data = yf.Ticker(input_ticker)

with col2:
    start_date = st.date_input("Please input the start date",datetime.date(2019,1,1))

with col3:
    end_date = st.date_input("Please input the start date",datetime.date(2025,1,25))

ticker_df = ticker_data.history(period = '1d', start=start_date, end=end_date)

# this is for dataframe

st.dataframe(ticker_df.head())
st.divider()

# this is for line chart
st.subheader("Plot the Metric")

metric = st.selectbox("What would you like to search.", ['Open','High','Low','Close','Volume'])


# ticker_df = ticker_data.history(period = '1d', start=start_date, end=end_date)

st.line_chart(ticker_df[metric])

