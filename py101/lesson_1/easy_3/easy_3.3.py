# Bannerizer

def print_in_box(str):
    length = len(str)
    print('+-' + ('-' * length) + '-+')
    print('| ' + (' ' * length) + ' |')
    print('| ' + str + ' |')
    print('| ' + (' ' * length) + ' |')
    print('+-' + ('-' * length) + '-+')




print_in_box('To boldly go where no one has gone before.')