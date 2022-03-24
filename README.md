## Kafka + Flink + Postgres 

## Project: Kraken Crypto Exchange Anomaly Detection
The outline of this project is to create a portable and idempotent ETL architecture that includes:

- CI/CD + testing
- logging
- Monitoring
- Data validation and Quality Checks

The data will be source from an open API provided by the https://support.kraken.com/hc/en-us cryptocurrency exchange. 
The websocket API is public with the endpoint located here:

wss://futures.kraken.com/ws/v1

We will be loking at the BTC (Bitcoin) to US Dollar index Bid/Ask by sending the websocket endpoint the following:


{  "event":"subscribed",  "feed":"ticker",  "product_ids":["PI_XBTUSD"] }


This will return a JSON object with the following information (Example)
{
  "time": 1612270825253,
  "feed": "ticker",

  "product_id": "PI_XBTUSD",

  "bid": 34832.5,

  "ask": 34847.5,

  "bid_size": 42864,

  "ask_size": 2300,

  "volume": 262306237,

  "dtm": 0,

  "leverage": "50x",

  "index": 34803.45,

  "premium": 0.1,

  "last": 34852,

  "change": 2.995109121267192,

  "funding_rate": 3.891007752e-9,

  "funding_rate_prediction": 4.2233756e-9,

  "suspended": false,

  "tag": "perpetual",

  "pair": "XBT:USD",

  "openInterest": 107706940,

  "markPrice": 34844.25,

  "maturityTime": 0,

  "relative_funding_rate": 0.000135046879166667,

  "relative_funding_rate_prediction": 0.000146960125,

  "next_funding_rate_time": 1612281600000

} 
 
 
More documentation about the product ID's can be found here:
https://support.kraken.com/hc/en-us/articles/360022835891-Ticker-symbols

## Problem outline



