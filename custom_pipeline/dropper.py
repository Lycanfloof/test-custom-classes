import numpy as np
import pandas as pd

from sklearn.base import TransformerMixin

class Dropper (TransformerMixin):
  def fit(self, X, y = None):
    return self

  def transform(self, X):
    return X.drop(['id', 'rated', 'created_at', 'last_move_at', 'victory_status', 'winner', 'increment_code', 'white_id', 'white_rating', 'black_id', 'black_rating', 'moves', 'opening_eco', 'opening_name', 'opening_ply'], axis = 1)