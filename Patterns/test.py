import unittest
import random
from kmp_find import find as find_kmp
from naive_find import find as find_naive
from kr_find import find as find_kr
test_text = "foobar"
class TestNaiveFind(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(find_naive(test_text,test_text),[0])

    def test_both_empty(self):
        self.assertEqual(find_naive('',''),[])

    def test_string_empty(self):
        self.assertEqual(find_naive('',test_text),[])

    def test_text_empty(self):
        self.assertEqual(find_naive(test_text,''),[])

    def test_string_longer(self):
        self.assertEqual(find_naive('foobarfoo',test_text),[])

    def test_unfound_string(self):
        self.assertEqual(find_naive('abc',test_text),[])

    def test_found_string(self):
        self.assertEqual(find_naive('foo',test_text),[0])

class TestKrFind(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(find_kr(test_text,test_text),[0])

    def test_both_empty(self):
        self.assertEqual(find_kr('',''),[])

    def test_string_empty(self):
        self.assertEqual(find_kr('',test_text),[])

    def test_text_empty(self):
        self.assertEqual(find_kr(test_text,''),[])

    def test_string_longer(self):
        self.assertEqual(find_kr('foobarfoo',test_text),[])

    def test_unfound_string(self):
        self.assertEqual(find_kr('abc',test_text),[])

    def test_found_string(self):
        self.assertEqual(find_kr('foo',test_text),[0])

class TestKmpFind(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(find_kmp(test_text,test_text),[0])

    def test_both_empty(self):
        self.assertEqual(find_kmp('',''),[])

    def test_string_empty(self):
        self.assertEqual(find_kmp('',test_text),[])

    def test_text_empty(self):
        self.assertEqual(find_kmp(test_text,''),[])

    def test_string_longer(self):
        self.assertEqual(find_kmp('foobarfoo',test_text),[])

    def test_unfound_string(self):
        self.assertEqual(find_kmp('abc',test_text),[])

    def test_found_string(self):
        self.assertEqual(find_kmp('foo',test_text),[0])
class TestAllFind(unittest.TestCase):
    def test_1(self):
        test_string = ''.join((random.choice('ab') for i in range(10)))
        test_txt = ''.join((random.choice('ab') for i in range(3)))
        self.assertTrue((find_kmp(test_string,test_txt)==find_kr(test_string,test_txt)) and (find_kmp(test_string,test_txt)==find_naive(test_string,test_txt)))
    def test_2(self):
        test_string = ''.join((random.choice('ab') for i in range(10)))
        test_txt = ''.join((random.choice('ab') for i in range(3)))
        self.assertTrue((find_kmp(test_string,test_txt)==find_kr(test_string,test_txt)) and (find_kmp(test_string,test_txt)==find_naive(test_string,test_txt)))
    def test_3(self):
        test_string = ''.join((random.choice('ab') for i in range(10)))
        test_txt = ''.join((random.choice('ab') for i in range(3)))
        self.assertTrue((find_kmp(test_string,test_txt)==find_kr(test_string,test_txt)) and (find_kmp(test_string,test_txt)==find_naive(test_string,test_txt)))