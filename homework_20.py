import unittest

class TestStringMethods(unittest.TestCase):

    def test_capitalize(self):
        self.assertEqual('vova'.capitalize(), 'Vova')
        self.assertEqual('hello world'.capitalize(), 'Hello world')

    def test_join(self):
        self.assertEqual(''.join(('#', 'blacklivesmatter')), '#blacklivesmatter')


'''
Task 2 (Function from PhoneBook)
'''

def difference (list1, list2):
        list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
        return list_dif

class TestDifferenceFunctionFromPhoneBook(unittest.TestCase):

    def test_diff(self):
        l1 = [2, 3, 4, 'a']
        l2 = [2, 3, 5, 'a', 'b']
        expected_result = [4, 5, 'b']
        actual_result = difference(l1, l2)
        self.assertEqual(actual_result, expected_result)

    l1 = [2, 3, 4, 'a']
    l2 = [2, 3, 5, 'a', 'b']
    expected_result = [4, 5, 'b']
    actual_result = (difference(l1, l2))
    assert actual_result == expected_result, f'Difference of {l1} and {l2} should be {expected_result} but got {actual_result}'
    
if __name__ == '__main__':
    unittest.main()



