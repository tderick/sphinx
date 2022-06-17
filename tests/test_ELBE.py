import Expected_Loss_Best_Estimate_t_test as ELBE
import pytest
import pandas as pd


def test_ELBE():
    df = pd.read_excel('synthetic_pd.xlsx')
    output = ELBE.elbe_t_test(df=df, LGD_col='LGD', ELBE_col='ELBE')
    assert output[0] == 373028
    assert round(output[1], 3) == 6581.532
    assert round(output[2], 3) == 6581.027
    assert round(output[3], 5) == 0.53385
    assert round(output[4], 3) == 333868.036
    assert round(output[5], 5) == 0.59344
