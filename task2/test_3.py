#coding=utf-8

file='input.txt'
minimum=ord(u'\u2E00')
maximum=ord(u'\uFFA5')

def read_input(file=file,minimum=minimum):
    f=open(file,'r')
    text=f.read()
    result=''.join([tt[i] for i in range(len(tt)) if (ord(tt[i])>minimum)])
    return result

def test_answer():
    assert len(read_input())==6
