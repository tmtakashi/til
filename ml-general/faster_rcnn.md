# Faster R-CNNまとめ
http://nonbiri-tereka.hatenablog.com/entry/2018/03/07/075835
## 全体構成
1. Conv Layerで特徴マップを得る
2. Region Proposal Network(RPN)で領域(Region of Interest, RoI)を抽出する
3. Conv Layerで得られた特徴マップをRoIで切り出す
4. 切り出した領域を分類する
![](https://cdn-ak.f.st-hatena.com/images/fotolife/t/tereka/20180303/20180303132456.png)

## Region Proposal Network

### 概要・目的
- 物体領域の候補を計算
- End-to-Endな処理によって高速化
処理の流れ
1. 物体の候補領域を見つけるAnchorの生成
2. 学習のための誤差を計算
3. 候補の中からNMSを用いて有効な領域を絞る

#### Anchor
Anchorと物体のIoU(Intersection over Union)が0.7以上 => 物体が存在(Positive anchor)

Anchorと物体のIoUが0.3以下 => 物体が存在しない(Negative anchor)

これら以外は学習に貢献しない

#### Non-maximum Supression(NMS)
同じ物体を示している領域の抽出を行う

#### Rol Pooling
可変長である抽出RoIを分類ネットワークに入力できるように固定次元に変換
