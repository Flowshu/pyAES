import unittest
import padding

class PaddingTest(unittest.TestCase):
    def test_apply_padding(self):
        message1, padding1 = b'', b''
        message2, padding2 = b'0123456', b'0123456' + 9*(b'\x09')
        message3, padding3 = b'01234567', b'01234567' + 8*(b'\x08')
        message4, padding4 = b'012345678', b'012345678' + 7*(b'\x07')
        message5, padding5 = b'0123456789ABCDEF', b'0123456789ABCDEF'
        message6, padding6 = b'11111111111111111', (b'1'*17) + (15*(b'\x0f'))
        self.assertEqual(padding.apply_padding(message1),padding1)
        self.assertEqual(padding.apply_padding(message2),padding2)
        self.assertEqual(padding.apply_padding(message3),padding3)
        self.assertEqual(padding.apply_padding(message4),padding4)
        self.assertEqual(padding.apply_padding(message5),padding5)
        self.assertEqual(padding.apply_padding(message6),padding6)

    def test_remove_padding(self):
        message1, padding1 = b'', b''
        message2, padding2 = b'0123456', b'0123456' + 9*(b'\x09')
        message3, padding3 = b'01234567', b'01234567' + 8*(b'\x08')
        message4, padding4 = b'012345678', b'012345678' + 7*(b'\x07')
        message5, padding5 = b'0123456789ABCDEF', b'0123456789ABCDEF'
        message6, padding6 = b'11111111111111111', (b'1'*17) + (15*(b'\x0f'))
        self.assertEqual(padding.remove_padding(padding1),message1)
        self.assertEqual(padding.remove_padding(padding2),message2)
        self.assertEqual(padding.remove_padding(padding3),message3)
        self.assertEqual(padding.remove_padding(padding4),message4)
        self.assertEqual(padding.remove_padding(padding5),message5)
        self.assertEqual(padding.remove_padding(padding6),message6)

if __name__ == "__main__":
    unittest.main()
