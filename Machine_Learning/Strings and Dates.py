#Check for specific type of variable
df_texts = df.loc[:,df.dtypes == np.object]

# Ako contertovat series object na stringArray. 
df_texts.MSZoning.astype('string')

# Mozme convertovat aj cely df
df_texts.astype('string')

# vsimnite si NaN hodnoty. Nan hodnota je cislo ale string nie je cislo preto pandas pouzil takyto workaround aspon pre zatial.
type(df_texts.astype('string').loc[1,'Alley'])


# vzdy pouzijem .str pred samotnou metodou
df_texts.Neighborhood.str.lower().head()


# Praca s viareymi slovami
string_series=pd.Series([
    'Michal Hucko', 'Bratislava', 'Luis Felipe Melo Mora', ' medzeri ', ' enter\n', 'tab\t '])

# Alebo ked chcem pracovat priamo ako string
string_series_future=pd.Series([
    'Michal Hucko', 'Bratislava', 'Luis Felipe Melo Mora', ' medzeri ', ' enter\n', 'tab\t '], dtype='string')

string_series

#Delete all unnecessary symbols/characters
string_series.str.strip().values

# Str vieme pouzit aj nad nazvami stlpcov
df.columns.str.upper()

# str operacie vieme aj retazit 
df.columns.str.lower().str.replace('a', 'misko') # replace je nahradenie stringu stringom

#Split based on any character
string_series.str.split("_")

#if there is no _ character then the second part will be None 
string_series.str.split("_", expand=True)

# regex replace
string_series=pd.Series([
    'Hucko', 'Huckova', 'Hucko', "Jano", np.nan])
string_series.str.replace("Hucko.*", "hruska", regex=True)

# Concatenacia 
string_series=pd.Series([
    'Hucko', 'Huckova', 'Hucko', "Jano", np.nan])

string_series.str.cat(sep="_", na_rep="Misko") # na_rep nahradi nan hodnotu

string_series.str.cat(string_series2, na_rep="") #if there is NAN than it will not be NAN in column


# contains, if Hucko is in string -> returns bools
string_series=pd.Series([
    'Michal_Hucko', 'Katarína_Huckova', 'Andrej_Hucko', "Jano"])
string_series.str.contains("Hucko")


# find matches
regex=r".*Hucko.*"
string_series.str.match(regex)

from datetime import datetime as dt

now = dt.now()

# konverzia datetime to tyimestamp
now_timestamp = pd.Timestamp(now)
print(type(now_timestamp)) # lebo povodny datetime nemal ziadne
# print(now_timestamp.nanosecond) 
now_timestamp

timestamp = pd.Timestamp(year=2020, month=6, day=9, hour=8, minute=30, second=20, microsecond=79, nanosecond=99)
print(timestamp)
print(type(timestamp))
timestamp.nanosecond

# mikro a nanosekundy sa aplikuju pri vypise len ak existuju
print(pd.Timestamp('2019-8-1'))
print(pd.Timestamp(2020, 6, 9, 12))
print(pd.Timestamp('2020-06-09 00:00:00'))
print(pd.Timestamp('August 9, 2020 13:45'))
print(pd.Timestamp('2020-01-01T14'))
print(pd.Timestamp(300)) # <--- number of seconds after UNIX epoch (January 1, 1970)
print(pd.Timestamp(1513393355.5))

import pandas as pd
import numpy as np
# Nan hodnota ma svoj specialny objekt 
nan_dt = pd.Timestamp(np.nan)
print(type(nan_dt))
nan_dt

# Pandas timestamp series
sample_timestamps = pd.date_range("2020-01-09", freq="D", periods=3) # pomocou funkcie daterange viem vytvorit takzvany  DatetimeIndex
sample_timestamps
df = pd.DataFrame(sample_timestamps, columns=["times"])

import pytz
len(pytz.all_timezones) # pozet vsetkych moznosti pre casove pasma
pytz.all_timezones[:10]

ts = pd.Timestamp(1513393355, tz="Europe/Bratislava")

# pouzitie s dataframmom 
sample_timestamps = pd.date_range("2020-01-09", freq="D", periods=3, tz="Etc/GMT+1") # pomocou funkcie daterange viem vytvorit takzvany  

df = pd.DataFrame(sample_timestamps, columns=["times"])

#If there is timestamp column 
df = pd.read_csv("dataset/timestamps_dataset.csv", parse_dates=["timestamp"])

#TIME DELTA
x = pd.Timestamp(year=2020, month=6, day=9, hour=8, minute=30, second=20, microsecond=79, nanosecond=99)
y = pd.Timestamp(year=2020, month=6, day=9, hour=8, minute=30, second=20, microsecond=79, nanosecond=89)
result = x - y #can be negative

# Konštruktor v pandase 
td1 = pd.Timedelta("1 days 00:42:00.89834") # len pomocou stringu 
print(td1)

# Konstruktor v pythone 
from datetime import timedelta

td2 = timedelta(days=55, seconds=3621, microseconds=992006)

vysledok = td1 + td2

# vieme ich hladne pripocitavat/odpocitavat  k timestampu 
ts = pd.Timestamp(dt.now())














