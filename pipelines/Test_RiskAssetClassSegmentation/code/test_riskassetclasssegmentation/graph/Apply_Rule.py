from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_riskassetclasssegmentation.config.ConfigStore import *
from test_riskassetclasssegmentation.functions import *

def Apply_Rule(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn(get_alias(RiskAssetClassSegmentation()), RiskAssetClassSegmentation())
