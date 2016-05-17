import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.datasets import load_boston
boston = load_boston()