## MacからBBGへのリアルタイムファイル同期

### 事前準備

1. 公開鍵認証でBBGにSSH接続できるように設定する．

   - 秘密鍵はローカル（Mac）の`~/.ssh/id_rsa`に保管すること．

2. brewでrsync（version 3.1以降）をインストール．

   `brew install rsync`

   - macの/usr/bin/rsyncはversion 2.6と古いため，lsyncdからの呼び出し時にエラーが発生する．

3. brewでlsyncdをインストール．

   `brew install lsyncd`

4. リモート（BBG）において，`sync`というディレクトリを作成．

   `mkdir ~/sync`

   - 以降，同期したいディレクトリはこの中に作成される．
   - `lsync.conf.lua`のtargetを書き換えることでこのディレクトリ名等は変更可能．

### 実行方法

1. BBGとMacをUSBで接続．
   （他の接続方法の場合は`lsync.conf.lua`内に記載のipアドレスに注意．）

2. ローカル（Mac）においてこのファイルのあるディレクトリに移動．

3. 以下のコマンドを実行して同期開始．

   `sudo lsyncd lsync.conf.lua `
