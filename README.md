# MAE345-Student
Source code assignments for MAE345.

This repository contains Jupyter notebook assignments for Princeton's MAE345 class. It is organized in the following manner:

- All Jupyter notebooks are placed in the top level directory so they have access to all other Python modules and paths referenced in them are consistent.
- All data provided / collected for use in assignments resides in `quad_data`.
- The script `install_dependencies.sh` will install the necessary dependencies for running the software for the class on a fresh Ubuntu 18.04 installation. It will also build the firmware for the Bitcraze Crazyflie 2.1 we have modified for the class that is available from [this repository](https://github.com/irom-lab/crazyflie-firmware).

# Virtual Box

For those not used to using with Python and Linux, we are providing a Virtual Box image that already has the software and libraries installed for working with the Crazyflie. While you can complete the assignments with your own OS / environment, the instructors will not be able to provide help for technical issues you may run into with your own setup. To that end, we encourage using the Virtual Box image.

## Setting Up

To use the image, complete the following instructions:

1. Download and install [Virtual Box](https://www.virtualbox.org/) for your OS.
2. Download the [OVA image](https://drive.google.com/file/d/1SMuKvwyBaQGdplbzOviqDJTqrKvKpgVu/view?usp=sharing) from our Google Drive.
3. Open Virtual Box. Click on `File -> Import Appliance`. Select the OVA image file you downloaded and hit `Next >`. On the next screen do not alter any of the options, simply hit `Import`.

If you are using Linux with secure boot enabled, you may need to go through some extra steps [(see here)](https://askubuntu.com/questions/920689/how-to-fix-modprobe-vboxdrv-error-in-virtualbox?fbclid=IwAR0N6lNVvzv54pQLpqGNtzaIWDqGXNTAL1bbzOIl_DlXxRaNniyxcCySsuw). You will also need to add yourself to the Virtual Box user group on your host machine by running the command `
sudo usermod -aG vboxusers $USER` in your terminal and restarting your machine. Contact the TAs if you need help.

You can start the virtual machine by double clicking it in the menu. Once it boots, the password for the account `mae345` (the only account) is, again, `mae345`.

## Working on Assignments

To work on an assignment, open the `Terminal` application. Enter the command `cd MAE345-Student` followed by the command `git pull`, which will update the code to the latest made available by the instructors. Then, enter `jupyter notebook`. This will open the Jupyter interface in your web browser, where you will work on your Python assignments. Then click on `LabX.py`, where `X` is the assignment number and fill out the specified cells in the notebook. Submission instructions are inside each notebook.

## Accessing New and Updated Assignments

Throughout the course, we will be adding more assignments to this Git repository. The instructors may also need to issue corrections to labs while they are assigned. To update the codebase on your computer, run the command `git fetch --all
 && git reset --hard origin/master`. **THIS COMMAND WILL OVERWRITE THE ASSIGNMENTS YOU HAVE IN THE FOLDER.** If you want to backup an assignment, copy it to your home directory with the command `cp <filename> ~/` first.
