'''
@Author: Puzhuo Li
@Github: https://github.com/JamesLi0217
@Date: 2019-02-19 01:19:34
'''

import unittest
from unittest import mock
from HW04 import search_repo


class TEST_search_repo(unittest.TestCase):
    '''test simple function search_repo()'''
    @mock.patch("urllib.request.urlopen")
    def test_search_repo(self, mock_search_repo):
        mock_search_repo.side_effect = [
            '[{"name":"GitHubApi567"}, {"name":"SSW810"},{"name":"Stevens"},{"name":"Triangle567"}]',
            '[{"foo":1},{"foo1":1},{"foo2":1},{"foo3":1},{"foo4":1},{"foo5":1},{"foo6":1},{"foo7":1},{"foo8":1}]',
            '[{"boo":1},{"boo1":1},{"boo2":1}]',
            '[{"bin":1},{"bin1":1},{"bin2":1},{"foo4":1},{"foo5":1},{"foo6":1},{"foo7":1},{"foo8":1}]',
            '[{"bin":1},{"bin1":1},{"bin2":1},{"foo4":1},{"foo5":1}]',
        ]

        expect = {"GitHubApi567": 9, "SSW810": 3,"Stevens": 8, "Triangle567": 5}
        result = search_repo("JamesLi0217")
        self.assertEqual(result, expect)


if __name__ == "__main__":

    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)
