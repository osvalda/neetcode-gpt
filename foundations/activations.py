import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        result = []
        for act in z:
            result.append(np.round(1 / (1 + pow(math.e, (-act)) ), 5))
        return result
        pass

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        result = []
        for act in z:
            if act >=0:
                result.append(act)
            else:
                result.append(0.0)
        return result
        pass
