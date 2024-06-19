from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_rule.config.ConfigStore import *
from test_rule.functions import *

def Sample_Data(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load(Config.parquet_filename)
