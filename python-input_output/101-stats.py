#!/usr/bin/python3

"""
101-stats Module
"""

import sys
from collections import defaultdict


def print_metrics(total_size, status_counts):
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


def main():
    total_size = 0
    status_counts = defaultdict(int)
    try:
        for i, line in enumerate(sys.stdin, start=1):
            parts = line.split()
            if len(parts) >= 7:
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size
                status_counts[status_code] += 1
            if i % 10 == 0:
                print_metrics(total_size, status_counts)
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)


if __name__ == "__main__":
    main()
