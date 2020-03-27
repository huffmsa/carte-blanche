'''
======================================================================
Generic wrapper for validator
----------------------------------------------------------------------
'''

from carte_blanche_utils.find_path import walk
# print(find_path)
ROOT_PATH = walk(keyfile='setup.cfg')

from carte_blanche_utils.lodash.chunk import chunk


def test_chunk():

    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chunk_size = 5

    chunked_list = chunk(array, chunk_size)

    assert len(chunked_list) == 2
