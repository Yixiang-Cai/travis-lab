#-*- coding:utf-8 -*-
import codecs

file='input.txt'
minimum=ord(u'\u2E00')
maximum=ord(u'\uFFA5')

def read_input(file=file,minimum=minimum):
    f=codecs.open(file,encoding='utf-8')
    text=f.read()
    result=''.join([text[i] for i in range(len(text)) if (ord(text[i])>minimum)])
    return result

def test_answer():
    assert len(read_input())==6

read_input()
