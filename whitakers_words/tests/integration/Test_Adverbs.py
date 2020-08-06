from whitakers_words.parse import Parser

import unittest


class AdverbTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.par = Parser()

    def test_melius(self):
        """
        expected = {'word': 'melius',
                    'defs': [{'orth': ['bene', 'melius', 'optime'],
	                          'senses': ['well, very, quite, rightly, agreeably, cheaply, in good style', 'better', 'best'],
	                          'infls': [{'stem': 'melius', 'ending': '', 'pos': 'adverb',
                                         'form': {'degree': 'comparative'}}]}}
        """
        result = self.par.parse("melius")

        # response syntax and basics
        self.assertEqual(len(result['defs']), 1)  # there is only one definition
        #self.assertTrue(len(result['defs'][0]))  # defs does not contain an empty dictionary
        #self.assertEqual(len(result['defs'][0]['infls']), 1)  # there is only one inflection

        # response splitting
        infl = result['defs'][0]['infls'][0]
        self.assertEqual(infl['stem'], 'melius')
        self.assertEqual(infl['ending'], '')
        self.assertEqual(infl['pos'], 'adverb')

        # response details
        form = infl['form']
        expected_form = {'degree': 'comparative'}
        self.assertEqual(form, expected_form)
