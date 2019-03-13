# Safe Navigation Operator（ぼっち演算子）
https://qiita.com/takaram/items/02dc68bf370cc3d8babb

メソッド呼び出しの.の前に&をつけておくと、レシーバーがnilのときにNoMethodErrorを投げずにnilを返してくれる機能
```ruby
str = nil
str&.upcase  #=>nil
```
