'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-02-19 01:19:34
'''
import unittest
from HW04 import search_repo

class TEST_search_repo(unittest.TestCase):
        '''test simple function search_repo()'''
        def test_search_repo(self):
                self.assertEqual(search_repo("JamesLi0217"),{"GitHubApi567": 9,"SSW555_TeamPrj" : 1,"SSW810" : 1,"Stevens": 1,"Stevens-SSW567" : 2,"Triangle567" : 7})


if __name__ == "__main__":
    
    print('Running unit tests')
    unittest.main()
