#!/usr/bin/env python
# coding=utf-8

"""TrainingPreparator engine action.

Use this module to add the project main code.
"""

from .._compatibility import six
from .._logging import get_logger
from sklearn.cross_validation import train_test_split
from marvin_python_toolbox.engine_base import EngineBaseDataHandler

__all__ = ['TrainingPreparator']


logger = get_logger('training_preparator')


class TrainingPreparator(EngineBaseDataHandler):

    def __init__(self, **kwargs):
        super(TrainingPreparator, self).__init__(**kwargs)

    def execute(self, params, **kwargs):
        train, test = train_test_split(self.marvin_initial_dataset, test_size=0.3)

        train_x = train[train.columns[0:len(train.columns) - 1]]
        train_y = train[train.columns[len(train.columns) - 1:len(train.columns)]]

        test_x = test[test.columns[:len(test.columns) - 1]]
        test_y = test[test.columns[len(test.columns) - 1:len(test.columns)]]

        train_x = train_x.stack().str.replace(',', '.').unstack()
        test_x = test_x.stack().str.replace(',', '.').unstack()


        self.marvin_dataset = {
            "X_train": train_x,
            "X_test": test_x,
            "y_train": train_y,
            "y_test": test_y
        }

