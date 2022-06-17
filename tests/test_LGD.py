import LGD_t_test as LGD
import pytest
import pandas as pd

def test_LGD():
    df = pd.read_excel('synthetic_pd.xlsx')
    output = LGD.lgd_t_test(df=df, observed_LGD_col='LGD', expected_LGD_col='PRED_LGD')
    assert output[0] == 373028
    assert round(output[1], 3) == 6581.532
    assert round(output[2], 3) == 6584.700
    assert round(output[3], 3) == -19.159
    assert round(output[4], 3) == 10197.483
    assert round(output[5], 5) == 1.00000