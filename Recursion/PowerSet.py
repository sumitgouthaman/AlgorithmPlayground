"""
Given a set of elements, give the power set, i.e. set containing all the 
possible subsets of the set.
"""

import unittest

def power_set_helper(input_set):
    if len(input_set) == 1:
    	return [[input_set[0]]]
    item = input_set.pop()
    
    subset = power_set_helper(input_set)
    copy = list()
    
    for s in subset:
        copy.append(s + [item])
    
    subset += copy + [[item]]
    
    return subset 

def power_set(input_set):
	subset = power_set_helper(input_set)
	subset.append([''])
	
	result = set()
	for s in subset:
		f = frozenset(s)
		result.add(f)
		
	return result


# Unit test
class PowersetTests(unittest.TestCase):
    
    def testA(self):
        expected = set([frozenset(['']), frozenset(['A'])])
        actual = power_set(['A'])
        self.failUnless(expected == actual)
    
    def testAB(self):
        expected = set([frozenset(['']), frozenset(['A']), frozenset(['B']),
        	frozenset(['A', 'B'])])
        actual = power_set(['A', 'B'])
        self.failUnless(expected == actual)
    
    def testABC(self):
        expected = set([frozenset(['']), frozenset(['A']), frozenset(['B']),
        	frozenset(['C']), frozenset(['A', 'B']), frozenset(['B', 'C']),
        	frozenset(['A', 'C']), frozenset(['A', 'B', 'C'])])
        actual = power_set(['A', 'B', 'C'])
        self.failUnless(expected == actual)
    
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
