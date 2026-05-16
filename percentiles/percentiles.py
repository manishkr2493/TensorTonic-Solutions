import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    a = np.array(x)
    b = np.array(q)

    return np.percentile(x,q, method ='linear')