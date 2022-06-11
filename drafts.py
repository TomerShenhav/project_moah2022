import random
import matplotlib.pyplot as plt

x = range(1, 101)
y1 = [random.randint(1, 100) for _ in range(len(x))]
y2 = [random.randint(1, 100) for _ in range(len(x))]

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.loglog(x, y1)
ax2.loglog(x, y2)

# Set common labels
#fig.text(0.5, 0.04, 'common xlabel', ha='center', va='center')
#fig.text(0.06, 0.5, 'common ylabel', ha='center', va='center', rotation='vertical')

ax1.set_title('ax1 title')
ax1.set_xlabel('ax1knelk')
ax2.set_title('ax2 title')
ax2.set_xlabel('rgkjrnge')

plt.show()
