import matplotlib.pyplot as plt 
import numpy as np 
import os 

PATH_FIGURES= 'figures'

#This file shpuld contain code that makes figures, and does nothing else 

def make_figrue(data: np.ndarray, file_name:str) ->None: 
    '''Inputs
    '''
    full_filename= os.path.join(PATH_FIGURES, file_name)

    if not os.path.exists(PATH_FIGURES): 
        os.mkdir(PATH_FIGURES)

    plt.figure(figsize=(6,6))
    plt.scatter(data[:,0], datra[;,a])
    plt.savefig()