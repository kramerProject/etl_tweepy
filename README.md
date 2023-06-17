## Description

This a practical activity part of the MBA in Data Engineering from XPE. It consists in a simple ETL using airflow. The are only two dags:

1. The first one is responsible for extracting data from twitter, do a simple transformation and loads into a JSON file.

2. The second one counts the number of people who favorite each tweet.

## Requirements

- Python
- Airflow

## Running with airflow

If you want to run the etl without airflow go to the next section

1. Enter in your airflow folder

```
cd airflow
```

2. Paste the dags folder from this repository into it


3. Run airflow in port 8080

```
airflow webserver -p 8080
```

4. Run airflow scheduler

```
airflow scheduler
```

5. Access you browser in http://localhost:8080/home

6. Create your variables on admin > variables, you should create four:
`access_key`, `access_secret`, `consumer_key` and `consumer_secret`

7. Start the dag, go to DAGS > find twitter_dag > mark DAG in the top left corner

![Start dags](/img/start_dag.png)

8. Press play in the top right corner and click trigger dag

![Trigger dag](/img/trigger_dag.png)

## Running without airflow


1. Create a virtual enviroment and install the necessary packages

```
python3 -m venv .venv

source .venv/bin/activate

pip install apache-airflow

pip install tweepy

```
2. Modify your keys and secrets in lines 7 to 10 of the twitter_etl.py

3. Uncomment line 56 and run the code. After running Just comment again before running the next step

```
python dags/twitter_etl.py
```

4. Uncomment line 57 and run the code

```
python dags/twitter_etl.py
```
