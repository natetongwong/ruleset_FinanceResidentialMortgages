from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test_riskassetclasssegmentation.config.ConfigStore import *
from test_riskassetclasssegmentation.functions import *
from prophecy.utils import *
from test_riskassetclasssegmentation.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Sample_Data = Sample_Data(spark)
    df_Apply_Rule = Apply_Rule(spark, df_Sample_Data)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Test_RiskAssetClassSegmentation")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Test_RiskAssetClassSegmentation")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/Test_RiskAssetClassSegmentation", config = Config)(
        pipeline
    )

if __name__ == "__main__":
    main()
