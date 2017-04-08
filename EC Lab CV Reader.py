import unittest

class CV_Reader_Test(unittest.Testcase):
    def setUp(self):
        filename = 'E:\Chrome Download\\blank_1_2.mpt'
        self.reader = CV_Reader(filename)

    def test_get_cv_data(self):
        self.assertEqual(self.reader.forward, 1000)
        self.assertEqual(self.reader.reverse, 1000)


class CV_Reader():
    def __init__(self, filename):
        self.forward = list()
        self.reverse = list()

        self.forward, self.reverse = get_cv_data(filename)

    def get_cv_data(filename):
        with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            file_lines = file.readlines()

            header_line = get_header_line_number(file_lines)
            current_forward = list()
            reverse = list()
            voltage_reverse = list()
            forward = list()
            for line in file_lines[header_line:]:
                sl = line.split()

                if int(float(sl[1])) == 1:
                    forward.append([float(sl[7]), float(sl[8])])
                    current_forward.append(float(sl[8]))
                elif int(float(sl[1])) == 0:
                    reverse.append([float(sl[7]), float(sl[8])])

            forward.sort()
            reverse.sort()

            return forward, reverse


