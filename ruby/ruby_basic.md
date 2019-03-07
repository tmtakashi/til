# Ruby基礎
## "Hello World"
```ruby
puts 'hello world!'
=> hello world
```
## 数値
```ruby
puts 22
=> 22
puts 2 + 9
=> 11
puts '2 + 9'
=> 2 + 9
```
## 文字列の連結
```ruby
puts 'hello' + 'world'
=> 'helloworld'
puts '39' + '19'
=> 3919
```

## 変数
```ruby
name = 'hoge'
puts name
=> home
```
## 変数展開
```ruby
name = 'John'
puts "My name is #{name}."
=> My name is John.
```
`puts`の後の囲いはダブルクオーテーション`""`である必要がある。シングルクオテーション`''`だと
```ruby
name = 'John'
puts 'My name is #{name}.'
=> My name is #{name}.
```
になってしまう。
```ruby
age = 22
puts 'I'm ' + age + ' years old.'
=> TypeError (String can't be coerced into Integer)
```
のようなトラブルを避けるために、文字列に変数を含めるときは基本的に変数展開を使う。

## 条件式

- if文

```ruby
score = 92
if score > 80
  puts 'High score!'
end
=> High score!
```

条件が単純な場合`puts "great! if score > 80`のようにもかける

- case文

```ruby
signal = gets.chomp # chompで改行コードを取り除く

case signal
when "red"
    puts "stop!"
when "green", "blue"
    puts "go!"
when "yellow"
    puts "caution!"
else
    puts 
end
```

## 破壊的メソッド
```ruby
name = "john"
puts name.upcase
=> JOHN
puts name
=> john
puts name.upcase!
=> JOHN
puts name
=> JOHN
```

## 真偽値
```ruby
puts name.empty?
=> false
puts name.include?("J")
=> true
```

## ハッシュ
```ruby
scores = {john: 100, bob: 200}
puts scores[:john]
=> 100
scores[:bob] = 600
puts scores
=> {:john => 100, :bob => 200}
puts scores.size
=> 2
puts scores.keys
=> [:john, :bob]
puts scores.values
=> [100, 200]
puts scores.has_key?(:john)
=> true
```

## 文字列 <=> 数値
```ruby
x = 50
y = "3"

puts x + y.to_i
=> 53
puts x + y.to_f
=> 53.0
puts x.to_s + y
=> "503"
```

## ハッシュ<=>配列
```ruby
scores = {taguchi: 200, fkoji: 400}
puts scores.to_a
=> [[:taguchi, 200], [:fkoji, 400]]
puts socres.to_a.to_h
=> {:taguchi=>200, :fkoji=>400}
```
## %記法
```ruby
puts "name: %s" % "taguchi"
=> "name: taguchi"
puts "name: %10s" % "taguchi"
=> name:    taguchi
puts 
```

エスケープシーケンスをバックスラッシュなしで記述できる

