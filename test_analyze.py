from analyze import running_total

def test_example_one():
    assert running_total([1, 2, 1, 8, 9, 2]) == [3, 18, 2]

def test_example_two():
    assert running_total([1, 3, 4, 2, 5, 4, 6, 9]) == [8, 7, 19]

def test_example_three():
    assert running_total([3]) == [3]  #check for single value

def test_example_four():
    assert running_total([-5,-2,3,2,4]) ==[-4,6] #check for negative integers
