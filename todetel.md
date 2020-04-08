```python
def global_signal_regression(data4D: np.array, mask: np.array) -> np.array:
    x, y, z, time = data4D.shape
    g = np.zeros((time, 1))
    mask_bool = mask.astype(bool)
    for k in range(time):
        data_slice = data[:, :, :, k]
        g[k] = np.nanmean(data_slice[mask_bool])
    B = data.reshape(time, x*y*z)
    gt = (1 / (g.T @ g)) @ g.T
    Bgt = gt @ B
    return (B - g @ Bgt).reshape(x, y, z, time)
```
