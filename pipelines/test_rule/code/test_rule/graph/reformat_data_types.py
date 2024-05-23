from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from test_rule.config.ConfigStore import *
from test_rule.functions import *

def reformat_data_types(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("From_Date"), 
        col("To_Date"), 
        col("Account_Id"), 
        col("Src_Sys_Code"), 
        col("Product_Code"), 
        col("Gl_Account_Id"), 
        col("Legal_Entity_Id"), 
        col("Current_Balance"), 
        col("Maturity_Date"), 
        col("Opened_Date"), 
        col("Currency"), 
        col("From_Date2"), 
        col("To_Date2"), 
        col("AppIn_Id"), 
        col("Origination_system"), 
        col("Prim_Purps_Type_Lbl"), 
        col("Secnd_Purps_Type_Lbl").cast(IntegerType()).alias("Secnd_Purps_Type_Lbl"), 
        col("Crncy_Code"), 
        col("Apprv_Lmt_Amt"), 
        col("Predominant_Purpose"), 
        col("Housing_Purpose"), 
        col("Sub_Purpose"), 
        col("EFS_Housing_purpose_Rule_ID")
    )
