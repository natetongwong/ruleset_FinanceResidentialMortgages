from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, parquet_filename: str=None, **kwargs):
        self.spark = None
        self.update(parquet_filename)

    def update(self, parquet_filename: str="adls:/paruqet_20180830.parquet", **kwargs):
        prophecy_spark = self.spark
        self.parquet_filename = parquet_filename
        pass
