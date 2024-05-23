from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_rule.config.ConfigStore import *
from test_rule.functions import *

def Check_Output(spark: SparkSession, add_rule_override_housing_purpose: DataFrame) -> DataFrame:
    return add_rule_override_housing_purpose.select(
        col("Secnd_Purps_Type_Lbl"), 
        col("Origination_system"), 
        col("Housing_Purpose"), 
        col("EFS_Housing_Purpose")
    )
