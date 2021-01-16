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
            # ylabel='가격(달러)',
            # ylabel_lower='거래량'
            )

        # 여백 자르기
        img = Image.open(file_name1)
        croppedImg = img.crop((200,200,4000,2300))
        croppedImg.save(file_name1)

        gcpUpload(file_name1=file_name1)

    return [file_name1, file_name2]


# 이미지 저장 -> GCP storage에 업로드
def gcpUpload(file_name1):
    #    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "src/main/resources/keystore/exalted-arcanum-356907-6273c406bf43.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/tweetpantry/stocksafe_test/key/exalted-arcanum-356907-6273c406bf43.json"

    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())

    print(buckets)

    # ----------------------------------------------------------
    print(file_name1)

    bucket_name = 'stocksafe_storage'    # 서비스 계정 생성한 bucket 이름 입력
    source_file_name = file_name1    # GCP에 업로드할 파일 절대경로
    destination_blob_name = file_name1    # 업로드할 파일을 GCP에 저장할 때의 이름

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('success')
    print('----end. -->' + str(time.time() - globalStartTime) + "----")


def noThread():
    global globalStartTime
    globalStartTime = time.time()
    startTime = time.time()

    print('----start.----')

    stock_list = readStockList()

    #print('----read stock list success.----')
    print(stock_list)

    img_file = predict(stock_list)

    #print('----predict success. image saved.----')

    # gcpUpload(img_file[0])

   # print('----gcp storage upload success.----')

    print('----end. -->' + str(time.time() - startTime) + "----")


# 단순히 입력을 나눠서 여러 개 동시에 실행하는 방법.
# 멀티 스레드지만 동시 처리랑 다를게 없다.
def multiThread():
    global globalStartTime
    globalStartTime = time.time()

    print('----start.----')

    list1 = readStockList()
    print(list1)

    thread_cnt = 2
    part_size = int( len(list1) / thread_cnt )
    for i in range(0, thread_cnt):  # 
        start = i*part_size
        print(start, thread_cnt, part_size)
        list1_slice=[]
        if i != thread_cnt-1:
            list1_slice = list1[start:start+part_size]
        else:
            list1_slice = list1[start:]
        print(list1_slice)
        my_thread = threading.Thread(target=predict, args=(list1_slice,))
        my_thread.start()
    

    # print('----end. -->' + str(time.time() - startTime) + "----")


if __name__ == '__main__':
    # noThread()
    multiThread()
