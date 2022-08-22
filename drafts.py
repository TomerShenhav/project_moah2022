import random
import matplotlib.pyplot as plt


x=[14794, 173954, 920, 85808, 17337, 1546, 213733, 18697, 10077, 150985]
plt.figure('summary')
plt.hist(x, bins=[50000,100000,200000,300000,400000,500000,600000,700000] )
plt.xlabel('day number', fontsize=12)
plt.ylabel('amount of mosquitos', fontsize=12)
my_title = 'test'
plt.title(my_title)
plt.grid(True)
plt.show()
#
# x = range(1, 101)
# y1 = [random.randint(1, 100) for _ in range(len(x))]
# y2 = [random.randint(1, 100) for _ in range(len(x))]
#
# fig = plt.figure()
# ax1 = fig.add_subplot(211)
# ax2 = fig.add_subplot(212)
#
# .ax1.loglog(x, y1)
# ax2.loglog(x, y2)
#
# # Set common labels
# #fig.text(0.5, 0.04, 'common xlabel', ha='center', va='center')
# #fig.text(0.06, 0.5, 'common ylabel', ha='center', va='center', rotation='vertical')
#
# ax1.set_title('ax1 title')
# ax1.set_xlabel('ax1knelk')
# ax2.set_title('ax2 title')
# ax2.set_xlabel('rgkjrnge')
#
# plt.show()
