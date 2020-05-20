import unittest
from drawer import seeker, stylist

class TestCode(unittest.TestCase):

    def test_seeker(self):
        self.assertNotEqual(seeker.seeker(['built_in_functions','list_functions']).get_and_return_data(),None) #everything ok test

        self.assertNotEqual(seeker.seeker(['built_in_functions', 'lists_functions']).get_and_return_data(), None) #1 ok file, 1 wrong file

        self.assertNotEqual(seeker.seeker(['builst_in_functions', 'list_ffunctions']).get_and_return_data(), None) # all wrong files

    def test_stylist(self):
        items1 = seeker.seeker(['built_in_functions']).get_and_return_data()
        self.assertNotEqual(stylist.stylist(items1),None)

        items2 = seeker.seeker(['dict_functions']).get_and_return_data()
        self.assertNotEqual(stylist.stylist(items2),None)

        items3 = seeker.seeker(['list_functions']).get_and_return_data()
        self.assertNotEqual(stylist.stylist(items3),None)