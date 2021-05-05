import string
import sys
import random
import os


matches= []


def gen_map():
    alpha = string.ascii_lowercase
    data = enumerate(alpha, 1)
    ch_map = { v: k for (k,v) in data}
    return ch_map


def get_args():
    if len(sys.argv) > 1:
        val = int(sys.argv[1]) if int(sys.argv[1]) else fallthrough # <- this would drop to the next condition
    else:                                                           #    ultimately saving a test down around line 40
        print("expected a number as an arg")
    return val

def read_file(file="/Users/rexfitzhugh/bin/data/words"):
    print("opening file..")
    with open(file) as f:
        contents = f.read().split("\n")
    print("contents stored...")
    return contents

def sum_ch(word, ch_map, val):
    _str_ = word.lower()
    score = []
    chars = list(_str_)
    for i in chars:
        if i not in ch_map.keys():
            continue
        else:
            score.append(ch_map[i])
    # here we now have to test the value
    if val and sum(score) == val:
        matches.append(word)

def main():
    val = get_args()
    ch_map = gen_map()
    contents = read_file()
    for i in contents:
        sum_ch(i, ch_map, val)

    for i in matches:
        print(i)

if __name__ == "__main__":
    main()
