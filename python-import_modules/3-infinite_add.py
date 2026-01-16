#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0

    for count in range(1, len(sys.argv)):
        sum += int(sys.argv[count])
    print(sum)
