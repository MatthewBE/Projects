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


This will return a JSON object with the following information:

{
  "time": <  positive integer: 	The UTC time of the server in milliseconds>,
  "feed": < string: 	The subscribed feed>,
  "product_id": < string: The subscribed product (referred also as instrument or symbol)>,
  "bid": <  positive float: 	The price of the current best bid>,
  "ask": <positive float 	: The price of the current best ask >,
  "bid_size": < positive float : The size of the current best bid>,
  "ask_size": < positive float 	:The size of the current best ask>,
  "volume": < positive float : The sum of the sizes of all fills observed in the last 24 hours>,
  "dtm": <  positive integer 	: The days until maturity>,
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




