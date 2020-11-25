def regions(columns):
    regions = []
    for col in columns:
        split_name = col.split()
        regions.append(split_name[0])
    return regions

def col_heads(regions,columns):
    col_head = {}
    ind = 0
    for region in regions:
        col_head[region] = columns.values[ind]
        ind += 1
    return col_head

def year_to_date(election_dates):
    year_to_date = {}
    for date in election_dates:
        year_to_date[date[:4]] = date
    return year_to_date

def dates_and_hashes(rows,df,col_head):
    hash_value_dates = {}
    dates = []
    ind = 0
    hash_value_dataframe = {}
    for i in range(rows+1):
        try:
            dates.append(df[col_head["Time"]][i])
            hash_value_dataframe[df[col_head["Time"]][i]] = i
            hash_value_dates[df[col_head["Time"]][i]] = ind
            ind += 1
        except:
            # print("Exception {}".format(e))
            pass
    return [dates,hash_value_dates,hash_value_dataframe]

def cost(dates,regions,df,col_head,hash_value_dataframe):
    cost = {}
    for date in dates:
        cost[date] = {}
    for date in dates:
        for region in regions:
            try:
                cost[date][region] = float(df[col_head[region]][hash_value_dataframe[date]]) 
            except:
                pass
    return cost