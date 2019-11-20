# CanSat
これはカンサットのビーグルボーン用のレポジトリになります。

## 環境構築

### Python
Python2.7を使うこと

### I2C出力
I2Cで通信するための準備をします
1. センサ  
   `sudo sh -c "echo BB-I2C1 > /sys/devices/platform/bone_capemgr/slots"`
2. サーボドライバ  
   `sudo sh -c "echo BB-I2C2 > /sys/devices/platform/bone_capemgr/slots"`

### センサフュージョン
1. `cd ./imu`
2. `sudo sh RTIMULib2_installer.sh`

### 時計合わせ
http://hatcy840.hatenablog.com/entry/2013/09/17/001212

### 無線LAN
BBGにWiFiドングルを付けたときの設定方法
普通のlinuxやRaspberry Piとは違って`connmanctl`なるものを使う。

#### パーソナル
1. `sudo connmanctl`  
    デバイスの認識を確認するには`iwconfig`して、これにwlan0とかで表示されていてばたぶんデバイスの認識はされている。これができなければ重症。ググってなんとかして認識させる。普通は`/etc/network/interfaces`に設定を書くらしいが、BBBの場合ここにコメントアウトされた状態で`connmanctl`を使えと書かれている。そのため`connmanctl`を使う。
2. `enable wifi`  
    Enabled wifiが出ればOK
3. `scan wifi`  
    Scan completed for wifiが出ればOK
4. `services`  
    サービスの一覧が出る。もしつなぎたいアクセスポイントがなければもう一度scanする
5. `agent on`  
    Agent registered が出ればOK
6. `connect (servicesで表示された右側の長い名前)`  
    パスワードを聞いてきたらOK、打ち込んでConnectedとかでたらOK
7. `quit`  
    これで`ifconfig`なり`iwconfig`なりをしてIPアドレスがとれていたらOK

#### エンタープライズ
https://wiki.archlinux.jp/index.php/WPA2_Enterprise
詳細はSlackのsoftwareチャネルを参照してください

## リモートリポジトリのルール
developブランチ(マスターブランチから切ったブランチ)からブランチを分けて開発し、マージしていくという感じにします。  
**作業する前に必ずdevelopブランチからプルしてください**

### 手順

#### ブランチ
まず、ブランチを切ります。「[機能名]\_[名前]」というブランチ名を命名してください。

#### プルリク
そのあと、プルリクを書きましょう。その際の命名方法は、「[状態]/[機能]/[名前]」で書きましょう。  
[状態]には、[作業中]、[承認待ち]のどちらかを入れてください。  
例：「[承認待ち]/サーボ機能改善/山田太郎」

### GitHubとは？
- https://qiita.com/nnahito/items/565f8755e70c51532459
- github for desktopというのもお勧めです。。。  
https://qiita.com/yukiyan/items/2ea3dc5813fdba5d9cd2

## 便利コマンド

### rsync
BBGとPC間のファイル転送に利用するとよい

#### エイリアスの例
```bash
rsyncbbgs='(){rsync -avcz $1 debian@192.168.6.2:~/$2}'
rsyncbbg='(){rsync -avcz debian@192.168.6.2:~/$1 $2}'
```

### lsyncd
BBGとPC間のファイル自動同期  
`./lsync-tools/README.md`を参照すること

