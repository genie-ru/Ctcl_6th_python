"""
def is_unique(string):
    char_set = {}
    for char in string:
        if char in char_set:
            return False
        char_set[char] = True
    return True
"""

#重複のない文字列：ある文字列が、すべて固有である(重複する文字がない)かどうかを判定するアルゴリズムを実装してください。また、それを実装するのに新たなデータ構造が使えない場合、どのようにすればいいですか？
# O(N)
import unittest


def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()