import org.apache.spark.sql.functions.{col, explode}
import org.apache.spark.sql.{SaveMode, SparkSession}

import java.time.LocalDate

object FormattedData {

  def main(args:Array[String]): Unit = {
    val spark = SparkSession.builder
      .appName("JobFormatted")
      .getOrCreate()
    val executionDate = spark.conf.get("spark.airflow.execution_date")
    val currentDate: String = if(executionDate != null) executionDate else LocalDate.now().toString


    //quand on veut lancer spark submit manuellement, on commente les 2 lignes du haut et on laisse celle du bas 
    
    //val currentDate: String =  LocalDate.now().toString


    var df= spark.read.json(s"hdfs://localhost:9000/datalake/raw/match/$currentDate.json")
    
    df.write.parquet(s"hdfs://localhost:9000/datalake/formatted/$currentDate")
    
    /*
    * Write your code here
    * Just use the currentDate*/
  }
}
