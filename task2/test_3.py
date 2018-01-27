#-*- coding:utf-8 -*- 
import re

def test_answer(file='input.txt'):
    f = open(file,'r')
    words = ''.join(f.readlines())
    regex_str = re.compile("[\u2E00-\uFFA5]+")
    assert len(''.join(regex_str.findall(words)))==6
