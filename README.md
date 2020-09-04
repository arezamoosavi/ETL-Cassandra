# ETL-ML-Cassandra

In this project, by using Google stock data, an ETL job is done with benefits of pandas data frame and Cassandra database. Then after that, all data are extracted from Cassandra and after prepossessing for the purpose of predicting the next month stock's closing price is done, a linear model is going to be developed. Finally, a linear model with Test Accuracy of  96.88 % is designed.

## Run

By this command all task will be run:
```bash
docker-compose up --build
```
To remove containers:
```bash
docker-compose down -v
```
## Tools
ML: Pandas, Sklearn


DB: Cassandra


Build: docker, docker-compose

## [Medium](https://medium.com/@sdamoosavi/google-stock-data-etl-with-cassandra-and-predictive-modeling-with-it-756a56b49ea9)
