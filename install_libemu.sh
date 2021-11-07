# Filename: install_libemu.sh
# Author: David Alvarez Robles (km0xu95)
# Website: https://blog.asturhackers.es

# Purpose: This script was developed in order to install libemu on a fresh
# Ubuntu operating system installation

apt-get install git autoconf libtool
git clone https://github.com/buffer/libemu
cd libemu
autoreconf -v -i
./configure --prefix=/opt/libemu; make install
cd tools/sctest
make
