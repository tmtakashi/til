# 配列内のN番目に大きい値のインデックスを取得する

```python
>>> a = np.array([1, 3, 2])
>>> np.argsort(a)
array([0, 2, 1])
>>> N = 2
>>> a[np.argsort(a)[N-1]]
2
```
