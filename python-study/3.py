#***   リスト型(list)   ***
#他のプログラミング言語同様,Pythonにも複数の要素(数や文字列を内包するデータ型があります.
#その1つがリストと呼ばれるものです.

#リストはコンマ(,)区切りの要素を角括弧[]で囲んで作る.
squares = [1, 4, 9, 16, 25]
print(squares)
#[1, 4, 9, 16, 25]

#文字列と同様に, リストにもインデックスやスライス表記がある.
#文字列と同じくインデックスは0番目から始まる.
#0番目の要素を取り出す
print(squares[0])
#1
#最終要素を取り出す
print(squares[-1])
#25
#2番目の要素から最後の要素まで取り出す.
print(squares[2:])
#[9, 16, 25]


#リストに別のリストを連結するときは+を利用する.
print(squares + [36, 49, 64, 81, 100])
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#文字列と違って, リストは要素の変更が可能.
#3番目の要素を間違えてしまった！
cubes = [1, 8, 27, 65, 125]
print(cubes)
#[1, 8, 27, 65, 125]

#正しくは4の3乗
cubes[3] = 4 ** 3
print(cubes)
#[1, 8, 27, 64, 125]

#リストの変数名の後ろに.append(x)と記述することで,
#リストの末尾に新しい要素xを追加することができる.
cubes.append(6 ** 3)
cubes.append(7 ** 3)
print(cubes)
#[1, 8, 27, 64, 125, 216, 343]

#スライスに代入することができる.
#また, スライスを使ってリストの要素数の変更や, 要素を削除することができる.
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)
#['a', 'b', 'c', 'd', 'e', 'f', 'g']

#2番目から4番目を書き換える
letters[2:5] = ["C", "D", "E"]
print(letters)
#['a', 'b', 'C', 'D', 'E', 'f', 'g']

#2番目から4番目を削除する
letters[2:5] = []
print(letters)
#['a', 'b', 'f', 'g']

#リストの要素を全て削除する(空リストを作る).
letters[:] = []
print(letters)
#[]

#全ての要素削除することはリストの変数名.clear()でも同じことができる.
letters = ["a", "b", "c", "d", "e", "f", "g"]
letters.clear()
print(letters)
#[]

#len()関数を用いてリストの要素数を取得(出力)することができる.
letters = ["a", "b", "c", "d"]
print(len(letters))
