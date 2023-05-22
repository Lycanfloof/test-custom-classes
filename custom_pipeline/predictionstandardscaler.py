import numpy as np
import pandas as pd

from sklearn.base import TransformerMixin
from sklearn.preprocessing import StandardScaler

class PredictionStandardScaler (TransformerMixin):
  def fit(self, X, y = None):
    return self

  def transform(self, X):
    stand_sca = StandardScaler()

    turns = stand_sca.fit_transform(X['turns'].values.reshape(-1, 1))
    X['turns'] = turns

    return X