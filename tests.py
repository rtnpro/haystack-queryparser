#!/usr/bin/python
# coding: latin-1

"""
Testing common search query syntax.
"""


from unittest import *
from haystack.query import SQ
from getSQ import parse

class SimpleTest(TestCase):
    def setUp(self):
        self.testcase = {
            "note":str(SQ(content="note")),
            '"need note"':str(SQ(content__exact="need note")),
            "author:admin":str(SQ(author="admin")),
            "author:admin notes":str(SQ(author="admin")&SQ(content="notes")),
            'title:"need note"':str(SQ(title__exact="need note")),
            #u"need note 您好测试这":str(SQ(content="need")&SQ(content="note")&SQ(content=u"您")&SQ(content=u"好")&SQ(content=u"测")&SQ(content=u"试")&SQ(content=u"这")),
            "need note NOT used":str(SQ(content="need")&SQ(content="note") & ~SQ(content="used")),
            "(a AND b) OR (c AND d)":str((SQ(content="a")&SQ(content="b"))|(SQ(content="c")&SQ(content="d"))),
            "a AND b OR (c AND d)":str(SQ(content="a")&SQ(content="b")|(SQ(content="c")&SQ(content="d"))),
            
        }
    def test_parse(self):
        for case in self.testcase.keys():
            self.assertEqual(str(parse(case)),self.testcase[case])


def main():
    suite = TestLoader().loadTestsFromTestCase(SimpleTest)
    TextTestRunner(verbosity=2).run(suite)


