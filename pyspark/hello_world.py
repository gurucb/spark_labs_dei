import pyspark.conf
from pyspark.sql import SparkSession
import pyspark
import os

def main():
    # Initialize SparkSession
    
# Initialize SparkConf
    conf = pyspark.SparkConf()
    conf.setMaster("spark://127.0.0.1:7077")

    # Initialize SparkSession with the SparkConf
    spark = SparkSession.builder \
        .appName("HelloWorld") \
        .config(conf=conf) \
        .getOrCreate()


    data = [("Alice", 1), ("Bob", 2), ("Cathy", 3)]
    df = spark.createDataFrame(data, ["Name", "Value"])

    # Show the DataFrame
    df.show()

    print(f"Count of numbers from 1 to 1000 is:500")

    # Stop the SparkSession
    spark.stop()


if __name__ == "__main__":
    main()