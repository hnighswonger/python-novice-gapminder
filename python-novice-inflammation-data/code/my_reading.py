import sys
import numpy as np

def compute_mean(data):
    
    mean = np.mean(data)
    print('The computed mean is: ', mean)

def compute_max(data):
    pass

def compute_min(data):
    pass

def load_data(filename):
    data = np.loadtxt(fname=filename, delimiter=',')
    assert isinstance(data, np.ndarray)
    return data

def main():
    
    action = sys.argv[1]
    assert action in ['--mean','--min','--max'], 'Invalid action'
    for filename in sys.argv[2:]:
        assert isinstance(filename, str)
        assert filename[-4:] == '.csv'
    
    for filename in sys.argv[2:]:
        
        data = load_data(filename)
    
        if action == '--mean':
            result = compute_mean(data)
        elif action == '--max':
            result = compute_max(data)
        elif action == '--min':
            result = compute_min(data)

if __name__ == '__main__':
    main()
