import matplotlib.pyplot as plt
import matplotlib.animation as animation



def animated_plot(ocean, shoal):
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_axes([0, 0, ocean.side_length, ocean.side_length], frameon=False)
    ax.set_xlim(0, ocean.side_length), ax.set_xticks([])
    ax.set_ylim(0, ocean.side_length), ax.set_yticks([])
    x = [fish.x_coord for fish in shoal.fish]
    y = [fish.y_coord for fish in shoal.fish]
    scat = ax.scatter(x, y)

    def move(shoal):
        shoal.move(10)
        x = [fish.x_coord for fish in shoal.fish]
        y = [fish.y_coord for fish in shoal.fish]
        scat.set_offsets(x, y)

    ani = animation.FuncAnimation(fig, move, 10, fargs=shoal)
    plt.show()

