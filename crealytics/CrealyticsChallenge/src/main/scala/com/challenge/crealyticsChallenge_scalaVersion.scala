package com.challenge
import scala.io.Source
import scala.collection.mutable.ArrayBuffer
import scala.collection.mutable.ListBuffer
object crealyticsChallenge_scalaVersion {
  
   def process(filename: String): ArrayBuffer[String]={
     
     val rows = ArrayBuffer[String]()
     val myList = Source.fromFile(filename, "UTF8").getLines().toList.sorted.reverse //read file in list, then sort file then reverse content
     val line =0
     val T = 60 //window size
     val total_lines=myList.length-1
     //println("total line:" + myList.length)
     for ( line <- 0 to total_lines ){
       
       val lineArr= myList(line).split("\t").map(_.trim())
       var curr_time = lineArr(0).toInt 
       var curr_value = lineArr(1).toFloat
       var min_value, max_value,sum =0.0
       var counter = 0  //counter to capture number of observations in a sliding window
       var next_index=line+1
       var time_diff=0
 
       sum=curr_value
       min_value = curr_value
       max_value = curr_value

          while ((time_diff >=0 && time_diff <= T) && (next_index <= total_lines )){
            var next_line = myList(next_index).split("\t").map(_.trim())
            val next_time = next_line(0).toInt
            val next_value = next_line(1).toFloat
            time_diff = curr_time - next_time
            counter +=1
          
              if (time_diff >=0 && time_diff <= T){
                min_value = math.min(next_value, min_value)
                max_value = math.max(next_value, max_value)
                sum =  BigDecimal(next_value).setScale(5, BigDecimal.RoundingMode.HALF_UP).toDouble +  sum
              }
            
            next_index +=1
            
          }

       if (next_index==total_lines+1) counter+=1
       val window_NO=counter
       val window_sum=BigDecimal(sum).setScale(5, BigDecimal.RoundingMode.HALF_UP).toDouble
       val window_min=BigDecimal(min_value).setScale(5, BigDecimal.RoundingMode.HALF_UP).toDouble
       val window_max = BigDecimal(max_value).setScale(5, BigDecimal.RoundingMode.HALF_UP).toDouble  
       
       //build result and append to rows ArrayBuffer
        rows+=curr_time.toString()+"\t"+ 
           curr_value.toString()+"\t"+
           window_NO.toString()+"\t"+
            window_sum.toString()+"\t"+
            window_min.toString()+"\t"+
           window_max.toString()+"\n"
           
     }
     
    return rows.reverse
     
   }
   
   
   def main(args: Array[String]): Unit = {
     
     val filename=args(0) //read argument
     val result = process(filename)
     
     result.foreach(print(_))  //print result
  
    
  } 
  
}