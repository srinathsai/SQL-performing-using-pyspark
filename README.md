# SQL-performing-using-pyspark

## Goal:-
To perform sql functions of groupby using pyspark.<br />

## INTRODUCTION:-
Apache Spark is an open source data processing engine for storing and processing data in real time across different computer clusters using a simple programming structure. Spark was construct to cover a wide range of workloads such as batch applications, iterative algorithms, interactive queries, and streaming. Not only does it support all of these workloads in one dedicated system, but it also reduces the administrative burden of maintaining individual tools.<br />

**Spark Core**:
Spark Core is the heart of Spark and performs its core functions. It includes components for task scheduling, troubleshooting, storage system interaction, and storage management.<br />

**Spark SQL**:
Spark is one of the most successful projects the Apache Software Foundation has ever devised.Spark SQL is built on top of SparkCore. it is working with structured and semi-structured data.Structured data has a schema with a known set of fields. If the schema and data are not separated,the data is said to be semi-structured. To put is briefly, structured and semi-structured data processing uses Spark SQL, which is just a module of Spark. It also supports a variety of data
sources such as Hive tables, Parquet and JSON.<br />

**Spark Streaming**:
Spark Streaming is a Spark element that helps scalable and fault-tolerant processing of streaming data. Leverage Spark Core's fast scheduling capabilities to perform streaming analysis. Accepts mini-batch data and performs RDD conversion on that data. Its design allows applications written to stream data to be reused to analyze batches of historical data with few changes. The log file generated by the web server can be viewed as a real-time example of a data stream.<br />

**Spark MLib** :
Apache Spark MLlib is an Apache Spark machine learning library that consists of common learning algorithms and utilities such as classification, regression, clustering, collaborative filtering, dimensionality reduction, and underlying optimization primitives.<br />

**GraphX** :
GraphX is a library used to control graphs and carry out graph parallel computations. It helps various fundamental operators such as Subgraph, Join Vertices, and Aggregate Messages for running with graphs. This facilitates the introduction of directed graphs with arbitrary properties
related to each vertex and facet.<br />

**Pysprark**:
PySpark is the association of Apache Spark and Python. Apache Spark is an analytics processing engine for large, high-performance distributed data processing and machine learning applications.<br />

A PySpark library for applying SQL-like analysis to large amounts of structured or semi-structured data. We can also use SQL queries with PySpark SQL. You can also connect to Apache Hive.HiveQL can also be applied. PySpark SQL is a wrapper for the PySpark core. PySpark SQL introduced a data frame, which is a tabular representation of structured data that resembles a table in a relational database management system.<br />

## STEPS OF EXECUTION :- 
FOLLOW THE ATTACHED README PDF.<br />

## CONCLUSION:-
With the help of pyspark a SQL query of grouping by two coloumns in which average of toeflScore along with major has been generated.<br />

## DATASET :- 
Attached csv file downloaded from kaggle.<br />
