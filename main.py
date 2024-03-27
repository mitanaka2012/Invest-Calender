import investpy
import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import json

# 現在の日付を取得
today = datetime.date.today()
# 開始日と終了日を設定
start = "{0:%d/%m/%Y}".format(today + relativedelta(days=-7))
end = "{0:%d/%m/%Y}".format(today + relativedelta(days=+8))

# investpyを使って経済カレンダーのデータを取得
important = investpy.news.economic_calendar(from_date=start, to_date=end)

# 'id', 'currency' カラムをドロップ
important.drop(['id', 'currency'], axis=1, inplace=True)
# 'time'カラムで"All Day"を除外
important = important[important['time'] != 'All Day']
# 'date'カラムの形式を変更
important['date'] = pd.to_datetime(important['date'], format='%d/%m/%Y').dt.strftime('%m/%d')
# 'zone'カラムの値を変更
important['zone'] = important['zone'].replace({'japan': 'JPY', 'united states': 'USA'})

# Streamlitを使ってデータを表示
st.write("経済カレンダー", important)
