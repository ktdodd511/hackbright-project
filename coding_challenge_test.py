#!/usr/bin/env python2.7

a_string = '0h2abe1zy'
# a_string = '1wk0a2wet1oi0e'
word_list = list(a_string)
new_list = []


def decode(word):
    word_list_iter = iter(word_list)
    # iterates over the list
    for word in word_list_iter:

        if word == '0':
            continue
            # doesn't skip, just goes to the next element
        elif word == '1':
            next(word_list_iter)
            # skips over the next element
        elif word == '2':
            next(word_list_iter)
            next(word_list_iter)
            # skips over the next 2 elements
        else:
            new_list.append(word)
            # adds anything that wasn't skipped over to an empty list

    decoded_string = ''.join(new_list)
    # form the list into a string
    print decoded_string


decode(a_string)