import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig, ax = plt.subplots()
ax.grid()
ax.set_xlim(-4, 4)
x = np.linspace(0, 100, 500)
y = np.random.randn(500)

plotdata = []


def run(i, y):
    print(i)
    # time.sleep(5)
    if len(plotdata) > 0:
        plotdata.pop().remove()
    # update the data
    print(y)
    for _ in range(i+1):
        y = np.concatenate((y, np.random.randn(500)))
    bins = 100
    print(y)
    hist, bins_ = np.histogram(y.ravel(), bins=bins, density=True)
    bins_range = bins_.max() + np.abs(bins_.min())
    plot_bar = ax.bar(bins_[:-1], hist, width=bins_range/bins, color='pink')
    plotdata.append(plot_bar)
    y_mean = y.mean()
    y_std = y.std()
    ax.set_title("mean="+str(y_mean)[:6]+" ,std="+str(y_std)[:6])


ani = animation.FuncAnimation(fig, run, 50, fargs=(y,), blit=False, interval=200,
                              repeat=False)
plt.show()
