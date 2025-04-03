from pyspark.sql import SparkSession
import os
import sys 

# Add the src directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.main.encrypt_decrypt.read_config import get_mysql_credentials


def get_spark_session(app_name="Mysql-Pyspark", mysql_jar_path=r"C:\spark_jars\mysql-connector-j-9.1.0.jar"):
    """
    Initialize and return a Spark session with MySQL JAR configuration.
    """
    return SparkSession.builder \
        .appName(app_name) \
        .config("spark.jars", mysql_jar_path) \
        .getOrCreate()



def get_mysql_connection_properties():
    """
    Fetch MySQL credentials and return connection properties.
    """
    creds = get_mysql_credentials()

    jdbc_url = f"jdbc:mysql://{creds['host']}:{creds['port']}/{creds['database']}?serverTimezone=UTC&useSSL=false"

    connection_properties = {
        "user": creds["user"],
        "password": creds["password"],
        "driver": "com.mysql.cj.jdbc.Driver"
    }

    return jdbc_url,connection_properties


def fetch_data_from_mysql(spark,query):
    jdbc_url, connection_properties = get_mysql_connection_properties()
    df = spark.read.jdbc(url=jdbc_url, table=query, properties=connection_properties).cache()
    return df











