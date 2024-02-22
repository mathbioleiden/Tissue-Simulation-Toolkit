import numpy as np
import numpy.typing as npt


def empty_f64() -> npt.NDArray[np.float64]:
    """Helper function for default-initialising arrays."""
    return np.empty(0, dtype=np.float64)


def empty_i32() -> npt.NDArray[np.int32]:
    """Helper function for default-initialising arrays."""
    return np.empty(0, dtype=np.int32)
