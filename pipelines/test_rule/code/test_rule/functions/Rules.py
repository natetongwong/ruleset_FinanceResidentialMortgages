from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

def Override_Housing_Purpose(
        secnd_purps_type_lbl: Column=col("Secnd_Purps_Type_Lbl"), 
        origination_system: Column=col("Origination_system"), 
        housing_purpose: Column=col("Housing_Purpose")
):
    return when(
          (
            (
              (secnd_purps_type_lbl == lit(231))
              & (origination_system == lit("MP-001"))
            )
            & (housing_purpose == lit("OO"))
          ),
          lit("IPL")
        )\
        .otherwise(col("housing_purpose"))\
        .alias("EFS_Housing_Purpose")
