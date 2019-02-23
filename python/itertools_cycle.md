# itertools.cycle

受け取ったイテラブルの要素を無限に周期的に返すイテレータを返す。
```python
>>> a = [1, 2, 3, 4]
>>> cycle = itertools.cycle(a)
>>> for num in cycle:
>>>     print(num)
1
2
3
4
1
2
....
```
