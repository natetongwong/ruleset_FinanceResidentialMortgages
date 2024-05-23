from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_riskassetclasssegmentation.config.ConfigStore import *
from test_riskassetclasssegmentation.functions import *

def Sample_Data(spark: SparkSession) -> DataFrame:
    return spark.read.table("`westpac`.`raw`.`assetclasssegmentation_sampledata`")
