#-*- coding: utf-8 -*-

import os
import os.path
import re
import sys

def hex2byte(h):
    return int(h, 16).to_bytes(1, 'big')

def parsehexstr(hexstr):
    hs = re.sub('[\\s,]+', '', hexstr)
    if (len(hs) % 2 != 0):
        raise Exception('渡された１６進数文字列の文字数は偶数ではありません')
    return [ hs[i:i+2] for i in range(0, len(hs), 2) ]

def readfile(p):
    with open(p, 'r') as fr:
        return fr.read()

def getwfilename(p):
    return p + '.dat'

def getreadfile():
    if len(sys.argv) != 2:
        raise Exception('引数の数が不正です。１６進数文字列のファイルを指定します')
    p = sys.argv[1]
    if not os.path.exists(p):
        raise Exception('インプットファイルが見つかりません')
    return p

def main():
    try:
        rfile = getreadfile()
        wfile = getwfilename(rfile)
        wbytCnt = 0
        with open(wfile, 'wb') as f:
            wbytCnt = len([ f.write(hex2byte(h)) for h in parsehexstr(readfile(rfile)) ])
    except Exception as e:
        print(e)
    print(f'write file success: {wfile}')
    print(f'write byte cnt    : {wbytCnt}')

if __name__ == '__main__':
    main()