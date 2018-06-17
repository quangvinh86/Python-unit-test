import unittest
import day_of_month


class TestExercise(unittest.TestCase):
    MESSAGE_FMT = 'Input: `{2}`, kết quả mong muốn là `{0}`, nhận được `{1}`'

    def _test_all(self, func, cases):
        for input_, expect in cases:
            output = func(input_)
            msg = self.MESSAGE_FMT.format(expect, output, input_)
            self.assertEqual(output, expect, msg)


class TestDayOfMonth(TestExercise):

    def test_day_of_month(self):
        res = day_of_month.get_day_of_month(2)
        self.assertTrue(isinstance(res, tuple))
        self.assertEqual(len(res), 2, "Số lượng phần tử không đúng")
        cases = [(1, ("January", 31)),
                 (2, ("February", 28)),
                 (3, ("March", 31)),
                 (4, ("April", 30)),
                 (7, ("July", 31)),
                 (8, ("August", 31)),
                 (9, ("September", 30))
                 ]
        self._test_all(day_of_month.get_day_of_month, cases)


if __name__ == '__main__':
    unittest.main(verbosity=2)
