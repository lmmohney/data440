import numpy as np
import os 

PATH_DATA = 'data'

#File should contain code related to date nothing else 

def make_data(n: int=100, low: int=0, high: int=25) -> np.array:
    '''
    Return an nx2 array of random integers between low and high (inclusive)
    '''
    return np.random.randint(low=low, high=high+1, size=(n,2))

def save_data(data:np.array, filename:str) -> None: 
    '''
    Save a numpy array to the default output folder, ensuring folder exists 
    '''
    full_filename=os.path.join(PATH_DATA, filename)
    #Ensure output directory exists
    if not os.path.exists(PATH_DATA):
        os.mkdir(PATH_DATA)
    if type(data) != np.ndarray:
        raise TypeError(f'data should be a numpy array, but a {type(data)} was provided')
    
    #Dont overwrite 

if os.path.exists(full_filename): 
    raise FileExistsError (f'file {full_filename} already exists')

np.save(full_filename, data)

def load_data(file_name: str) -> np.ndarray: 
    '''
    load_data
    '''
    return np.load(os.path.join(PATH_DATA))
