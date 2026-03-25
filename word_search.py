#! /usr/bin/env python3

import re # import regex module
if __name__== "__main__": # make modular
    herit_pattern_str = r'\w*herit\w*' # any word including "herit" whether there are any number of letters before or after
    herit_pattern = re.compile(herit_pattern_str, re.IGNORECASE) # ignore upper or lower case

