#! /usr/bin/env python3

import re # import regex module
if __name__== "__main__": # make modular
    herit_pattern_str = r'\w*herit\w*' # any word including "herit" whether there are any number of letters before or after
    herit_pattern = re.compile(herit_pattern_str, re.IGNORECASE) # ignore upper or lower case

print('Opening origin.txt')
with open('origin.txt', 'r') as in_stream:
    print('Opening origin_output.txt')
    with open('origin_output.txt', 'w') as out_stream:
        for line_index, line in enumerate(in_stream):
            line = line.strip()
            word_list = line.split()
            word_list.sort()
            for word in word_list:
                out_stream.write(f'Line: {line_index + 1}\t{word}\n')
print("Done!")
print('origin.txt is closed?', in_stream.closed)
print('origin_output.txt is closed?', out_stream.closed)
