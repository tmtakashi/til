# addEventListenerでボタンに機能をつける

HTML
```html
<!DOCTYPE html>
<html>
<body>
    <div id="btn">Click</div>
</body>
</html>
```

JS
```javascript
'use strict';
{
    const btn = document.getElementById('btn');
    btn.addEventListener('click', () => {
        const results = ['大吉', '中吉', '凶', '末吉'];
        const n = Math.floor(Math.random() * results.length);
        btn.textContent = results[n]; 
    });
}
```
1. `document.getElementById`などで要素を変数`btn`に格納
2. 格納した変数`btn`に`addEventLister`を設定
    
    - `btn.addEventListener(操作, アロー関数);`