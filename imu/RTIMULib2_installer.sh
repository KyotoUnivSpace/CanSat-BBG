#!/bin/sh

# これはMPU9250のセンサフュージョンを可能にするRTIMULib2のインストール用シェルスクリプトです．
# これを実行したディレクトリ上にライブラリをクローンし，ライブラリをビルド・インストールします．

emecho() {
    echo "\e[1;35m$1\e[m"
}

cd $(dirname $0)

emecho "環境構築中..."
sudo apt install cmake
sudo apt install python-dev

emecho "GithubからRTIMULib2をクローンします"
git clone https://github.com/richards-tech/RTIMULib2.git

emecho "ライブラリをコンパイルします"
cd RTIMULib2/Linux/RTIMULibCal
make -j4
sudo make install

emecho "pythonラッパーをインストールします"
cd ../python
python3 setup.py build
sudo python3 setup.py install
