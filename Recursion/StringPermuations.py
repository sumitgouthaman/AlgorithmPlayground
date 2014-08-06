"""
Print all possible permutations of a set of characters in a given string
"""

import unittest

def get_permutations(string):
    
    if string == "": return []
    
    if len(string) == 1: return [string]
    
    sub_permutations = get_permutations(string[1:])
    permutations = []
    first_letter = string[0]
    
    for sub_permutation in sub_permutations:
        for i in range(0, len(sub_permutation)):
            permutations.append(
                sub_permutation[:i]
                + first_letter
                + sub_permutation[i:])
        permutations.append(sub_permutation + first_letter)
    
    return permutations

# Unit Tests
class GetPermutationsTest(unittest.TestCase):
    
    def testA(self):
        intended_output = ['A']
        actual_output = get_permutations('A')
        self.failUnless(intended_output.sort() == actual_output.sort())
        
    def testAB(self):
        intended_output = ['AB', 'BA']
        actual_output = get_permutations('AB')
        self.failUnless(intended_output.sort() == actual_output.sort())
    
    def testABC(self):
        intended_output = ['ABC', 'BCA', 'CAB', 'BAC', 'ACB', 'CBA']
        actual_output = get_permutations('ABC')
        self.failUnless(intended_output.sort() == actual_output.sort())
        
def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
