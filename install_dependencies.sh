#!/bin/bash

##################################################
#########       INSTALL  LIBRARIES       #########
##################################################
cd

add-apt-repository ppa:team-gcc-arm-embedded/ppa
apt-get update

apt install -y python3-pip gcc-arm-embedded git python-minimal

pip3 install numpy scipy matplotlib sympy jupyterlab


##################################################
#########         BUILD FIRMWARE         #########
##################################################

cd
git clone --recursive https://github.com/irom-lab/crazyflie-firmware
cd crazyflie-firmware
make

##################################################
#########        CLONE  NOTEBOOKS        #########
##################################################

cd
git clone https://github.com/irom-lab/MAE345-Student
