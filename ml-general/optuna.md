# Optunaの使い方

https://qiita.com/ryota717/items/28e2167ea69bee7e250d

## インストール
`pip install optuna`

## モデルの定義

```python
def create_model(num_layer, activation, mid_units, num_filters):
    """
    num_layer : 畳込み層の数
    activation : 活性化関数
    mid_units : FC層のユニット数
    num_filters : 各畳込み層のフィルタ数
    """
    inputs = Input((28,28,1))
    x = Convolution2D(filters=num_filters[0], kernel_size=(3,3), padding="same", activation=activation)(inputs)
    for i in range(1,num_layer):
        x = Convolution2D(filters=num_filters[i], kernel_size=(3,3), padding="same", activation=activation)(x)

    x = GlobalAveragePooling2D()(x)
    x = Dense(units=mid_units, activation=activation)(x)
    x = Dense(units=10, activation="softmax")(x)

    model = Model(inputs=inputs, outputs=x)
    return model
```

## 目的関数の設定
```python
def objective(trial):
    #セッションのクリア
    K.clear_session()

    #最適化するパラメータの設定
    #畳込み層の数
    num_layer = trial.suggest_int("num_layer", 3, 7)

    #FC層のユニット数
    mid_units = int(trial.suggest_discrete_uniform("mid_units", 100, 500, 100))

    #各畳込み層のフィルタ数
    num_filters = [int(trial.suggest_discrete_uniform("num_filter_"+str(i), 16, 128, 16)) for i in range(num_layer)]

    #活性化関数
    activation = trial.suggest_categorical("activation", ["relu", "sigmoid", "tanh"])

    #optimizer
    optimizer = trial.suggest_categorical("optimizer", ["sgd", "adam", "rmsprop"])

    model = create_model(num_layer, activation, mid_units, num_filters)
    model.compile(optimizer=optimizer,
          loss="categorical_crossentropy",
          metrics=["accuracy"])

    history = model.fit(train_x, train_y, verbose=0, epochs=5, batch_size=128, validation_split=0.1)

    # 最小化問題を解くので(1 - accuracy)を返す
    return 1 - history.history["val_acc"][-1]
```


## study objectの作成、最適化の実行
```python
import optuna

study = optuna.create_study()
study.optimize(objective, n_trials=100)
```

## 
