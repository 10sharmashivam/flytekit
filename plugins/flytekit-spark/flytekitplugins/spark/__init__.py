"""
.. currentmodule:: flytekitplugins.spark

This package contains things that are useful when extending Flytekit.

.. autosummary::
   :template: custom.rst
   :toctree: generated/

   new_spark_session
   ParquetToSparkDecodingHandler
   Spark
   SparkDataFrameSchemaReader
   SparkDataFrameSchemaWriter
   SparkDataFrameTransformer  # noqa
"""

from flytekit.configuration import internal as _internal

from .connector import DatabricksConnector
from .generic_task import GenericSparkConf
from .pyspark_transformers import PySparkPipelineModelTransformer
from .schema import SparkDataFrameSchemaReader, SparkDataFrameSchemaWriter, SparkDataFrameTransformer  # noqa
from .sd_transformers import ParquetToSparkDecodingHandler, SparkToParquetEncodingHandler
from .task import Databricks, DatabricksV2, Spark, new_spark_session  # noqa
