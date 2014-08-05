"""
A child is running up a staircase with n steps, and can hop either 1 step, 2
steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
"""
import unittest

def step_climbing(no_of_steps):
    if no_of_steps < 1:
        raise ValueError('There must be atleast one step')
    
    n = no_of_steps # For convenience
    
    sums = [1, 0, 0, 0]
    index = 0
    
    while n > 0:
        index = (index + 1) % 4
        sums[index] = sums[(index + 1) % 4] \
                    + sums[(index + 2) % 4] \
                    + sums[(index + 3) % 4]
        n -= 1
    return sums[index]
    
# Unit tests
class StepClimbingTest(unittest.TestCase):
    
    def test0(self):
        self.assertRaises(ValueError, step_climbing, 0)
        
    def test1(self):
        self.failUnless(step_climbing(1) == 1)
        
    def test2(self):
        self.failUnless(step_climbing(2) == 2)
    
    def test3(self):
        self.failUnless(step_climbing(3) == 4)
    
    def test4(self):
        self.failUnless(step_climbing(4) == 7)
    
    def test5(self):
        self.failUnless(step_climbing(5) == 13)
        
    def test20(self):
        self.failUnless(step_climbing(20) == 121415)
        
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
