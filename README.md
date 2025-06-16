
**Weather Monitoring and Prediction System**

**Overview**
This project implements a real-time weather monitoring and prediction system using big data technologies. It leverages Apache Kafka to collect live weather data from the OpenWeatherMap API, processes the data using Apache Spark (PySpark), applies machine learning to predict temperatures, and visualizes the results using an interactive dashboard built with Dash. The system is deployed in a distributed environment with a master-slave cluster setup.

**Technologies Used**

* Apache Kafka
* Apache Spark (PySpark)
* OpenWeatherMap API
* Dash (Plotly)
* Python (pandas, requests, csv, json)

**System Architecture**
The system follows a master-slave cluster configuration:

* The **master node** manages Spark job coordination and resource allocation.
* The **slave node** executes Spark tasks in parallel.
* Data is shared via a common directory or a network file system.
* Kafka runs on the master node. Spark is configured in standalone cluster mode with appropriate settings in `SPARK_HOME`, `conf/slaves`, and started using `start-slave.sh`.

**Workflow**

1. **Data Collection with Kafka**

   * The script `kafkafetch.ipynb` fetches live weather data for multiple Canadian cities using the OpenWeatherMap API.
   * The collected data is written to `weather_forecast.csv` and `predict_forecast.csv`.
   * The data is also published to a Kafka topic named `weather_topic`.

2. **Data Analysis and Prediction with PySpark**

   * The notebook `analysis.ipynb` loads the weather data, converts numeric columns, and calculates per-city statistics.
   * The notebook `prediction.ipynb` builds and applies a linear regression model using Spark MLlib to predict temperature based on humidity, wind speed, and cloudiness.

3. **Visualization with Dash**

   * The script `dashboard.py` launches a Dash application to visualize actual vs. predicted values of temperature and humidity.
   * The dashboard allows users to interactively compare forecasts city-wise.

**Project Files**

* `kafkafetch.ipynb`: Fetches weather data and sends it to Kafka
* `weather_forecast.csv`: Collected weather data (current)
* `predict_forecast.csv`: Forecasted weather data (next day)
* `analysis.ipynb`: PySpark-based analysis of weather statistics
* `prediction.ipynb`: Linear regression model and prediction using Spark
* `dashboard.py`: Web dashboard for interactive visualization
* `README.md`: Project documentation

**Features**

* Real-time weather data ingestion using Kafka
* Distributed processing with PySpark
* Machine learning predictions using Spark MLlib
* Interactive visualization through Dash
* Tested in a cluster environment with master and slave Spark nodes

**Sample Output (from analysis)**

| City     | Avg Temperature | Avg Humidity | Wind Speed | Cloudiness |
| -------- | --------------- | ------------ | ---------- | ---------- |
| Toronto  | 275.62          | 92.0         | 3.6        | 100.0      |
| Edmonton | 263.74          | 75.0         | 2.24       | 56.0       |

**How to Run the Project**

1. Start Kafka broker on master node (default: localhost:9092)
2. Configure Spark in standalone cluster mode (1 master, 1 slave)
3. Run `kafkafetch.ipynb` to collect and publish weather data
4. Run `analysis.ipynb` to compute average statistics
5. Run `prediction.ipynb` to generate temperature predictions
6. Run `dashboard.py` to launch the web-based dashboard


