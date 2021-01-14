# 필요 모듈...?매번 받는건 아닌것같은데
import pymysql
import os
from google.cloud import storage
import threading
import time

import FinanceDataReader as fdr
from prophet import Prophet
import pandas as pd
import mplfinance as mpf

from PIL import Image

TRADING_PERIODS = 1000
PROPHET_PERIODS = 365

def readStockList():
    # DB에서 주식코드 받아오기
    # DB연결
    connect = pymysql.connect(host='localhost', user='root', password='ssafy',
                              db='stocksafe_db', charset='utf8')  # 한글처리 (charset = 'utf8')
    cur = connect.cursor()
    sql = "select id from stock"
    cur.execute(sql)
    list1 = cur.fetchall()

    return list1


def predict(list1):
    #list1 = list1[:4]
    for stock in list1:
        # 데이터 가져오기
        STOCK_CODE = stock[0]
        data = fdr.DataReader(STOCK_CODE)

        # prophet사용 위한 전처리
        # 반드시 y 컬럼과 ds 컬럼이 존재해야합니다.
        # 예측 값은 y, 시계열 데이터는 ds에 지정합니다.
        data['y'] = data['Close']
        data['ds'] = data.index

        # prophet사용
        # 객체 선언
        m = Prophet()
        m.fit(data)

        # 기간 설정
        future = m.make_future_dataframe(