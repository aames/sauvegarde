__author__ = 'Andrew'
import unittest
import os
from CopyUtils import ChecksumCalculator


class TestCopyUtils(unittest.TestCase):
    def setUp(self):
        f = open(os.path.dirname(__file__)+"\\temp", 'w')
        f.write("one")
        f.close()
        f1 = open(os.path.dirname(__file__)+"\\temp1", 'w')
        f1.write("one")
        f1.close()
        f2 = open(os.path.dirname(__file__)+"\\temp2", 'w')
        f2.write("oneo")
        f2.close()

    def test_checksum(self):
        cc = ChecksumCalculator()
        self.assertEqual(cc.calculate_checksum(os.path.dirname(__file__)+"\\temp"), cc.calculate_checksum(os.path.dirname(__file__)+"\\temp1"))

    def test_checksum_neg(self):
        cc = ChecksumCalculator()
        self.assertNotEqual(cc.calculate_checksum(os.path.dirname(__file__)+"\\temp"), cc.calculate_checksum(os.path.dirname(__file__)+"\\temp2"))


    def test_copy_file(self):
        pass
        #self.assertEqual(call, result)

    def tearDown(self):
        try:
            os.remove("temp")
            os.remove("temp1")
            os.remove("temp2")
        except WindowsError as e:
            #Windows is known for locking files (blame Anti-v etc...) Re-try after a snooze
            import time
            time.sleep(1)
            os.remove("temp")
            os.remove("temp1")
            os.remove("temp2")
        except:
            print("error removing temp files!")

'''
if __name__ == '__main__':
    unittest.main()
    import sys
    sys.path.append(os.path.abspath(__file__))
    '''