

**Weather Monitoring and Prediction System**

**Overview**
This project implements a real-time weather monitoring and prediction system. It uses Apache Kafka to collect live weather data from the OpenWeatherMap API, processes the data using Apache Spark (PySpark), predicts future temperatures using a linear regression model, and visualizes the results through an interactive dashboard built with Dash. The system is deployed using a distributed cluster architecture consisting of one master node and one slave node.

**Technologies Used**

* Apache Kafka
* Apache Spark (PySpark)
* OpenWeatherMap API
* Dash (Plotly)
* Python (pandas, requests, csv, json)

**System Architecture**
The project is deployed using a master-slave cluster configuration:

* The **master node** coordinates Spark jobs and manages resource allocation.
* The **slave node** runs the Spark executor processes that carry out the data processing tasks.
* Both nodes communicate over the same network and use a shared directory or network file system for file access.
* Kafka is hosted on the master node, and Spark is configured in standalone cluster mode using environment variables (`SPARK_HOME`) and configuration files (`conf/slaves`, `start-slave.sh`, etc.).

**Workflow**

1. **Data Collection with Kafka**

   * Fetches real-time weather data from the OpenWeatherMap API for multiple Canadian cities.
   * Stores the data in `weather_forecast.csv` and `predict_forecast.csv`.
   * Publishes data to the Kafka topic named `weather_topic`.

2. **Data Analysis with PySpark**

   * Loads the CSV files into Spark DataFrames.
   * Converts temperature, humidity, wind speed, and cloudiness columns to appropriate numeric types.
   * Calculates average weather statistics for each city.
   * Uses Spark MLlib to apply a linear regression model and predict temperature.

3. **Visualization with Dash**

   * Displays bar charts comparing actual and predicted values for temperature and humidity.
   * Provides an interactive interface for comparing city-wise forecasts.

**Project Structure**

* `weather_forecast.csv` – Real-time collected weather data
* `predict_forecast.csv` – Predicted weather data for the next day
* `kafka_producer.py` – Script to fetch and stream data into Kafka
* `spark_analysis.py` – PySpark script for calculating weather statistics
* `temperature_prediction.py` – Spark ML pipeline for temperature prediction
* `dashboard.py` – Dash web application for visualization
* `README.md` – Documentation file

**Key Features**

* Real-time data ingestion using Kafka
* Scalable batch data processing using Apache Spark
* Machine learning-based temperature prediction using linear regression
* Interactive dashboard for visualization
* Tested on a distributed Spark setup with master and slave nodes

**Sample Output from Spark**

| City     | Average Temperature | Average Humidity | Wind Speed | Cloudiness |
| -------- | ------------------- | ---------------- | ---------- | ---------- |
| Toronto  | 275.62              | 92.0             | 3.6        | 100.0      |
| Edmonton | 263.74              | 75.0             | 2.24       | 56.0       |

**Setup Instructions**

1. Set up Kafka and start the broker on the master node (localhost:9092).
2. Configure Spark in standalone cluster mode with one master and one slave node.
3. Run `kafka_producer.py` to collect and stream weather data to Kafka.
4. Execute `spark_analysis.py` on the master node to process the collected data.
5. Run `temperature_prediction.py` to perform temperature prediction using Spark MLlib.
6. Launch `dashboard.py` to start the Dash web interface and visualize results.

