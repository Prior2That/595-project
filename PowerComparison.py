import matplotlib.pyplot as plt
import numpy as np

mem_type = ['RRAM', 'PCM', 'MRAM','FeRAM'] #each memory type analyzed
p_read = [] # power consumed for each read operation
p_write = [] # power consumed for each write operation

barwidth = 0.3
fig = plt.subplots(figsize= (10,7))

br1 = np.arange(len(mem_type))
br2 = [x + barwidth for x in br1]

plt.bar(br1, p_read, width=barwidth,edgecolor = 'grey', label = 'Read Op')
plt.bar(br2, p_write, width=barwidth,edgecolor = 'grey', label = 'Write Op')

plt.xlabel('Memory Type', fontweight = 'bold', fontsize = 15)
plt.ylabel('Unit Power Consumption (J)', fontweight = 'bold', fontsize = 15)
plt.xticks([r + barwidth/2 for r in range(len(p_read))],mem_type)

plt.legend()
plt.show()