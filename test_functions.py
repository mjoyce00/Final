"""Test for my functions.""" 

from my_module.functions import *

###FUNCTIONS THAT TEST IF MY FUNCTIONS ARE CALLABLE 
def test_my_function():
    
    assert callable(Welcome_To_The_Game)
    
def test_my_function_2():
    
    assert callable(instructions)
    
def test_my_function_3():
    
    assert callable(level_1)
    
def test_my_function_4():
    
    assert callable(level_2)   
    
def test_my_function_5():
    
    assert callable(level_3) 
    
def test_my_function_6():
    
    assert callable(level_4)
    
def test_my_function_7():
    
    assert callable(level_5) 