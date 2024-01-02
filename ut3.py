import unittest
import a3 

class check(unittest.TestCase):
    def test_ans(self):
        a={'id': 'id1', 'impressions': [{'id': 'id1', 'name': 'n1'}, {'id': 'id2', 'name': 'n2'}], 'clicks': [{'id': 'id1', 'cid': 'cid1'}, {'id': 'id1', 'cid': 'cid2'},  {'id': 'id3', 'cid': 'cid4'}]}
        b=a3.ans(a)
        c={'id': 'id1', 'impressions': [{'id': 'id1', 'name': 'n1', 'clicks': ['cid1', 'cid2'], 'has_click': True}, {'id': 'id2', 'name': 'n2', 'clicks': [], 'has_click': False}]}

        self.assertEqual(b,c)

unittest.main()