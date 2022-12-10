# Team_Coders
DATA MINING GROUP PROJECT

# Predicting NHL statistics using ML

## Introduction

This project explores using data mining on Official [NHL stats API](https://statsapi.web.nhl.com/api/v1/). 
Easy use of this API was possible thanks to this incredible [documentation](https://gitlab.com/dword4/nhlapi/-/blob/master/stats-api.md).

## Data Mining
Data is collected from previously mentioned official and free NHL statistics API. For optimization and caching reasons this data is fetched into simple sql data [SQLite](https://www.sqlite.org/index.html)

## Dependencies
- unidecode
- grequests
- tqdm
