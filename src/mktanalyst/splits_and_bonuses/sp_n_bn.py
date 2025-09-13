# https://www.nseindia.com/api/corporates-corporateActions?index=equities&from_date=28-04-2025&to_date=13-09-2025&subject=Split
# Gives a response like:
# [{"symbol":"UNITEDPOLY","series":"EQ","ind":"-","faceVal":"1","subject":"Face Value Split (Sub-Division) - From Rs 10/- Per Share To Re 1/- Per Share","exDate":"02-May-2025","recDate":"02-May-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"United Polyfab Gujarat Limited","isin":"INE368U01011","ndEndDate":"-","caBroadcastDate":null},{"symbol":"NAUKRI","series":"EQ","ind":"-","faceVal":"2","subject":"Face Value Split (Sub-Division) - From Rs 10/- Per Share To Rs 2/- Per Share","exDate":"07-May-2025","recDate":"07-May-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Info Edge (India) Limited","isin":"INE663F01024","ndEndDate":"-","caBroadcastDate":null},{"symbol":"NAVKARURB","series":"EQ","ind":"-","faceVal":"1","subject":"Face Value Split (Sub-Division) - From Rs 2/- Per Share To Re 1/- Per Share","exDate":"09-May-2025","recDate":"09-May-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Navkar Urbanstructure Limited","isin":"INE268H01036","ndEndDate":"-","caBroadcastDate":null},{"symbol":"COFORGE","series":"EQ","ind":"-","faceVal":"2","subject":"Face Value Split (Sub-Division) - From Rs 10/- Per Share To Rs 2/- Per Share","exDate":"04-Jun-2025","recDate":"04-Jun-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Coforge Limited","isin":"INE591G01017","ndEndDate":"-","caBroadcastDate":null},{"symbol":"VESUVIUS","series":"EQ","ind":"-","faceVal":"1","subject":"Face Value Split (Sub-Division) - From Rs 10/- Per Share To Re 1/- Per Share","exDate":"10-Jun-2025","recDate":"10-Jun-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Vesuvius India Limited","isin":"INE386A01015","ndEndDate":"-","caBroadcastDate":null},{"symbol":"BAJFINANCE","series":"EQ","ind":"-","faceVal":"1","subject":"Face Value Split (Sub-Division) - From Rs 2/- Per Share To Re 1/- Per Share","exDate":"16-Jun-2025","recDate":"16-Jun-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Bajaj Finance Limited","isin":"INE296A01016","ndEndDate":"-","caBroadcastDate":null},{"symbol":"PARAS","series":"EQ","ind":"-","faceVal":"5","subject":"Face Value Split (Sub-Division) - From Rs 10/- Per Share To Rs 5/- Per Share","exDate":"04-Jul-2025","recDate":"04-Jul-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Paras Defence and Space Technologies Limited","isin":"INE045601015","ndEndDate":"-","caBroadcastDate":null},{"symbol":"INDOTHAI","series":"EQ","ind":"-","faceVal":"1","subject":"Face Value Split (Sub-Division) - From Rs 10/- Per Share To Re 1/- Per Share","exDate":"18-Jul-2025","recDate":"18-Jul-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Indo Thai Securities Limited","isin":"INE337M01013","ndEndDate":"-","caBroadcastDate":null},{"symbol":"KELLTONTEC","series":"EQ","ind":"-","faceVal":"1","subject":"Face Value Split (Sub-Division) - From Rs 5/- Per Share To Re 1/- Per Share","exDate":"25-Jul-2025","recDate":"25-Jul-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Kellton Tech Solutions Limited","isin":"INE164B01022","ndEndDate":"-","caBroadcastDate":null},{"symbol":"INDIAGLYCO","series":"EQ","ind":"-","faceVal":"5","subject":"Face Value Split (Sub-Division) - From Rs 10/- Per Share To Rs 5/- Per Share","exDate":"12-Aug-2025","recDate":"12-Aug-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"India Glycols Limited","isin":"INE560A01015","ndEndDate":"-","caBroadcastDate":null},{"symbol":"DEVIT","series":"EQ","ind":"-","faceVal":"2","subject":"Face Value Split (Sub-Division) - From Rs 5/- Per Share To Rs 2/- Per Share","exDate":"21-Aug-2025","recDate":"21-Aug-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Dev Information Technology Limited","isin":"INE060X01018","ndEndDate":"-","caBroadcastDate":null},{"symbol":"STEELCAS","series":"EQ","ind":"-","faceVal":"1","subject":"Face Value Split (Sub-Division) - From Rs 5/- Per Share To Re 1/- Per Share","exDate":"29-Aug-2025","recDate":"29-Aug-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Steelcast Limited","isin":"INE124E01020","ndEndDate":"-","caBroadcastDate":null},{"symbol":"PAVNAIND","series":"EQ","ind":"-","faceVal":"1","subject":"Face Value Split (Sub-Division) - From Rs 10/- Per Share To Re 1/- Per Share","exDate":"01-Sep-2025","recDate":"01-Sep-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Pavna Industries Limited","isin":"INE07S101020","ndEndDate":"-","caBroadcastDate":null},{"symbol":"FISCHER","series":"EQ","ind":"-","faceVal":"1","subject":"Face Value Split (Sub-Division) - From Rs 10/- Per Share To Re 1/- Per Share","exDate":"12-Sep-2025","recDate":"12-Sep-2025","bcStartDate":"-","bcEndDate":"-","ndStartDate":"-","comp":"Fischer Medical Ventures Limited","isin":"INE771F01025","ndEndDate":"-","caBroadcastDate":null}]
# My job is to extract the symbol, exDate and the ratio from the subject field

import time
import requests
from urllib.parse import urlencode


def parse_split_info(split_data: list) -> dict:
    split_info = {}
    print("inside parse_split_info")
    for entry in split_data:
        symbol = entry.get("symbol")
        ex_date = entry.get("exDate")
        subject = entry.get("subject", "")
        # Extract ratio from subject using regex
        import re
        match = re.search(r'From Rs (\d+)/- Per Share To Rs? (\d+)/- Per Share', subject)
        if match:
            from_ratio = int(match.group(1))
            to_ratio = int(match.group(2))
            ratio = from_ratio / to_ratio
            split_info[(symbol, ex_date)] = ratio
    return split_info


if __name__ == "__main__":
    # Example usage
    start_date = "28-04-2025"
    end_date = "13-09-2025"
    split_data = fetch_split_data(start_date, end_date)
    split_info = parse_split_info(split_data)
    for key, value in split_info.items():
        print(f"Symbol: {key[0]}, Ex-Date: {key[1]}, Split Ratio: {value}")

