#!/bin/sh

# これはMPU9250のセンサフュージョンを可能にするRTIMULib2のインストール用シェルスクリプトです．
# これを実行したディレクトリ上にライブラリをクローンし，ライブラリをビルド・インストールします．

sudo apt install cmake
sudo apt install python-dev

echo "--githubからRTIMULib2をクローンします---"
git clone https://github.com/richards-tech/RTIMULib2.git
cd RTIMULib2/Linux/RTIMULibCal
make -j4
sudo make install

cd ../python
python3 setup.py build
sudo python3 setup.py install