```ruby
puts %Q(he"llo) # ダブルクォーテーション
=> he"llo
puts %(he"llo) # 「Q」は省略可能
=> he"llo
puts #q(he'llo) # シングルクォーテーション
=> he`llo
```
文字列のみの配列を簡単にかける

```ruby
blue = "blue"
puts %W(red #{blue}) # 式展開有り
red
blue

puts %w(red #{blue})
red
#{blue}
```

## 書式付の値の埋め込み

文字列

```ruby
puts "name: %s" % "taguchi"
=> "name: taguchi"
puts "name: %10s" % "taguchi"
=> "name:    taguchi"
puts "name: %-10s" % "taguchi"
=> "name: taguchi     "
```

数値

```ruby
puts "id:%05d, rate:%10.2f" % [355, 3.284] #10.2f: 全体が10桁、小数点以下が2桁
=> id:00355, rate:      3.28
````

`printf`

```ruby
printf("name: %10s\n", "taguchi")
printf("id:%05d, rate:%10.2f", 355, 3.284)
=> name:    taguchi
id:00355, rate:      3.28
```

`sprintf`: printせずに文字列を返す
```ruby
p sprintf("name: %10s\n", "taguchi")
p sprintf("id:%05d, rate:%10.2f", 355, 3.284)
=> name:    taguchi
id:00355, rate:      3.28
```

## 標準入力
```ruby
score = gets # 文字列を受け取る
```

## 繰り返し

- while

```ruby
i = 0

while i < 10 do
    puts "hello"
    i += 1
end
```

- times

```ruby
10.times do |i|
  puts "#{i}: hello"
end
```

```ruby
10.times { |i| puts "#{i}: hello" }
```

- for

```ruby
for i in 15..20
    puts i
end
=> 15
16
17
18
19
20

for color in ["red", "blue"]
    puts color
end
=> red
blue

for name, score in {taguchi:200, fkoji:400} do
    puts "#{name}: #{score}"
end
=> taguchi: 200
fkoji: 400
```

- each
```ruby
(15..20).each do |i|
    p i
end
=> 15
16
17
18
19
20

{taguch: 200, fkoji:400}.each do |name, score|
    puts "#{name}: #{score}"
end
=> taguch: 200
fkoji: 400
```

- loop
```ruby
i = 0
loop do
    p i
    i += 1
end
```

- break, next
```ruby
10.times do |i|
    if i == 7
        break
    end
    puts i 
end
=> 0
1
2
3
4
5
6

10.times do |i|
    if i == 7
        next
    end
    puts i 
end
=> 0
1
2
3
4
5
6
8
9
```

## メソッド
```ruby
def sayHi(name = 'tom')
    puts "hi! #{name}"
end

sayHi("Takashi")
sayHi
=> hi! Takashi
hi! tom
```

## クラス

```ruby
class User
    def name=(name) # セッター
        @name = name
    end
    def name # ゲッター
        @name
    end
end
```
```ruby
class User
    # セッターとゲッターを同時に定義
    attr_accessor :name, :address, :email
end
```
```ruby
# メソッドからメソッドを使う
class User
    # セッターとゲッターを同時に定義
    attr_accessor :name, :address, :email

    def profile
        "#{name}(#{address})"
    end
end
```

```ruby
# クラスメソッド
class User
    attr_accessor :name

    def initialize(name)
        @name = name
    end

    def sayHi
        puts "hi! i am #{self.name}"
    end

    def self.info
        puts "User class"
    end
end

User.info
=> User class
```

```ruby
# クラス変数
class User
    @@count = 0
    
    attr_accessor :name

    def initialize(name)
        @@count += 1
        @name = name
    end

    def sayHi
        puts "hi! i am #{self.name}"
    end

    def self.info
        puts "User class"
    end
end

User.info
=> User class
```

```ruby
# クラス変数
class User
    @@count = 0

    attr_accessor :name

    def initialize(name)
        @@count += 1
        @name = name
    end

    def sayHi
        puts "hi! i am #{self.name}"
    end

    def self.info
        puts "User class #{@@count} instances."
    end
end

tom = User.new("tom")
bob = User.new("tom")

User.info
=> User class 2 instances.
```

```ruby
# 定数
class User
    @@count = 0
    
    attr_accessor :name
    
    VERSION = 1.1
    def initialize(name)
        @@count += 1
        @name = name
    end

    def sayHi
        puts "hi! i am #{self.name}"
    end

    def self.info
        puts "#{VERSION}: User class #{@@count} instances."
    end
end

tom = User.new("tom")
bob = User.new("tom")

User.info
puts  User::VERSION
=> 1.1: User class 2 instances.
1.1
```

```ruby
# 継承
class User
    
    def initialize(name)
        @name = name
    end

    def sayHi
        puts "hi! i am #{@name}"
    end

end

class AdminUser < User
    def sayHello
        puts "Hello from #{@name}"
    end
end

tom = AdminUser.new("tom")
tom.sayHi
tom.sayHello
=> hi! i am tom
Hello from tom
```

```ruby
# アクセス権
class User

    private
      def sayPrivate
          puts "hi! i am #{@name}"
      end

end

User.new.sayPrivate
=> ruby_practice.rb:20:in `<main>': private method `sayPrivate' called for #<User:0x007fee07990e60 @name="tom"> (NoMethodError)

class User
    
    def sayHi
        puts "hi!"
        sayPrivate
    end

    private
      def sayPrivate
          puts "hi!"
      end

end

class AdminUser < User
    def sayHello
        puts "Hello from #{@name}"
    end
end

User.new.sayHi
=> hi!
hi!
```

## モジュール
```ruby
module Movie

    VERSION = 1.1

    def self.encode
        puts "encoding..."
    end

    def self.export
        puts "exporting..."
    end
end

Movie.encode
Movie.export

puts Movie::VERSION
=> encoding...
exporting...
1.1
```

## ミックスイン
```ruby
module Debug

    def info
        puts "#{self.class} debug info ..."
    end

end

class Player
    include Debug
end

class Monster
    include Debug
end

Player.new.info
Monster.new.info
```

## 例外
```ruby
x = gets.to_i

begin
    p 100 / x
rescue => ex
    p ex.message
    p ex.class
    puts "stopped"
ensure
    puts "--END--"
end
=> 0
"divided by 0"
ZeroDivisionError
stopped
--END--
```
