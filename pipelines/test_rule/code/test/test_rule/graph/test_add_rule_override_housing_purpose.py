from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from argparse import Namespace
from prophecy.test import BaseTestCase
from prophecy.test.utils import *
from test_rule.graph.add_rule_override_housing_purpose import *
from test_rule.config.ConfigStore import *


class add_rule_override_housing_purposeTest(BaseTestCase):

    def test_unit_test_(self):
        dfIn0 = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/test_rule/graph/add_rule_override_housing_purpose/in0/schema.json',
            'test/resources/data/test_rule/graph/add_rule_override_housing_purpose/in0/data/test_unit_test_.json',
            'in0'
        )
        dfOut = createDfFromResourceFiles(
            self.spark,
            'test/resources/data/test_rule/graph/add_rule_override_housing_purpose/out/schema.json',
            'test/resources/data/test_rule/graph/add_rule_override_housing_purpose/out/data/test_unit_test_.json',
            'out'
        )
        dfOutComputed = add_rule_override_housing_purpose(self.spark, dfIn0)
        assertDFEquals(
            dfOut.select("EFS_Housing_Purpose"),
            dfOutComputed.select("EFS_Housing_Purpose"),
            self.maxUnequalRowsToShow
        )

    def setUp(self):
        BaseTestCase.setUp(self)
        import os
        fabricName = os.environ['FABRIC_NAME']
        Utils.initializeFromArgs(
            self.spark,
            Namespace(
              file = f"configs/resources/config/{fabricName}.json",
              config = None,
              overrideJson = None,
              defaultConfFile = None
            )
        )
