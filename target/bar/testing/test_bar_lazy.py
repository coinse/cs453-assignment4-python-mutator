import sys
import numpy as np
import os

curr_dir = os.getcwd()
parent_dir = os.path.dirname(os.path.dirname(curr_dir))
sys.path.insert(1, parent_dir)

from bar.lazy import *

def test_sort1():
    randnums= np.random.randint(1,101,10)
    result = sort1(randnums)
    sorted_array = sorted(randnums)
    assert (np.array(randnums) == np.array(sorted_array)).all()

def test_sort2():
    randnums= np.random.randint(1,101,10)
    result = sort2(randnums)
    sorted_array = sorted(randnums)
    assert (np.array(randnums) == np.array(sorted_array)).all()

def test_sort3():
    randnums= np.random.randint(1,101,10)
    result = sort3(randnums)
    sorted_array = sorted(randnums)
    assert (np.array(randnums) == np.array(sorted_array)).all()
