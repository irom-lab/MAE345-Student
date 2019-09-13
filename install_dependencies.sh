#!/bin/bash

##################################################
#########       INSTALL  LIBRARIES       #########
##################################################
cd

add-apt-repository ppa:team-gcc-arm-embedded/ppa
apt-get update

apt install -y python3 python3-pip gcc-arm-embedded git python-minimal python3-pyqt5 python3-pyqt5.qtsvg

pip3 install numpy scipy matplotlib sympy jupyterlab


##################################################
#########         BUILD FIRMWARE         #########
##################################################

cd
git clone --recursive https://github.com/irom-lab/crazyflie-firmware
cd crazyflie-firmware
make

##################################################
#########        INSTALL CFCLIENT        #########
##################################################

cd
git clone https://github.com/bitcraze/crazyflie-clients-python.git
cd crazyflie-clients-python
pip3 install -e .

##################################################
#########        CLONE  NOTEBOOKS        #########
##################################################

cd
git clone https://github.com/irom-lab/MAE345-Student
