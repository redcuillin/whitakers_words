import unittest
from whitakers_words.finder import find_inflection
from whitakers_words.enums import WordType


class FinderTest(unittest.TestCase):
    def test_basic_noun_us(self):
        us = find_inflection(WordType.N, [2, 1], ["NOM", "S", "M"])
        self.assertEqual("us", us)

    def test_basic_noun_a(self):
        a = find_inflection(WordType.N, [1, 1], ["NOM", "S", "F"])
        self.assertEqual("a", a)

    def test_basic_noun_ae(self):
        ae = find_inflection(WordType.N, [1, 1], ["GEN", "S", "F"])
        self.assertEqual("ae", ae)

    def test_basic_noun_empty(self):
        em = find_inflection(WordType.N, [3, 1], ["NOM", "S", "M"])
        self.assertEqual("", em)

    def test_basic_noun_em(self):
        em = find_inflection(WordType.N, [3, 1], ["ACC", "S", "M"])
        self.assertEqual("em", em)

    def test_basic_verb_em(self):
        em = find_inflection(WordType.V, [1, 1], ["PRES", "ACTIVE", "SUB", "1", "S"])
        self.assertEqual("em", em)

    def test_basic_verb_mini(self):
        i = find_inflection(WordType.V, [3, 1], ["PRES", "PASSIVE", "IND", "2", "P"])
        self.assertEqual("imini", i)

    def test_basic_verb_i(self):
        i = find_inflection(WordType.V, [3, 1], ["PERF", "ACTIVE", "IND", "1", "S"])
        self.assertEqual("i", i)

    def test_basic_verb_are(self):
        are = find_inflection(WordType.V, [1, 1], ["PRES", "ACTIVE", "INF", "0", "X"])
        self.assertEqual("are", are)

    def test_basic_verb_isse(self):
        isse = find_inflection(WordType.V, [1, 1], ["PERF", "ACTIVE", "INF", "0", "X"])
        self.assertEqual("isse", isse)

    def test_basic_verbal_participle_us(self):
        us = find_inflection(WordType.VPAR, [3, 1], ["NOM", "S", "M", "PERF", "PASSIVE"])
        self.assertEqual("us", us)
