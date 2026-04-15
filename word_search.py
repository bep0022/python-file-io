#! /usr/bin/env python3

import re

def extract_herit_words(input_file, output_file):
    """
    Read an input file, extract all words containing 'herit',
    and write them to an output file with their line numbers.

    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output text file.
    """
    herit_pattern = re.compile(r'\w*herit\w*', re.IGNORECASE)

    print(f'Opening {input_file}')
    with open(input_file, 'r') as in_stream:
        print(f'Opening {output_file}')
        with open(output_file, 'w') as out_stream:

            for line_index, line in enumerate(in_stream):
                line = line.strip()

                # Extract clean words (no punctuation)
                word_list = re.findall(r'\b\w+\b', line)
                word_list.sort()

                for word in word_list:
                    if herit_pattern.search(word):
                        out_stream.write(f'Line: {line_index + 1}\t{word}\n')

    print("Done!")
    print(f'{input_file} is closed?', in_stream.closed)
    print(f'{output_file} is closed?', out_stream.closed)


def main():
    """
    Main function that defines file names and runs the extraction process.
    """
    input_file = 'origin.txt'
    output_file = 'origin_output.txt'

    extract_herit_words(input_file, output_file)


if __name__ == "__main__":
    main()
