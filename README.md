
Weather Monitoring and Prediction System

Overview
This project implements a real-time weather monitoring and prediction system. It uses Apache Kafka to collect live weather data from the OpenWeatherMap API, processes the data using Apache Spark (PySpark), predicts future temperatures using a linear regression model, and visualizes results through an interactive dashboard built with Dash. The system is deployed using a distributed cluster architecture with one master node and one slave node.

Technologies Used
Apache Kafka
Apache Spark (PySpark)
OpenWeatherMap API
Dash (Plotly)
Python (pandas, requests, csv, json)

System Architecture
The project is deployed using a master-slave cluster configuration.

* The master node is responsible for coordinating Spark jobs and managing the resource allocation.
* The slave node runs the Spark executor processes that actually perform the data processing tasks.
* Both nodes communicate over the network and share data files using a shared directory or network file system.
* Kafka is run on the master node, and Spark is configured in standalone cluster mode with appropriate `SPARK_HOME`, `conf/slaves`, and `start-slave.sh` setup.

Workflow

1. Data Collection with Kafka
   Fetches current weather data from the OpenWeatherMap API for multiple Canadian cities.
   Writes data to CSV files named weather\_forecast.csv and predict\_forecast.csv.
   Publishes data to the Kafka topic named weather\_topic.

2. Data Analysis with PySpark
   Loads weather data into Spark DataFrames.
   Converts temperature, humidity, wind speed, and cloudiness columns to numeric types.
   Calculates average weather statistics per city.
   Applies a linear regression model using Spark MLlib to predict temperatures.

3. Visualization with Dash
   Displays bar graphs comparing actual and predicted values for temperature and humidity.
   Provides an interactive interface to compare city-wise forecasts.

Project Structure

weather\_forecast.csv - Real-time collected weather data
predict\_forecast.csv - Predicted weather data for next day
kafka\_producer.py - Script to fetch and stream data into Kafka
spark\_analysis.py - PySpark script to calculate average weather statistics
temperature\_prediction.py - Spark ML pipeline to predict temperature
dashboard.py - Dash web app to visualize data
README.md - Documentation file

Features
Real-time data ingestion using Kafka
Batch processing and analysis with PySpark
Linear regression-based temperature prediction
Interactive data visualization dashboard
Tested on a distributed Spark setup with master and slave machines

Sample Output from Spark
City          Average Temperature    Average Humidity    Wind Speed    Cloudiness
Toronto            275.62                    92.0               3.6            100.0
Edmonton           263.74                    75.0               2.24            56.0

Setup Instructions

1. Set up Kafka and start the broker on the master node (localhost:9092)
2. Configure Spark in standalone cluster mode with one master and one slave
3. Run kafka\_producer.py to collect and send weather data to Kafka
4. Run spark\_analysis.py on the master node to process the collected data
5. Run temperature\_prediction.py to perform prediction using Spark MLlib
6. Run dashboard.py to launch the Dash web interface and visualize results


