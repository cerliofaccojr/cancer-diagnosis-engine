#!/usr/bin/env python
# coding=utf-8

"""AcquisitorAndCleaner engine action.

Use this module to add the project main code.
"""

from .._compatibility import six
from .._logging import get_logger

from marvin_python_toolbox.engine_base import EngineBaseDataHandler
from marvin_python_toolbox.common.data import MarvinData
import pandas as pd


__all__ = ['AcquisitorAndCleaner']


logger = get_logger('acquisitor_and_cleaner')

class AcquisitorAndCleaner(EngineBaseDataHandler):

    def __init__(self, **kwargs):
        super(AcquisitorAndCleaner, self).__init__(**kwargs)

    def execute(self, params, **kwargs):
        data = pd.read_csv("/desenvolvimento/marvin/data/diag.csv")
        data = data.drop("id", axis=1)
        data = data.rename(columns={"diagnosis": "label"})
        data['diagnosis_num'] = data.label.map({'B': 0, 'M': 1})
        data = data.drop("label", axis=1)
        self.marvin_initial_dataset = data
