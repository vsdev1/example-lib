from typing import List

import numpy as np


def print_hi(name) -> None:
    print(f"Hi, {name}")


def create_array(l: List) -> np.ndarray:
    return np.array(l, np.int32)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Max')
