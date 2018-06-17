import unittest
import list_value

class TestStringMethods(unittest.TestCase):

    def test_create_tuple(self):
        test_str = list_value.data
        data_list = test_str.split()
        len_expected = len(data_list)
        result_list = list_value.create_value(test_str)
        self.assertIsInstance(result_list, list, "Dữ liệu trả về không đúng dạng list")
        for item in result_list:
            self.assertIsInstance(item, tuple, "Dữ liệu trả về không đúng dạng tuple")
        self.assertEqual(len(result_list), len_expected, "Số lượng phần tử không đúng")
        self.assertEqual(result_list[0][0], 1, 'Index phần tử đầu tiên không đúng')
        self.assertEqual(
            result_list[-1][0],
            len_expected,
            'Index phần tử cuối cùng không đúng'
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
