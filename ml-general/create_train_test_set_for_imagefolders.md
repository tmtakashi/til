# クラスごとにフォルダ分けされたデータをtrain, testに分ける

```python

from pathlib import Path
import shutil
import random

random.seed(0)
test_size = 0.2

p = Path('.')

for class in class_list:
    # 元画像ディレクトリのパスオブジェクト
    raw_dir = p / 'data' / neta

    # 訓練データを格納するディレクトリ作成
    train_set = p / 'train_set' / neta
    train_set.mkdir(parents=True, exist_ok=True)

    # テストデータを格納するディレクトリ作成
    test_set = p / 'test_set' / neta
    test_set.mkdir(parents=True, exist_ok=True)

     # 各ブランドのの画像一覧取得
    imgs_path = list(raw_dir.iterdir())

    # 訓練データを格納
    for img in imgs_path[:int(len(imgs_path)*test_size)]:
        # 訓練画像をコピー
        shutil.copy(str(img), str(test_set.resolve()))

    # テストデータを格納
    for img in imgs_path[int(len(imgs_path)*test_size):]:
        # 訓練画像をコピー
        shutil.copy(str(img), str(train_set.resolve()))
```
