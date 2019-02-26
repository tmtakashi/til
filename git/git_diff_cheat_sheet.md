# git diffチートシート

https://qiita.com/shibukk/items/8c9362a5bd399b9c56be

## git pullする前にリモートとの変更点を確認
```
git diff HEAD..リモート名/ブランチ名
```

## git pushする前にリモートとの変更点を確認
```
git diff リモート名/ブランチ名..HEAD
```

## git addする前に変更点を確認
```
git diff
```

## git addした後に変更点を確認
```
git diff --cached
```
