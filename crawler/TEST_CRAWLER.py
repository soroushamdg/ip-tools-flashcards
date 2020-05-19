import unittest
from crawler import extracter, requester, saver

class TestCode(unittest.TestCase):
    def test_request(self):
        requester_1 = requester.requester('http://apple.com')
        self.assertEqual(requester_1.extract_html()['error'],False)

        requester_2 = requester.requester('https://www.w3schools.com/python/python_datetime.asp')
        self.assertEqual(requester_2.extract_html()['error'], False)

        requester_3 = requester.requester('http://google.com')
        self.assertEqual(requester_3.extract_html()['error'], False)

    def test_extracter(self):

        test_1 = requester.requester('https://www.w3schools.com/python/python_ref_list.asp').extract_html()
        extracter_1 = extracter.extracter_from_w3(test_1['content'])
        self.assertNotEqual(extracter_1.extract_data(),False)

        test_2 = requester.requester('https://www.w3schools.com/python/python_ref_dictionary.asp').extract_html()
        extracter_2 = extracter.extracter_from_w3(test_2['content'])
        self.assertNotEqual(extracter_2.extract_data(), False)

        test_3 = requester.requester('https://www.w3schools.com/python/python_ref_functions.asp').extract_html()
        extracter_3 = extracter.extracter_from_w3(test_3['content'])
        self.assertNotEqual(extracter_3.extract_data(), False)


    def test_saver(self):
        test_1 = requester.requester('https://www.w3schools.com/python/python_ref_list.asp').extract_html()
        extracter_1 = extracter.extracter_from_w3(test_1['content']).extract_data()
        self.assertEqual(saver.saver('list_functions').save_data_into_file(extracter_1), True)
        test_2 = requester.requester('https://www.w3schools.com/python/python_ref_dictionary.asp').extract_html()
        extracter_2 = extracter.extracter_from_w3(test_2['content']).extract_data()
        self.assertEqual(saver.saver('dict_functions').save_data_into_file(extracter_2), True)
        test_3 = requester.requester('https://www.w3schools.com/python/python_ref_functions.asp').extract_html()
        extracter_3 = extracter.extracter_from_w3(test_3['content'],index=False).extract_data()
        self.assertEqual(saver.saver('built_in_functions',index=False).save_data_into_file(extracter_3), True)