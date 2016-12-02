from Meth_blue_06_09 import get_header_line_number
from Meth_blue_06_09 import get_data_paths
import codecs
import numpy as np
import matplotlib.pyplot as plt

def get_looped_cv_data(filename):
    with codecs.open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        file_lines = file.readlines()

        header_line = get_header_line_number(file_lines)
        current_forward= list()
        reverse=list()
        voltage_reverse=list()
        forward = list()
        for line in file_lines[header_line:]:
            sl = line.split()

            if int(float(sl[1])) == 1:
                forward.append([float(sl[7]), float(sl[8]), int(float(sl[9]))])
                current_forward.append(float(sl[8]))

            elif int(float(sl[1])) == 0:
                reverse.append([float(sl[7]), float(sl[8]), int(float(sl[9]))])

        forward_cycle = list()
        reverse_cycle = list()
        forward_cycle_list = list()
        reverse_cycle_list = list()
        current_cycle = forward[0][2]

        for reading_forward, reading_reverse in zip(forward,reverse):
            if reading_forward[2] == current_cycle:
                forward_cycle.append(reading_forward)
                reverse_cycle.append(reading_reverse)

            else:
                forward_cycle_list.append(forward_cycle)
                reverse_cycle_list.append(reverse_cycle)
                forward_cycle = list()
                reverse_cycle = list()
                current_cycle = reading_forward[2]
                forward_cycle.append(reading_forward)
                reverse_cycle.append(reading_reverse)



        second_cv_forward = forward_cycle_list[-1]
        second_cv_reverse = reverse_cycle_list[-1]
        second_cv_forward.sort()
        second_cv_reverse.sort()

        return second_cv_forward, second_cv_reverse



def plot_looped_data(directory):
    file_list = get_data_paths(directory)
    print(len(file_list))
    file_list.pop(0)
    voltage_list = list()
    current_list = list()
    for file in file_list:
        print(file)
        for_voltage = list()
        rev_voltage = list()
        for_current = list()
        rev_current = list()
        forward,reverse = get_looped_cv_data(file)
        for reading_for, reading_rev in zip(forward,reverse):
            for_voltage.append(reading_for[0])
            rev_voltage.append(reading_rev[0])
            for_current.append(reading_for[1])
            rev_current.append(reading_rev[1])
        forward_np = np.array(forward)
        reverse_np = np.array(reverse)
        voltage = np.concatenate((for_voltage, rev_voltage[::-1]), axis=0)
        current = np.concatenate((for_current, rev_current[::-1]), axis=0)
        voltage_list.append(voltage)
        current_list.append(current)



    return voltage_list, current_list








