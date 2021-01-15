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
        future = m.make_future_dataframe(periods=PROPHET_PERIODS)
        # 예측
        forecast = m.predict(future)

        
        ########################
        # 예측 데이터 시각화
        #경향 그래프 그리기
        # (Prophet 기능 사용, forecast데이터 자르기 전에 처리해야)
        ########################
        file_name = "prophet/img/" + STOCK_CODE + "_seasonality.png"
        m.plot_components(forecast).savefig(file_name)
                
        ########################
        # 예측 데이터 시각화
        # 실거래+예상치 데이터 그리기
        # 차트용으로 데이터 자르기
        ########################
        # 실거래데이터 자르기
        data = data[-TRADING_PERIODS:]

        # 예측치를 위한 실거래 데이터의 날짜가 더 길어야한다.
        dummy = data[-1:]
        tmp = forecast[-PROPHET_PERIODS:]
        for i in range(PROPHET_PERIODS) :
            dummy.index = tmp[i:i+1].ds
            dummy.Close = 0
            dummy.Open = 0
            dummy.High = 0
            dummy.Low = 0
            dummy.Volume = 0
            dummy.Change = 0
            dummy.y = 0
            dummy.ds = 0
            data = pd.concat([data,dummy])


        # 예측치 자르기
        forecast = forecast[(TRADING_PERIODS+PROPHET_PERIODS)*-1:]
        forecast_t = forecast['ds'].dt.to_pydatetime()


        # 차트 그리기(밑그림)
        index = data.index.astype('str') # 캔들스틱 x축이 str로 들어감

        # 예측선 그리기
        ap0 = [ mpf.make_addplot(forecast['yhat'],color='g',type='line') ]


        file_name1 = "prophet/img/" + STOCK_CODE + ".png"
        save = dict(fname=file_name1,dpi=300,pad_inches=1,bbox_inches="tight")
        mpf.plot(data,                # 차트에 채울 데이터(실거래가)
            addplot=ap0,         # 추가로 그릴 데이터(자체적으로 테마 등 지정 되어있음)
            volume=True,         # 거래량
            style='yahoo',       # 차트 테마(색,선, ...)
            type='candle',       # 그래프 타입 : 캔들스틱
            savefig=save,        # 이미지로 저장
            figratio=(20,10),     # 차트의 종횡비
            ylabel='Price($)',
            ylabel_lower='Volume',
            scale_padding=0
            # yl