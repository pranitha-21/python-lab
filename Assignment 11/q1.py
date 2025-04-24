import numpy as np
import pandas as pd
import datetime

date_time_a=pd.to_datetime('Jan 15 2012')
print("Date time object for jan 15 2012:")
print(date_time_a)
print(type(date_time_a))


date_time_b=pd.to_datetime('2025-04-07 21:20:00')
print("specific date and time of 9:20 pm:")
print(date_time_b)
print(type(date_time_b))

local_date_time_c=pd.to_datetime('now')
print("local date and time :")
print(local_date_time_c)
print(type(local_date_time_c))

date_only_d=pd.to_datetime('now').date()
print("a date without time:")
print(date_only_d)
print(type(date_only_d))

current_date_e=pd.to_datetime('today').date()
print("current date:")
print(current_date_e)
print(type(current_date_e))

given_date_time=pd.to_datetime('2023-10-26 14:33:45')
time_from_date_f=given_date_time.time()
print("time from date :")
print(time_from_date_f)
print(type(time_from_date_f))

current_local_time_g=pd.to_datetime('now').time()
print("current local time:")
print(current_local_time_g)
print(type(current_local_time_g))
