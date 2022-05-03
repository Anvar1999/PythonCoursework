from __future__ import print_function  # just for making sure that
                                       # the below works for Python 2 and 3

# print value associated with key 'James' in dct, if that key is in dct
if 'James' in dct:
    print(dct['James'])
else:
    print("'James' isn't a key in dct.")

# delete key 'Jim' and associated value if in dct
if 'Jim' in dct:
    del dct['Jim']