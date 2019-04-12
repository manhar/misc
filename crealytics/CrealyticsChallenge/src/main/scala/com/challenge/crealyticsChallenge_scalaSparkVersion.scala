package com.challenge
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.expressions.Window
import org.apache.spark.sql.functions._


import org.apache.spark.SparkConf
import org.apache.spark.SparkContext

object crealyticsChallenge_scalaSparkVersion {
  
  
  def main(args: Array[String]): Unit = {
   
        
    val filename=args(0)
    val output_filename="/Users/ashish/GoogleDrive/crealytics_test_output.csv"
    
    //create spark session
    val spark = SparkSession.builder().master("local").appName("CrealyticsChallenge").getOrCreate()
    
    //read file into a dataframe
    val df = spark.read.option("header","true").option("inferSchema","true").csv(filename) 
    
    //define a window of T=60
    val window = Window.orderBy("time").rangeBetween(-60L, 0L)
    
    //compute derived attributes
    val outDF= df.withColumn("num_obs_in_window", sum(lit(1)).over(window)).withColumn("sum_values_in_window", sum("value").over(window)).withColumn("min_value_in_window", min("value").over(window)).withColumn("max_value_in_window", max("value").over(window))
    
    //write to file
    outDF.coalesce(1).write.mode("overwrite").option("delimiter", "\t").option("header", "true").csv(output_filename)
    
    


    
  }
  
}