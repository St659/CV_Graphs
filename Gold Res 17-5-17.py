from Meth_blue_06_09 import get_data_paths, calculate_graph_data
import matplotlib.pyplot as plt
import os

directory = '/Users/st659/Google Drive/ITO Resazurin 17-5-17/Resazurin/Gold'
directory2 = '/Users/st659/Google Drive/ITO Resazurin 17-5-17/MB/SHU'
paths = get_data_paths(directory)

paths_2 = get_data_paths(directory2)
blank = paths[:2]
mg = paths[2:]


mg_pseudo = paths_2[2:]

plt.style.use(['seaborn-white', 'seaborn-notebook'])
data_list = list()
data_list_2 = list()



# fig = plt.figure()
fig2 = plt.figure()

# ax = fig.add_subplot(111)
ax = fig2.add_subplot(111)
#ax2 = fig2.add_subplot(122)

# for path in paths_list:


for pb_path in paths:
    print(pb_path)
    no, pb, legend = calculate_graph_data(pb_path)
    #esfe, shu, seg = calculate_graph_data(shu_path)

    #legend_str = path[0].split('/')[-1]
    #legend = legend_str.split('_')[0]
    #ax.plot(shu[0], shu[1])
    ax.plot(pb[0], pb[1])

#plt.xlim((-0.6,0))
#plt.ylim((-0.06, 0.02))
#plt.legend(loc = 'lower right')
#plt.title('E.coli MG1655 Pseudo starting at 10^5 CFU/ml after 5 hours Incubation with 1mM Resazurin')
ax.set_xlabel('Voltage vs AgAgCl (V)')
ax.set_ylabel('Current (mA)')
#ax2.set_xlabel('Voltage vs AgAgCl (V)')

plt.savefig(os.path.join(directory,'Resazurin_Gold_17-5-17.png'), dpi=300)
plt.show()
