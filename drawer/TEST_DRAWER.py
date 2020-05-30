import unittest
from drawer import seeker, stylist, designer

class TestCode(unittest.TestCase):

    def test_seeker(self):
        self.assertNotEqual(seeker.seeker(['built_in_functions','list_functions']).get_and_return_data(),None) #everything ok test

        self.assertNotEqual(seeker.seeker(['built_in_functions', 'lists_functions']).get_and_return_data(), None) #1 ok file, 1 wrong file

        self.assertNotEqual(seeker.seeker(['builst_in_functions', 'list_ffunctions']).get_and_return_data(), None) # all wrong files

    def test_stylist(self):
        items1 = seeker.seeker(['built_in_functions']).get_and_return_data()
        self.assertNotEqual(stylist.stylist(items1).set_pptx_to_item(),None)

        items2 = seeker.seeker(['dict_functions']).get_and_return_data()
        self.assertNotEqual(stylist.stylist(items2).set_pptx_to_item(),None)

        items3 = seeker.seeker(['list_functions']).get_and_return_data()
        self.assertNotEqual(stylist.stylist(items3).set_pptx_to_item(),None)

    # def test_designer(self):
    #     items1 = seeker.seeker(['built_in_functions']).get_and_return_data()
    #     datalist1 = stylist.stylist(items1).set_pptx_to_item()
    #     self.assertEqual(designer.designer(datalist1).design_data(False), True)
    #
    #     items2 = seeker.seeker(['dict_functions']).get_and_return_data()
    #     datalist2 = stylist.stylist(items2).set_pptx_to_item()
    #     self.assertEqual(designer.designer(datalist2).design_data(), True)
    #
    #     items3 = seeker.seeker(['list_functions']).get_and_return_data()
    #     datalist3 = stylist.stylist(items3).set_pptx_to_item()
    #     self.assertEqual(designer.designer(datalist3).design_data(), True)