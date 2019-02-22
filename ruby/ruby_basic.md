# Ruby基礎
## "Hello World"
```ruby
puts 'hello world!'
>>> hello world
```
## 数値
```ruby
puts 22
>>> 22
puts 2 + 9
>>> 11
puts '2 + 9'
>>> 2 + 9
```
## 文字列の連結
```ruby
puts 'hello' + 'world'
>>> 'helloworld'
puts '39' + '19'
>>> 3919
```

## 変数
```ruby
name = 'hoge'
puts name
>>> home
```
## 変数展開
```ruby
name = 'John'
puts "My name is #{name}."
>>> My name is John.
```
`puts`の後の囲いはダブルクオーテーション`""`である必要がある。シングルクオテーション`''`だと
```ruby
name = 'John'
puts 'My name is #{name}.'
>>> My name is #{name}.
```
になってしまう。
```ruby
age = 22
puts 'I'm ' + age + ' years old.'
>>> TypeError (String can't be coerced into Integer)
```
のようなトラブルを避けるために、文字列に変数を含めるときは基本的に変数展開を使う。

## 条件式
```ruby
score = 92
if score > 80
  puts 'High score!'
end
```

