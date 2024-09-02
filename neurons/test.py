import sys
import os

# Add the project root directory to sys.path
sys.path.append('/Users/muhammadabdullahshahid/p3.10/test-travelling-salesman-problem-main')
#print(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import tqdm

from neurons.compare_solutions import compare

if __name__ == '__main__':
    data = [compare() for i in tqdm.tqdm(range(2000))]
    data = np.array(data)

    
    

    print("BEAM:", data[:, 0].mean())
    print("BASELINE:", data[:, 1].mean())
    print("NNS_VALI :", data[:, 2].mean())
    print("HPN:", data[:, 3].mean())
    print("CHRIST:", data[:, 4].mean())
    print("Min:", data[:, 5].mean())
    print("NEW:", data[:, 6].mean())
