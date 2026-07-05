# Databricks notebook source
import sys
sys.path.append("../src")
from my_package.transform import clean_customers

df = spark.read.table("bronze.customers")
result = clean_customers(df)
result.write.mode("overwrite").saveAsTable("silver.customers")