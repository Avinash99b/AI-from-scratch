import math

import numpy as np

#These weights are aquired by 10,000 epoch trains
weights = [0.6999999999999986, -0.19999999999999968, -0.20000000000000018]

bias = 0.4000

inputs = [1.0, 2.0, -1.5]

print(np.dot(weights,inputs)+bias)