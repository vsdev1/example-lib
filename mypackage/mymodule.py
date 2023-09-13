from typing import List

import numpy as np
import importlib.metadata


def print_version() -> None:
    package_name = "myexamplelib"
    print(f"version of {package_name}: {importlib.metadata.version(package_name)}")


def create_array(l: List) -> np.ndarray:
    return np.array(l, np.int32)


if __name__ == "__main__":
    print_version()
