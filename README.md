![lu-logo-transparent-2](https://user-images.githubusercontent.com/26578616/56578738-41993380-65c6-11e9-897b-044ce963e21a.png)

# 18WSD030-Advanced-Project

Repository for my MEng Advanced Project.

*Diversity Techniques for riverside Wireless Sensor Nodes over Software Defined Radios*

**Project Description** 

This project will investigate the effectiveness of multiple antennas on wireless sensor nodes to improve radiofrequency reliability. Different diversity techniques will be investigated, and a suggestion as to which is the most suitable will be made. During the project, the student will model and measure a multiple input single output system. Firstly in a lab and secondly outdoors. The platform used will be software defined radios. 

**Project Aim** 

 To measure the effectiveness of using multiple antennas on sensor nodes close to, and upon water using software defined radios.
 
**Project Progress**

Set up test
 1. Carrier Wave detection Rx Target with Host interface

FM SISO 
 1. FM audio Tx Target (SISO)
 2. FM audio Rx Target and Host
 
FM SIMO 
 1. FM audio Rx Target and Host SIMO
 
LoRa (beyond project aim - further progress) 
 1. LoRa Rx on Target and Host with fosphor (waterfall)
 2. LoRa Tx on Target using Host generated IQ
 3. Arduino code for LoRa32 v2 Tx and RX
 4. LoRa Tx and Rx now works for targets and host - decoding not always successful
 
Experimental setup
1. Created three antenna mounts to test spatial and polarisation diversity
2. Data collected has also been included for completion

MATLAB code
1. Spectrum function that creates Power Density Dunction (PDF) to the input signal
2. SC,EGC,MRC - functions that perform Selection Combining, Maximal Ratio Combining and Equal Gain Combining to input signals 
3. Read and write complex binary files - this is to read from GNU Radio file sinks - code was taken from gr-utils

**Project Outcome**

Based on the results obtained the optimal arrangment for a 2-branch SIMO system is an antenna separion of a full wavelength (434MHz=>70 cm) with no antenna polirisation. MRC seems to be the best combining technique with EGC being the second best and SC the worst.

The effects of spatial diversity were very clear through out the set of measurments but the effects of polarisation diversity were inclusive. 

**Usage instructions**

The majority of the code developed for this project was done in GNU Radio companion and python. To use the above code, you will need to install GNU Radio it the Ettus USRP dependancies. 

GNU Radio is a free and open-source software development toolkit that provides signal processing blocks to implement software radios. GNU Radio can be installed by following the instructions here [https://wiki.gnuradio.org/index.php/InstallingGR]. 

If you are looking to implement the code using hardware (SDRs), you will have to install the appropriate libraries. The above code was developed to be used on the Ettus E310 USRP using the UHD library from Ettus [https://files.ettus.com/manual/page_build_guide.html]. 

After installing the required dependencies (explained above), you can download or clone the repository to your host machine. The file structure is simple. Code for Targets (SDRs) can be found in the /Targets folder. Please note that in my case the Target/1 is my *Rx* and Target/2 is my *Tx*. The differences between the two folders should be minimal. 

The /Host_Examples folder includes all the code written for the host computer. Host code will usually involve some kind of GUI for either real-time viewing of the data coming in or for controlling the setup or both. The GUI applications can be demanding, so my recommendation is to either use a Rasberry Pi or any other mid to high range computer running a recent version of Ubuntu. Using VMs can usually complicate things but haven't tested it. 

The /MATLAB folder includes the functions used to read, analyse and combine the IQ data obtained through the SDR. The functions are quite simple. They are fully document in the code. Please refer to that. Also note that the read and write_complex_binary functions were not developed by me. The come with a GNU Radio installation under gr-utils.

I am not sure if I will keep maintaining this after the end of the project but if any alterations are made they will be indicated here. 

**License**

All code developed and shared above is developed by me, Kyprianos Diamantides (unless stated otherwise above).

Copyright (C) 2018  K. Diamantides

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
