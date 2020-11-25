# Instantiation
import pandas as pd
import region_converter
import generator
import graph

dataset = "Foreign_Exchange_Rates.csv"
df = pd.read_csv(dataset)
cnt_rows = df.shape[0]
election_dates = ['2000-09-07' , '2004-09-02' , '2008-09-04' , '2012-09-06' , '2016-09-08']

# Cleaning
updated_df_without_nd = df[df.columns.values[2]]!="ND" 
df = df[updated_df_without_nd]
df.dropna(axis=0,inplace=True)

regions = generator.regions(df.columns)
# col_head["NEW ZEALAND"] = "NEW" 
col_head = generator.col_heads(regions,df.columns)
year_to_date = generator.year_to_date(election_dates)
dates = generator.dates_and_hashes(cnt_rows,df,col_head)[0]
hash_value_dates = generator.dates_and_hashes(cnt_rows,df,col_head)[1]
hash_value_dataframe = generator.dates_and_hashes(cnt_rows,df,col_head)[2]
# cost['2004-09-02']["THAILAND"] = 41.52
cost = generator.cost(dates,regions,df,col_head,hash_value_dataframe)

# Conversion of Region -> It's Currency
region_of = region_converter.convert(regions)[1]
currency_of = region_converter.convert(regions)[0]

buffer_plot = 120
currency = "CHF"
timespan = 3
election_year = "2016"
strike = 0.1
date = year_to_date[election_year]

[x_values,traded_at] = graph.trading_plot(120,dates,hash_value_dates,region_of,cost,date,currency,timespan,election_year)
[euro_plot,american_plot,days_after_election] = graph.options_plot(traded_at,hash_value_dates,dates,buffer_plot,date,timespan,strike)
