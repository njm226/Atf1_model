#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:16:19 2019
histogramm and timecourse data
@author: fabio
"""


import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#from smaller_model_function_AtoU import simple_small as ss
from AtoU_model import simple as ss
import multiprocessing
#import time
import pickle
pool = multiprocessing.Pool(multiprocessing.cpu_count())



X_Y_atf1_on=[[182,49,120,0]] #X_Y_atf1_on=[[182,49,130,0]]
X_Y_atf1_off=[[182,49,120,1]] #X_Y_atf1_off=[[182,49,130,1]]
#X_Y_atf1_one_on=[[182,49,120,2]] #X_Y_atf1_off=[[182,49,130,1]]


reps=10000

repeat=reps*X_Y_atf1_on
repeat_sm=reps*X_Y_atf1_off
#repeat_m=reps*X_Y_atf1_one_on

duration=201

if __name__ == '__main__':
    status_small = pool.map(ss, repeat) 
    status_m = pool.map(ss, repeat_sm) 
    

#small system
reporters_diff_small = np.zeros([len(repeat),duration])
reporters_off_small = np.zeros([len(repeat),duration])
reporters_on_small = np.zeros([len(repeat),duration])


cenH_list_small = np.zeros([len(repeat),duration])
EcoRV_list_small = np.zeros([len(repeat),duration])



#medium system
reporters_diff_m = np.zeros([len(repeat),duration])
reporters_off_m = np.zeros([len(repeat),duration])
reporters_on_m = np.zeros([len(repeat),duration])


cenH_list_m = np.zeros([len(repeat),duration])
EcoRV_list_m = np.zeros([len(repeat),duration])


#medium system
reporters_diff_m = np.zeros([len(repeat),duration])
reporters_off_m = np.zeros([len(repeat),duration])
reporters_on_m = np.zeros([len(repeat),duration])


cenH_list_m = np.zeros([len(repeat),duration])
EcoRV_list_m = np.zeros([len(repeat),duration])




for elt in range(len(repeat)):
    
    cenH_small = np.array(status_small[elt][0])
    EcoRV_small = np.array(status_small[elt][1])
    
    
    
    # generate list with cenH and EcoRV states being both at different states (1)
    reporter_diff_small = cenH_small != EcoRV_small
    #transform that vector into a int vector
    reporter_diff_small = reporter_diff_small.astype(int)
    # copy this vector into reporter_states vector
    reporters_diff_small[elt]=reporter_diff_small
    
    
    
    # generate list with cenH and EcoRV states being both switched off
    reporter_off_small = np.zeros(len(cenH_small),'int')
    for index in range(len(cenH_small)):
        if cenH_small[index]==1 and EcoRV_small[index]==1:
            reporter_off_small[index]=1
        else:
            reporter_off_small[index]=0
            
    reporters_off_small[elt]=reporter_off_small
    
    
    
    # generate list with cenH and EcoRV states being both switched on
    reporter_on_small = np.zeros(len(cenH_small),'int')
    for Index in range(len(cenH_small)):
        if cenH_small[Index]==0 and EcoRV_small[Index]==0:
            reporter_on_small[Index]=1
        else:
            reporter_on_small[Index]=0
            
    reporters_on_small[elt]=reporter_on_small
    
    
    #switch the values of the list (1 stands now for timepoint when reporter is on)
    cenH_small=1-cenH_small
    EcoRV_small=1-EcoRV_small
    
    cenH_list_small[elt]=cenH_small
    EcoRV_list_small[elt]=EcoRV_small
    
    
    
    
    
    
    
    
    cenH_m = np.array(status_m[elt][0])
    EcoRV_m = np.array(status_m[elt][1])
    
    
    
    # generate list with cenH and EcoRV states being both at different states (1)
    reporter_diff_m = cenH_m != EcoRV_m
    #transform that vector into a int vector
    reporter_diff_m = reporter_diff_m.astype(int)
    # copy this vector into reporter_states vector
    reporters_diff_m[elt]=reporter_diff_m
    
    
    # generate list with cenH and EcoRV states being both switched off
    reporter_off_m = np.zeros(len(cenH_m),'int')
    for index in range(len(cenH_m)):
        if cenH_m[index]==1 and EcoRV_m[index]==1:
            reporter_off_m[index]=1
        else:
            reporter_off_m[index]=0
            
    reporters_off_m[elt]=reporter_off_m
    
    
    # generate list with cenH and EcoRV states being both switched on
    reporter_on_m = np.zeros(len(cenH_m),'int')
    for Index in range(len(cenH_m)):
        if cenH_m[Index]==0 and EcoRV_m[Index]==0:
            reporter_on_m[Index]=1
        else:
            reporter_on_m[Index]=0
            
    reporters_on_m[elt]=reporter_on_m
    
    #switch the values of the list (1 stands now for timepoint when reporter is on)
    cenH_m=1-cenH_m
    EcoRV_m=1-EcoRV_m
    
    cenH_list_m[elt]=cenH_m
    EcoRV_list_m[elt]=EcoRV_m
    
    
    print(cenH_small)
    print(cenH_m)
    
    

diff_small = (sum(reporters_diff_small))/reps
off_small = (sum(reporters_off_small))/reps
on_small = (sum(reporters_on_small))/reps




diff_m = (sum(reporters_diff_m))/reps
off_m = (sum(reporters_off_m))/reps
on_m = (sum(reporters_on_m))/reps







#output
cenH_total_small = (sum(cenH_list_small))/reps
#
EcoRV_total_small = (sum(EcoRV_list_small))/reps




cenH_total_m = (sum(cenH_list_m))/reps
#
EcoRV_total_m = (sum(EcoRV_list_m))/reps


    
# save state_list
with open('AtoU_Atf1_on_S30_AtoU_49_UtoM_120_without_single_atf1_KO.txt', 'wb') as F:
    pickle.dump(EcoRV_total_small, F)
    
# save state_list
with open('AtoU_Atf1_off_S30_AtoU_49_UtoM_120_without_single_atf1_KO.txt', 'wb') as F:
    pickle.dump(EcoRV_total_m, F)
    

    

time = np.array(range(duration))

y_axis = np.array([cenH_total_small, EcoRV_total_small,  cenH_total_m, EcoRV_total_m])
        
#fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=((36, 12)))
fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=((15, 10)))
#default line colors and styles
ax1.plot(time,EcoRV_total_small, color='yellowgreen', label='mCherry both atf1-sites on (4.5 kb)')
ax1.plot(time,cenH_total_small, color='cyan', label='cenH both atf1-sites on(4.5 kb)')
ax1.plot(time,EcoRV_total_m, color='black', label='mCherry both atf1-sites off (4.5 kb)')
#ax1.plot(time,cenH_total_m,'ro', label='cenH 24 kb region')
ax1.legend(loc='upper left')
#ax1.set_ylabel("fraction of 'ON' cells", fontsize = 35)  
#ax1.set_xlabel('t (generations)', fontsize = 35)  
ax1.set_yscale('log')    
ax1.tick_params(labelsize='30')
ax1.set_ylim([0.001,1])
ax1.set_xlim([1,200])
ax1.legend(fontsize='25')

plt.savefig("AtoU_Atf1_S30_AtoU_49_UtoM_120_without_single_atf1_KO.pdf")
    

# #fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=((36, 12)))
# fig, (ax1) = plt.subplots(nrows=1, ncols=1, figsize=((12, 10)))
# #default line colors and styles
# ax1.plot(time,EcoRV_total_small, color='yellowgreen', label='EcoRV 20 kb region')
# ax1.plot(time,cenH_total_small, color='cyan', label='cenH 20 kb region')
# ax1.plot(time,EcoRV_total_m, color='red', label='EcoRV 24 kb region')
# #ax1.plot(time,cenH_total_m,'ro', label='cenH 24 kb region')
# ax1.plot(time,EcoRV_total_large, color='black', label='EcoRV 26 kb region')
# #ax1.plot(time,cenH_total_large, color='blue', label='cenH 26 kb region')
# ax1.plot(time,EcoRV_total_max, color='gold', label='EcoRV 28 kb region')
# #ax1.plot(time,cenH_total_max, color='purple', label='cenH 28 kb region')
# #ax1.set_title('Combined debt growth over time')
# #ax1.legend(loc='upper left')
# ax1.set_ylabel('fraction of ''ON'' cells', fontsize = 25)  
# ax1.set_xlabel('t (generations)', fontsize = 25)  
# ax1.set_yscale('log')    
# ax1.tick_params(labelsize='18')
# ax1.set_ylim([0.01,1])
# ax1.set_xlim([1,46])
# ax1.legend(fontsize='20')

#plt.savefig("timecourse_small_SUS350")

# ax2.plot(time, off_small, color='k')
# ax2.plot(time, on_small, color='b')
# ax2.plot(time, diff_small, color='r')
# #ax1.set_title('Combined debt growth over time')
# #ax1.legend(loc='upper left')
# ax2.set_ylabel('fraction of cells (small system)', fontsize = 26)  
# ax2.set_xlabel('t (generations)', fontsize = 25)   
# ax2.tick_params(labelsize='18') 
# ax2.set_ylim([0,1])
# ax2.set_xlim([1,100])

# ax3.plot(time, off_large, color='k')
# ax3.plot(time, on_large, color='b')
# ax3.plot(time, diff_large, color='r')
# #ax1.set_title('Combined debt growth over time')
# #ax1.legend(loc='upper left')
# ax3.set_ylabel('fraction of cells (large system)', fontsize = 25)  
# ax3.set_xlabel('t (generations)', fontsize = 25)   
# ax3.tick_params(labelsize='18') 
# ax3.set_ylim([0,1])
# ax3.set_xlim([1,100])

















