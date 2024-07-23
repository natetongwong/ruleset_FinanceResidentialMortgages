from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test_rule.config.ConfigStore import *
from test_rule.functions import *
from prophecy.utils import *
from test_rule.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Sample_Data = Sample_Data(spark)
    df_Reformat = Reformat(spark, df_Sample_Data)
    df_add_override_housing_purpose = add_override_housing_purpose(spark, df_Reformat)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("test_rule")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/test_rule")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/test_rule", config = Config)(pipeline)

if __name__ == "__main__":
    main()
