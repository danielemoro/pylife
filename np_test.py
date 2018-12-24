import numpy as np

a = np.array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24]])

sub_shape = (3,3)
view_shape = tuple(np.subtract(a.shape, sub_shape) + 1) + sub_shape
strides = a.strides + a.strides
sub_matrices = np.lib.stride_tricks.as_strided(a,view_shape,strides)
print(sub_matrices)


def conv2d(a, f):
    s = f.shape + tuple(np.subtract(a.shape, f.shape) + 1)
    strd = np.lib.stride_tricks.as_strided
    subM = strd(a, shape = s, strides = a.strides * 2)
    return np.einsum('ij,ijkl->kl', f, subM)

a_padded = np.pad(a, 1, "constant")
print(conv2d(a_padded, np.array([[1,1,1], [1,0,1], [1,1,1]])))
