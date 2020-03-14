# Epub-to-Mobi-Converter
# Python script to convert epub files to mobi

import argparse
import os

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get the Output file format')
    parser.add_argument('--out',
                        required=True,
                        choices=['azw3', 'docx', 'epub', 'fb2', 'html',
                                 'htmlz', 'lit', 'lrf', 'mobi',
                                 'oeb', 'pdb', 'pdf', 'pml', 'rb',
                                 'rtf', 'snb', 'tcr', 'txt', 'txtz'],
                        help='Output file format')

    args = parser.parse_args()

    out_ext = vars(args).get('out')

    # Example system call for converting ebooks
    # /Applications/calibre.app/Contents/MacOS/ebook-convert input output

    input_list = ['.azw4', '.chm', '.comic', '.djvu', '.docx',
                  '.epub', '.fb2', '.htlz', '.html', '.lit',
                  '.lrf', '.mobi', '.odt', '.pdb', '.pdf', '.pml',
                  '.rb', '.rtf', '.recipe', '.snb', '.tcr', '.txt']

    directory = "./ebooks/"
    directory_formatted = "./converted-books/"
    for files in os.listdir(directory):

        file_name, ext = os.path.splitext(files)

        if ext not in input_list:
            break

        os.system(
            "/Applications/calibre.app/Contents/MacOS/ebook-convert " +
            directory +
            files + " " +
            directory_formatted + file_name + "." + out_ext)
