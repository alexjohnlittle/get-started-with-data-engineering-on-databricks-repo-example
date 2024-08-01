# Databricks notebook source
# MAGIC %md
# MAGIC ### This is my first notebook
# MAGIC

# COMMAND ----------

print("This is a notebook")

# COMMAND ----------

# MAGIC %run ./Includes/Classroom-Setup-05

# COMMAND ----------

display((
  spark.read.csv(f"{DA.paths.datasets}/customers.csv")
  ))

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM csv.`dbfs:/mnt/dbacademy-datasets/get-started-with-data-engineering-on-databricks/v01/customers.csv`
