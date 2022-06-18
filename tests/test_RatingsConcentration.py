import Concentration_of_Rating_Grades as RC
import pytest
import pandas as pd


def test_RC():
    df = pd.read_excel('synthetic_pd.xlsx')
    output = RC.ratings_concentration(df=df, initial_ratings_col='ratings', final_ratings_col='ratings2')
    assert round(output[0], 6) == 8e-06
    assert round(output[1], 6) == 0.020336
    assert round(output[2], 6) == 1.0
    assert round(output[3], 6) == 373028
