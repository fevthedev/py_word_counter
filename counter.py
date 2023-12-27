import sys


def count_words(filename):
    try:
        with open(filename, 'r') as sample:
            txt = sample.read()
            print('word count: ', len(txt.split()))
            print('Word count complete.')
    except FileNotFoundError:
        print('Please provide a valid file path.')
        print('Operation failed.')


print('Reading words')
# expects file path to be provided after script name
count_words(sys.argv[1])
