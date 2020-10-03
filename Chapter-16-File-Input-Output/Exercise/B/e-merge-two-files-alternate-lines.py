"""
WAP that merges lines alternately from two files and writes the results to new file.
If one file has less number of lines than the other, the remaining lines from the larger file should be simply copied into the
target file.
"""
import itertools

with open('file-A.txt') as src1, open('file-B.txt', 'r') as src2, open('file-merge.txt', 'w') as dst:
    for line_from_first, line_from_second in itertools.zip_longest(src1, src2):
        if line_from_first is not None:
            dst.write(line_from_first)
        if line_from_second is not None:
            dst.write(line_from_second)

#[Source: stackoverflow]