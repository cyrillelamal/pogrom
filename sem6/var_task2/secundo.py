# Написать программу, позволяющую выполнять проверку свойства
# парности скобок в строке текста, а также вычислять их количество.
# Используйте для возвращения результатов подсчета механизм генераторов.
# Решение сопроводить тестами и опубликовать в портфолио.
import unittest
import random


class BracketCheck:
    BRACKET_PAIRS = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    def __init__(self, is_valid=False, counts=None):
        self.is_valid = is_valid
        self.counts = counts if counts is not None else {b: 0 for b in self.BRACKET_PAIRS.keys()}

    @classmethod
    def invalid(cls):
        return cls(False, {})

    @classmethod
    def check(cls, string: str) -> 'BracketCheck':
        stack = []
        counts = {b: 0 for b in cls.BRACKET_PAIRS.keys()}

        for ch in string:
            if ch in cls.BRACKET_PAIRS.keys():  # opening
                stack.append(ch)
                counts[ch] = counts[ch] + 1 if counts.get(ch, None) else 1
            elif ch in cls.BRACKET_PAIRS.values():  # closing
                if not stack or cls.BRACKET_PAIRS[stack.pop()] != ch:
                    return BracketCheck.invalid()

        if stack:
            return BracketCheck.invalid()

        return BracketCheck(True, counts)


class TestBracketCheck(unittest.TestCase):
    def test_valid_pairs(self):
        string = "()"
        check = BracketCheck.check(string)
        self.assertTrue(check.is_valid)

        string = "(())"
        check = BracketCheck.check(string)
        self.assertTrue(check.is_valid)

        string = "{([])}"
        check = BracketCheck.check(string)
        self.assertTrue(check.is_valid)

    def test_invalid_pairs(self):
        string = "())"
        check = BracketCheck.check(string)
        self.assertFalse(check.is_valid)

        string = ")"
        check = BracketCheck.check(string)
        self.assertFalse(check.is_valid)

        string = "{("
        check = BracketCheck.check(string)
        self.assertFalse(check.is_valid)

    def test_valid_pairs_with_other_symbols(self):
        string = """
print({$var}); // valid php program
        """
        check = BracketCheck.check(string)
        self.assertTrue(check.is_valid)

    def test_counts(self):
        bank = BracketCheck.BRACKET_PAIRS.copy()
        nb = random.randint(3, 10)
        bracket = random.choice(list(bank.keys()))
        string = nb * bracket + nb * bank[bracket]

        check = BracketCheck.check(string)
        self.assertEqual(nb, check.counts[bracket])
