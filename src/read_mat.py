import h5py
import numpy as np

filepath = './data/vessel_seg/data_cuhk/cen2export.mat'
arrays = {}
f = h5py.File(filepath)
for k, v in f.items():
    arrays[k] = np.array(v)

print(arrays)
