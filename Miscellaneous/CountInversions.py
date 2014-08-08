"""
Count number of inversions in a array
"""

import unittest
import random

def count_inversions(array):
    
    array, count = quicksort_and_count(array)
    
    return count

def quicksort_and_count(array):
    l = len(array)
    if l < 2: return array, 0
    
    mid = (l + 1) // 2
    a1, c1 = quicksort_and_count(array[:mid])
    a2, c2 = quicksort_and_count(array[mid:])
    count = 0
    i, j, k = 0, 0, 0
    l1, l2 = len(a1), len(a2)
    while k < l:
        if i < l1 and j < l2 and a1[i] <= a2[j]:
            array[k] = a1[i]
            i += 1
            k += 1
        elif i < l1 and j < l2:
            array[k] = a2[j]
            count += l1 - i
            j += 1
            k += 1
        elif i < l1:
            array[k:] = a1[i:]
            break
        else:
            array[k:] = a2[j:]
            break
    return array, c1 + c2 + count

# Unit test

def brute_count_inversions(array):
    l = len(array)
    sum = 0
    for i in range (0, l):
        for j in range(i + 1, l):
            if array[i] > array[j]: sum += 1
    return sum
    
class CountInversionsTest(unittest.TestCase):
    
    def testEmpty(self):
        self.failUnless(count_inversions([]) == 0)
        
    def test1Element(self):
        self.failUnless(count_inversions([1]) == 0)
        
    def test2Elements1(self):
        self.failUnless(count_inversions([1, 2]) == 0)
    
    def test2Elements2(self):
        self.failUnless(count_inversions([2, 1]) == 1)
        
    def test100Inverted(self):
        input_array = [i for i in range(100, 0, -1)]
        expected = (100 - 1) * 100 / 2
        self.failUnless(count_inversions(input_array) == expected)
        
    def testRandom1(self):
        input_array = [random.randint(0, 1000) for i in range(100)]
        expected = brute_count_inversions(input_array)
        self.failUnless(count_inversions(input_array) == expected)
        
    def testRandom2(self):
        input_array = [random.randint(0, 1000) for i in range(100)]
        expected = brute_count_inversions(input_array)
        self.failUnless(count_inversions(input_array) == expected)
    
    def testRandom3(self):
        input_array = [random.randint(0, 10000) for i in range(1000)]
        expected = brute_count_inversions(input_array)
        self.failUnless(count_inversions(input_array) == expected)

def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
