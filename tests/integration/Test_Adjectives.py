from whitakers_words.parse import Parser

import unittest


class AdjectiveTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.par = Parser()

    def test_saevarum(self):
        """
        expected = {'word': 'saevarum',
                    'defs': [{'orth': ['saev', 'saev', 'saevi', 'saevissi'],
                              'senses': ['savage', 'fierce/ferocious', 'violent/wild/raging',
                                         'cruel, harsh, severe', 'vehement'],
                              'infls': [{'stem': 'saev', 'ending': 'arum', 'pos': 'adjective',
                                         'form': {'case': 'genitive', 'number': 'plural',
                                                  'gender': 'feminine', 'degree': 'positive'}}]}]}
        """
        result = self.par.parse("saevarum")

        # response syntax and basics
        self.assertEqual(len(result['defs']), 1)  # there is only one definition
        self.assertTrue(len(result['defs'][0]))  # defs does not contain an empty dictionary
        self.assertEqual(len(result['defs'][0]['infls']), 1)  # there is only one inflection

        # response splitting
        infl = result['defs'][0]['infls'][0]
        self.assertEqual(infl['stem'], 'saev')
        self.assertEqual(infl['ending'], 'arum')
        self.assertEqual(infl['pos'], 'adjective')

        # response details
        form = infl['form']
        expected_form = {'case': 'genitive', 'number': 'plural', 'gender': 'feminine', 'degree': 'positive'}
        self.assertEqual(form, expected_form)
