## itertools.islice

イテラブルから要素を選択して返すイテレータを作成
```python
list(itertools.islice(range(10), 7, None))
>>> [7, 8, 9]
```
`itertools.cycle`と組み合わせると
```python
list(itertools.islice(itertools.cycle(range(5)), 2, 9))
>>> [2, 3, 4, 0, 1, 2, 3]
```
