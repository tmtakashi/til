# np.random.RandomState.shuffle(x)

一定のシード状態で受けっとった配列をシャッフルする。
```python
>>> state = np.random.RandomState(seed=1)
>>> x = np.array([1, 2, 3, 4])
>>> state.shuffle(x)
>>> print(x) 
array([4, 3, 1, 2])
```
