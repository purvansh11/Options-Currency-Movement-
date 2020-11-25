def convert(regions):
    currency_of = {}
    region_of = {}
    currency_of["AUSTRALIA"] = "AUD"
    currency_of["EURO"] = "EUR"
    currency_of["NEW"] = "NZD"
    currency_of["UNITED"] = "GBP"
    currency_of["BRAZIL"] = "BRL"
    currency_of["CANADA"] = "CAD"
    currency_of["CHINA"] = "CNY"
    currency_of["HONG"] = "HKD"
    currency_of["INDIA"] = "INR"
    currency_of["KOREA"] = "KRW"
    currency_of["MEXICO"] = "MXN"
    currency_of["SOUTH"] = "ZAR"
    currency_of["SINGAPORE"] = "SGD"
    currency_of["DENMARK"] = "DKK"
    currency_of["JAPAN"] = "JPY"
    currency_of["MALAYSIA"] = "MYR"
    currency_of["NORWAY"] = "NOK"
    currency_of["SWEDEN"] = "SEK"
    currency_of["SRI"] = "LKR"
    currency_of["SWITZERLAND"] = "CHF"
    currency_of["TAIWAN"] = "TWD"
    currency_of["THAILAND"] = "THB"
    for region in regions:
        if region == "Unnamed:" or region == "Time":
            continue
        region_of[currency_of[region]] = region
    return [currency_of,region_of]