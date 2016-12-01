from Looped_CV_Data import plot_looped_data
import matplotlib.pyplot as plt
import numpy as np
import os
directory = '/Users/st659/Google Drive/Celll Ref Measurements 28-11-16'
directory2 = '/Users/st659/Google Drive/Cell 1 Reference Measurement'
voltage_list, current_list =plot_looped_data(directory)


max_current_list = list()
max_voltage_list = list()
for current, voltage in zip(current_list, voltage_list):
    max_current = max(current)
    max_current_arg = np.argmax(current)
    max_current_list.append(max_current)
    max_voltage_list.append(voltage[max_current_arg])

time_points = np.linspace(0,len(max_current_list)*10, num=len(max_current_list))
plt.style.use(['seaborn-white','seaborn-poster'])
fig = plt.figure()
ax = fig.add_subplot(111)
for volt, curr in zip(voltage_list, current_list):
    ax.plot(volt,curr)
ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Current (mA)')
ax.set_title('Cyclic Voltammetry of On Chip Electrode Array of 100 $\mu$M Methylene Blue over 6 Hours', y=1.04)
plt.savefig(os.path.join(directory,'CV On Chip MB 28-11-16 300dpi.png'), dpi=300)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax3 = ax2.twinx()
ax2.plot(time_points, max_current_list, label='Current')
ax3.plot(time_points, max_voltage_list, color='g', label='Voltage')
ax2.set_title('Maximum Current and Corresponding Voltage of CV of 100 $\mu$M Methylene Blue over 6 Hours', y=1.04)
ax2.set_xlabel('Time (Mins)')
ax2.set_ylabel('Current (mA)')
ax3.set_ylabel('Voltage (V)')
ax2.legend(loc=(0.1,0.15))
ax3.legend(loc=(0.1,0.1))
plt.savefig(os.path.join(directory,'Max current On Chip MB 28-11-16 300dpi.png'), dpi=300)
