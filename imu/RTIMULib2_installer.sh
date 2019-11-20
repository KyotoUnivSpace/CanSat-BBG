#!/bin/sh

# これはMPU9250のセンサフュージョンを可能にするRTIMULib2のインストール用シェルスクリプトです．
# これを実行したディレクトリ上にライブラリをクローンし，ライブラリをビルド・インストールします．

cd $(dirname $0)

echo "環境構築中..."
sudo apt install cmake
sudo apt install python-dev

echo "GithubからRTIMULib2をクローンします"
git clone https://github.com/richards-tech/RTIMULib2.git

echo "ライブラリをコンパイルします"
cd RTIMULib2/Linux/RTIMULibCal
make -j4
sudo make install

echo "pythonラッパーをインストールします"
cd ../python
python3 setup.py build
sudo python3 setup.py install
