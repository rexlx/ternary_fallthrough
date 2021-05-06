import string
import sys


matches = []


def gen_map():
    alpha = string.ascii_lowercase
    data = enumerate(alpha, 1)
    ch_map = { v: k for (k,v) in data}
    return ch_map


def get_args():
    if len(sys.argv) > 1:
        # traditional
        # val = int(sys.argv[1]) if int(sys.argv[1]) else False
        # this reads: try and convert to int if you can, if you cant, dont.
        val = int(sys.argv[1]) if int(sys.argv[1]) else fallthrough # <- this would drop to the next condition
    else:
        print("expected a number as an arg")
        exit(1)
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
    # if we had done a traditional ternary operation, we
    # would have written "else False" (or whatever we wanted it to be,
    # rather), which would require this additional logic.
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
