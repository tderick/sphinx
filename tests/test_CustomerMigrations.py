import Customer_migrations as CM
import pytest
import pandas as pd

def test_CM():
    df = pd.read_excel('synthetic_pd.xlsx')
    output = CM.migration_matrix(df=df, initial_ratings_col='ratings', final_ratings_col='ratings2')
    assert round(output[0], 2) == 1.05
    assert round(output[1],1) == 0.6