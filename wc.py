import sys, os
sys.path.append('/Users/Quentin/Documents/Python/Think Python')

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print(linecount('/Users/Quentin/Documents/Python/Think Python/wc.py'))


if __name__ == '__main__':
    print(linecount('wc.py'))
