# Faster R-CNNまとめ
http://nonbiri-tereka.hatenablog.com/entry/2018/03/07/075835

https://qiita.com/arutema47/items/8ff629a1516f7fd485f9

https://qiita.com/yu4u/items/5cbe9db166a5d72f9eb8

## 全体構成
1. Conv Layerで特徴マップを得る
2. Region Proposal Network(RPN)で領域(Region of Interest, RoI)を抽出する
3. Conv Layerで得られた特徴マップをRoIで切り出す
4. 切り出した領域を分類する
![](https://cdn-ak.f.st-hatena.com/images/fotolife/t/tereka/20180303/20180303132456.png)

一枚の画像の推論時間

Fast R-CNN:2.3秒

Faster R-CNN:0.2秒

## Region Proposal Network

### 概要・目的
- 物体領域の候補を計算
- End-to-Endな処理によって高速化
- 3~4層ほどのCNNで構成可能
処理の流れ
1. 物体の候補領域を見つけるAnchorの生成
2. 学習のための誤差を計算
3. 候補の中からNMSを用いて有効な領域を絞る

#### Anchor
Anchorと物体のIoU(Intersection over Union)が0.7以上 => 物体が存在(Positive anchor)

Anchorと物体のIoUが0.3以下 => 物体が存在しない(Negative anchor)

これら以外は学習に貢献しない
![](https://camo.qiitausercontent.com/bc1839c4c56095cdb9ccfdedb02f419a7cd3af67/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3137313931352f34646538303631372d313462372d653937302d663130382d6531383366306231646133342e706e67)
- 一箇所につきk個のBindingBoxを提案。だいたい`k=128`が多い

#### Non-maximum Supression(NMS)
- IoUの閾値を決めて、同じ物体を示している領域の抽出を行う。
- IoUが小さい領域は削除する

#### Rol Pooling
可変長である抽出RoIを分類ネットワークに入力できるように固定次元の特徴マップに変換 
![](https://camo.qiitausercontent.com/8cf05cf36d952981add1dbf70b0cafa01731adfe/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3133393830392f63383161356163372d663135392d303835382d653162642d6537326664343262646363392e706e67)

元画像のRegion Proposalの領域をfeature map上に投影すると、feature mapとサブピクセルレベルのズレが生じる。

よって以下の処理を施す。（3x3のfeature mapを得たいとする）
![](https://camo.qiitausercontent.com/ab088881a617422c99b40610f357cad4ac0037b7/68747470733a2f2f71696974612d696d6167652d73746f72652e73332e616d617a6f6e6177732e636f6d2f302f3133393830392f39616366363937312d363263332d383265312d656136312d3562613062623736393862312e706e67)
1. Region Proposalの座標を整数値に丸め込み、赤い外接矩形を得る。
2. 得たいfeature mapのサイズと同じビン数で分割
3. 元のfeature map内のピクセルを3x3のビンのいずれかに割り当て、maxやaverageを取る。
