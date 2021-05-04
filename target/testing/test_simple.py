# # some_file.py
import sys
import os

curr_dir = os.getcwd()
parent_dir = os.path.dirname(curr_dir)
sys.path.insert(1, parent_dir)

from simple import *

def test_simple():
    assert get_started() == 6

def test_simple_1(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "hi all\n"

def test_simple_2(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.err == ""

def test_simple_3():
    assert nami(5) == 20

def test_simple_3():
    assert nami(-1) == 5