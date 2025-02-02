""" Scan outlier metrics
"""

#+ Your imports here.
import numpy as np

def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the sum of the (voxel differences squared) divided by the number of
    voxels).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumnes in `img`.
    """
    # Hint: remember 'axis='.  For example:
    # In [2]: arr = np.array([[2, 3, 4], [5, 6, 7]])
    # In [3]: np.mean(arr, axis=1)
    # Out[2]: array([3., 6.])
    #
    # You may be be able to solve this in four lines, without a loop.
    # But solve it any way you can.
    data = img.get_fdata()
    voxel_per_time = np.reshape(data, (-1, data.shape[-1]))
    diff = np.diff(voxel_per_time)
    dvals = np.sqrt(np.mean(diff ** 2, axis=0))
    return dvals
