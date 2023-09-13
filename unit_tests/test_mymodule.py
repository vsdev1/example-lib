import numpy as np
from mypackage.mymodule import create_array


def test_create_array():
    l = [1, 2, 3]
    assert np.array_equal(create_array(l), np.array(l, np.int32))
