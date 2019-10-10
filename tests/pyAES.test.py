import sys
sys.path.insert(0, '../')

import pyAES
import s_box

import unittest
from copy import deepcopy


class pyAES_test(unittest.TestCase):
    TEST_STATE = [[b'\x01',b'\x02',b'\x03',b'\x04'],
                  [b'\x05',b'\x06',b'\x07',b'\x08'],
                  [b'\x09',b'\x0a',b'\x0b',b'\x0c'],
                  [b'\x0d',b'\x0e',b'\x0f',b'\x00']]

    def test_shift_rows(self):
        state = deepcopy(self.TEST_STATE)
        rows_shifted = [[b'\x01',b'\x02',b'\x03',b'\x04'],
                        [b'\x06',b'\x07',b'\x08',b'\x05'],
                        [b'\x0b',b'\x0c',b'\x09',b'\x0a'],
                        [b'\x00',b'\x0d',b'\x0e',b'\x0f']]
        self.assertEqual(pyAES.shift_rows(state), rows_shifted)

    def test_inv_shift_rows(self):
        state = deepcopy(self.TEST_STATE)
        inv_rows_shifted = [[b'\x01',b'\x02',b'\x03',b'\x04'],
                            [b'\x08',b'\x05',b'\x06',b'\x07'],
                            [b'\x0b',b'\x0c',b'\x09',b'\x0a'],
                            [b'\x0e',b'\x0f',b'\x00',b'\x0d']]
        self.assertEqual(pyAES.inverse_shift_rows(state), inv_rows_shifted)

    def test_mix_columns(self):
        state = deepcopy(self.TEST_STATE)
        columns_mixed = [[b'\x09', b'\x0a', b'\x0b', b'\x1c'], 
                         [b'\x15', b'\x16', b'\x17', b'\x18'], 
                         [b'\x19', b'\x1a', b'\x1b', b'\x1c'], 
                         [b'\x0d', b'\x0e', b'\x0f', b'\x20']]
        self.assertEqual(pyAES.mix_columns(state), columns_mixed)

    def test_inv_mix_columns(self):
        state = deepcopy(self.TEST_STATE)
        inv_columns_mixed = []
        #self.assertEqual(pyAES.inverse_mix_columns(state), inv_columns_mixed)

    def test_sub_bytes(self):
        state = deepcopy(self.TEST_STATE)
        sbox = s_box.create()
        bytes_subed = [[b'\x7c',b'\x77',b'\x7b',b'\xf2'],
                       [b'\x6b',b'\x6f',b'\xc5',b'\x30'],
                       [b'\x01',b'\x67',b'\x2b',b'\xfe'],
                       [b'\xd7',b'\xab',b'\x76',b'\x63']]
        self.assertEqual(pyAES.sub_bytes(state,sbox), bytes_subed)

    def test_inv_sub_bytes(self):
        state = deepcopy(self.TEST_STATE)
        inv_sbox = s_box.create_inverse()
        inv_bytes_subed = [[b'\x09',b'\x6a',b'\xd5',b'\x30'],
                           [b'\x36',b'\xa5',b'\x38',b'\xbf'],
                           [b'\x40',b'\xa3',b'\x9e',b'\x81'],
                           [b'\xf3',b'\xd7',b'\xfb',b'\x52']]
        self.assertEqual(pyAES.inverse_sub_bytes(state,inv_sbox), inv_bytes_subed)

    def test_add_round_key(self):
        state = deepcopy(self.TEST_STATE)
        key = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x00'
        round_key_added = [[b'\x00',b'\x00',b'\x00',b'\x00'],
                           [b'\x00',b'\x00',b'\x00',b'\x00'],
                           [b'\x00',b'\x00',b'\x00',b'\x00'],
                           [b'\x00',b'\x00',b'\x00',b'\x00']]
        self.assertEqual(pyAES.add_round_key(state,key), round_key_added)

if __name__ == "__main__":
    unittest.main()
