import sys
sys.path.insert(0, '../')
import key_schedule
import unittest

class KeyScheduleTest(unittest.TestCase):
    def test_generate(self):
        generated1 = generate(b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c')
        generated2 = generate(b'\x8e\x73\xb0\xf7\xda\x0e\x64\x52\xc8\x10\xf3\x2b\x80\x90\x79\xe5\x62\xf8\xea\xd2\x52\x2c\x6b\x7b')
        generated3 = generate(b'\x60\x3d\xeb\x10\x15\xca\x71\xbe\x2b\x73\xae\xf0\x85\x7d\x77\x81\x1f\x35\x2c\x07\x3b\x61\x08\xd7\x2d\x98\x10\xa3\x09\x14\xdf\xf4')
        schedule1 = [b'\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c',
                     b'\xa0\xfa\xfe\x17\x88\x54\x2c\xb1\x23\xa3\x39\x39\x2a\x6c\x76\x05',
                     b'\xf2\xc2\x95\xf2\x7a\x96\xb9\x43\x59\x35\x80\x7a\x73\x59\xf6\x7f',
                     b'\x3d\x80\x47\x7d\x47\x16\xfe\x3e\x1e\x23\x7e\x44\x6d\x7a\x88\x3b',
                     b'\xef\x44\xa5\x41\xa8\x52\x5b\x7f\xb6\x71\x25\x3b\xdb\x0b\xad\x00',
                     b'\xd4\xd1\xc6\xf8\x7c\x83\x9d\x87\xca\xf2\xb8\xbc\x11\xf9\x15\xbc',
                     b'\x6d\x88\xa3\x7a\x11\x0b\x3e\xfd\xdb\xf9\x86\x41\xca\x00\x93\xfd',
                     b'\x4e\x54\xf7\x0e\x5f\x5f\xc9\xf3\x84\xa6\x4f\xb2\x4e\xa6\xdc\x4f',
                     b'\xea\xd2\x73\x21\xb5\x8d\xba\xd2\x31\x2b\xf5\x60\x7f\x8d\x29\x2f',
                     b'\xac\x77\x66\xf3\x19\xfa\xdc\x21\x28\xd1\x29\x41\x57\x5c\x00\x6e',
                     b'\xd0\x14\xf9\xa8\xc9\xee\x25\x89\xe1\x3f\x0c\xc8\xb6\x63\x0c\xa6']
        schedule2 = [b'\x8e\x73\xb0\xf7\xda\x0e\x64\x52\xc8\x10\xf3\x2b\x80\x90\x79\xe5',
                     b'\x62\xf8\xea\xd2\x52\x2c\x6b\x7b\xfe\x0c\x91\xf7\x24\x02\xf5\xa5',
                     b'\xec\x12\x06\x8e\x6c\x82\x7f\x6b\x0e\x7a\x95\xb9\x5c\x56\xfe\xc2',
                     b'\x4d\xb7\xb4\xbd\x69\xb5\x41\x18\x85\xa7\x47\x96\xe9\x25\x38\xfd',
                     b'\xe7\x5f\xad\x44\xbb\x09\x53\x86\x48\x5a\xf0\x57\x21\xef\xb1\x4f',
                     b'\xa4\x48\xf6\xd9\x4d\x6d\xce\x24\xaa\x32\x63\x60\x11\x3b\x30\xe6',
                     b'\xa2\x5e\x7e\xd5\x83\xb1\xcf\x9a\x27\xf9\x39\x43\x6a\x94\xf7\x67',
                     b'\xc0\xa6\x94\x07\xd1\x9d\xa4\xe1\xec\x17\x86\xeb\x6f\xa6\x49\x71',
                     b'\x48\x5f\x70\x32\x22\xcb\x87\x55\xe2\x6d\x13\x52\x33\xf0\xb7\xb3',
                     b'\x40\xbe\xeb\x28\x2f\x18\xa2\x59\x67\x47\xd2\x6b\x45\x8c\x55\x3e',
                     b'\xa7\xe1\x46\x6c\x94\x11\xf1\xdf\x82\x1f\x75\x0a\xad\x07\xd7\x53',
                     b'\xca\x40\x05\x38\x8f\xcc\x50\x06\x28\x2d\x16\x6a\xbc\x3c\xe7\xb5',
                     b'\xe9\x8b\xa0\x6f\x44\x8c\x77\x3c\x8e\xcc\x72\x04\x01\x00\x22\x02']
        schedule3 = [b'\x60\x3d\xeb\x10\x15\xca\x71\xbe\x2b\x73\xae\xf0\x85\x7d\x77\x81',
                     b'\x1f\x35\x2c\x07\x3b\x61\x08\xd7\x2d\x98\x10\xa3\x09\x14\xdf\xf4',
                     b'\x9b\xa3\x54\x11\x8e\x69\x25\xaf\xa5\x1a\x8b\x5f\x20\x67\xfc\xde',
                     b'\xa8\xb0\x9c\x1a\x93\xd1\x94\xcd\xbe\x49\x84\x6e\xb7\x5d\x5b\x9a',
                     b'\xd5\x9a\xec\xb8\x5b\xf3\xc9\x17\xfe\xe9\x42\x48\xde\x8e\xbe\x96',
                     b'\xb5\xa9\x32\x8a\x26\x78\xa6\x47\x98\x31\x22\x29\x2f\x6c\x79\xb3',
                     b'\x81\x2c\x81\xad\xda\xdf\x48\xba\x24\x36\x0a\xf2\xfa\xb8\xb4\x64',
                     b'\x98\xc5\xbf\xc9\xbe\xbd\x19\x8e\x26\x8c\x3b\xa7\x09\xe0\x42\x14',
                     b'\x68\x00\x7b\xac\xb2\xdf\x33\x16\x96\xe9\x39\xe4\x6c\x51\x8d\x80',
                     b'\xc8\x14\xe2\x04\x76\xa9\xfb\x8a\x50\x25\xc0\x2d\x59\xc5\x82\x39',
                     b'\xde\x13\x69\x67\x6c\xcc\x5a\x71\xfa\x25\x63\x95\x96\x74\xee\x15',
                     b'\x58\x86\xca\x5d\x2e\x2f\x31\xd7\x7e\x0a\xf1\xfa\x27\xcf\x73\xc3',
                     b'\x74\x9c\x47\xab\x18\x50\x1d\xda\xe2\x75\x7e\x4f\x74\x01\x90\x5a',
                     b'\xca\xfa\xaa\xe3\xe4\xd5\x9b\x34\x9a\xdf\x6a\xce\xbd\x10\x19\x0d',
                     b'\xfe\x48\x90\xd1\xe6\x18\x8d\x0b\x04\x6d\xf3\x44\x70\x6c\x63\x1e']
        self.assertEqual(schedule1,generated1)
        self.assertEqual(schedule2,generated2)
        self.assertEqual(schedule3,generated3)

    def test_rot_word(self):
        word = [0x01,0x02,0x03,0x04]
        rotated = [0x02,0x03,0x04,0x01]
        self.assertEqual(rotated,key_schedule.rot_word(word))
        word = [0x00,0x00,0x00,0x00]
        rotated = [0x00,0x00,0x00,0x00]
        self.assertEqual(rotated,key_schedule.rot_word(word))
        word = [0x01,0x02,0x01,0x02]
        rotated = [0x02,0x01,0x02,0x01]
        self.assertEqual(rotated,key_schedule.rot_word(word))

    def test_sub_word(self):
        word = [0x12,0x34,0x56,0x78]
        substituted = [0xc9,0x18,0xb1,0xbc]
        self.assertEqual(substituted,key_schedule.sub_word(word))
        word = [0xff,0xff,0xff,0xff]
        substituted = [0x16,0x16,0x16,0x16]
        self.assertEqual(substituted,key_schedule.sub_word(word))
        word = [0x87,0x65,0x43,0x21]
        substituted = [0x17,0x4d,0x1a,0xfd]
        self.assertEqual(substituted,key_schedule.sub_word(word))

    def test_xor_words(self):
        word1 = [0xff,0xff,0xff,0xff]
        word2 = [0x00,0x00,0x00,0x00]
        xored = [0xff,0xff,0xff,0xff]
        self.assertEqual(xored,key_schedule.xor_words(word1,word2))
        word1 = [0x00,0x00,0x00,0x00]
        word2 = [0x12,0x34,0x56,0x78]
        xored = [0x12,0x34,0x56,0x78]
        self.assertEqual(xored,key_schedule.xor_words(word1,word2))
        word1 = [0x0f,0x00,0x11,0x00]
        word2 = [0x00,0xf0,0x00,0x77]
        xored = [0x0f,0xf0,0x11,0x77]
        self.assertEqual(xored,key_schedule.xor_words(word1,word2))
        word1 = [0x12,0x34,0x56,0x78]
        word2 = [0x87,0x65,0x43,0x21]
        xored = [0x95,0x51,0x15,0x59]
        self.assertEqual(xored,key_schedule.xor_words(word1,word2))

if __name__ == "__main__":
    unittest.main()