import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.grid()
ax.set_xlim(-4, 4)
x = np.linspace(0, 100, 500)
y = np.random.randn(500)

plotdata = []


def run(i, Rep):
    print(i)
    # time.sleep(5)
    if len(plotdata) > 0:
        plotdata.pop().remove()
    # update the data
    # for _ in range(i+1):
    #     y = np.concatenate((y, np.random.randn(500)))
    Rep = Rep[i]
    bins = 10
    hist, bins_ = np.histogram(y.ravel(), bins=bins, density=True)
    bins_range = bins_.max() + np.abs(bins_.min())
    plot_bar = ax.bar(bins_[:-1], hist, width=bins_range/bins, color='pink')
    plotdata.append(plot_bar)
    # y_mean = Rep.mean()
    # y_std = Rep.std()
    # ax.set_title("mean="+str(y_mean)[:6]+" ,std="+str(y_std)[:6])


ani = animation.FuncAnimation(fig, run, 50, fargs=(Rep,), blit=False, interval=200,
                              repeat=False)
plt.show()
