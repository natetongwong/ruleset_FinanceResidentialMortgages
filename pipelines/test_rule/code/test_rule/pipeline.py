from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test_rule.config.ConfigStore import *
from test_rule.functions import *
from prophecy.utils import *
from test_rule.graph import *

def pipeline(spark: SparkSession) -> None:
    df_sample_data = sample_data(spark)
    df_reformat_data_types = reformat_data_types(spark, df_sample_data)
    df_add_rule_override_housing_purpose = add_rule_override_housing_purpose(spark, df_reformat_data_types)

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
