import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc

params = {'text.usetex' : True,
          'font.size' : 8,
          'font.family' : 'lmodern',
          'text.latex.unicode' : True}
plt.rcParams['text.latex.preamble']=[r'\usepackage{lmodern}']
plt.rcParams.update(params)
colors = [ 'dimgrey', 'royalblue', 'orange', 'seagreen', 'y' ]

fig_width = 5.33


if __name__ == '__main__':

    # --> Define the function.
    f = lambda x, mu : mu - x**2

    # --> Define the mesh.
    x = np.linspace(-2, 2, 100)

    # --> Define the range of parameters.
    mu = np.array([-0.5, 0., 0.5])

    # --> Plot the figure.
    fig, axes = plt.subplots(1, 3, figsize=(fig_width, fig_width/3))

    for i, ax in enumerate(axes):

        ax.plot(x, f(x, mu[i]), color=colors[0], zorder=3)

        # --> Add Title and fixed points.
        if mu[i] < 0:
            ax.set_title(r'$\mu < 0$', y=-0.25)
        elif mu[i] > 0:
            ax.set_title(r'$\mu > 0$', y=-0.25)
            ax.plot(-np.sqrt(mu[i]), 0, marker='o', fillstyle='none', color='royalblue', zorder=4)
            ax.plot(np.sqrt(mu[i]), 0, 'o', color='royalblue', zorder=5)
        else:
            ax.set_title(r'$\mu = 0$', y=-0.25)
            ax.plot(np.sqrt(mu[i]), 0, marker='o', fillstyle='right', color='royalblue', zorder=4)

        # --> x axis.
        ax.set_xlim(-2, 2)
        ax.set_xticks([-1, 1])
        ax.set_xlabel(r'$x$')
        ax.xaxis.set_label_coords(1.1, 0.475)

        # --> y axis.
        ax.set_ylim(-0.75, 0.75)
        ax.set_yticks([])
        ax.set_ylabel(r'$\dot{x}$', rotation=0)
        ax.yaxis.set_label_coords(0.5, 1.05)

        #--> Remplace le cadre habituel de la figure par un systeme d'axes
        #    centre en (0, 0).
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data', 0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data',0))

        #--> Ajout des fleches au bout des axes.
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()

        # get width and height of axes object to compute
        # matching arrowhead length and width
        dps = fig.dpi_scale_trans.inverted()
        bbox = ax.get_window_extent().transformed(dps)
        width, height = bbox.width, bbox.height

        # manual arrowhead width and length
        hw = 1./20.*(ymax-ymin)/3
        hl = 1./20.*(xmax-xmin)
        lw = 1. # axis line width
        ohg = 0.3 # arrow overhang

        # compute matching arrowhead length and width
        yhw = hw/(ymax-ymin)*(xmax-xmin)* height/width
        yhl = hl/(xmax-xmin)*(ymax-ymin)* width/height

        # draw x and y axis
        ax.arrow(xmin, 0., xmax-xmin, 0., fc='k', ec='k', lw = lw,
                 head_width=hw, head_length=0.25*hl, overhang = ohg,
                 length_includes_head= True, clip_on = False, zorder=1)

        ax.arrow(0, ymin, 0., ymax-ymin, fc='k', ec='k', lw = lw,
                 head_width=yhw, head_length=0.25*yhl, overhang = ohg,
                 length_includes_head= True, clip_on = False, zorder=2)

    plt.savefig('../imgs/saddle_node_phase_line.pdf', bbox_inches='tight', dpi=300)





    ###############################

    mu = np.linspace(0.001, 1, 50)

    fig, ax = plt.subplots(1, 4, sharex=True, sharey=True, figsize=(fig_width, fig_width/3))

    #--> dx/dt = mu - x**2
    ax[0].plot(mu, np.sqrt(mu), color=colors[1])
    ax[0].plot(mu, -np.sqrt(mu), '--', color=colors[1])
    ax[0].set_title(r'$\dot{x} = \mu - x^2$')
    ax[0].set_xlabel(r'$\mu$')
    ax[0].set_ylabel(r'$x^*$', rotation=0)
    ax[0].set_xticks([-1, 0, 1])
    ax[0].set_yticks([-1, 0, 1])

    #--> dx/dt = -mu + x**2
    ax[1].plot(mu, -np.sqrt(mu), color=colors[1])
    ax[1].plot(mu, np.sqrt(mu), '--', color=colors[1])
    ax[1].set_title(r'$\dot{x} = -\mu + x^2$')
    ax[1].set_xlabel(r'$\mu$')

    #--> dx/dt = -mu - x**2
    ax[2].plot(-mu, np.sqrt(mu), color=colors[1])
    ax[2].plot(-mu, -np.sqrt(mu), '--', color=colors[1])
    ax[2].set_title(r'$\dot{x} = -\mu - x^2$')
    ax[2].set_xlabel(r'$\mu$')

    #--> dx/dt = mu + x**2
    ax[3].plot(-mu, -np.sqrt(mu), color=colors[1])
    ax[3].plot(-mu, np.sqrt(mu), '--', color=colors[1])
    ax[3].set_title(r'$\dot{x} = \mu + x^2$')
    ax[3].set_xlabel(r'$\mu$')

    plt.savefig('../imgs/saddle_node_bifurcation_diagrams.pdf', bbox_inches='tight', dpi=300)





    #######################

    def dynamical_sytem(x, t=None, mu=0.1):
        # --> Initialize variable.
        dx = np.zeros_like(x)

        # --> x-equation
        dx[0] = mu - x[0]**2

        # --> y-equation
        dx[1] = - x[1]

        return dx

    # --> Mesh of the phase plane.
    x = np.linspace(-2, 2)
    x, y = np.meshgrid(x, x)

    # --> Range of parameters.
    mu = np.array([-0.5, 0., 0.5])

    fig, axes = plt.subplots(1, 3, figsize=(fig_width, fig_width/3))

    for i, ax in enumerate(axes):
        # --> Compute xdot and ydot.
        xdot = np.zeros_like(x)
        ydot = np.zeros_like(y)

        xdot[:], ydot[:] = dynamical_sytem([x[:], y[:]], mu=mu[i])

        magnitude = np.sqrt(xdot[:]**2 + ydot[:]**2)
        ax.streamplot(x, y, xdot, ydot, color=magnitude, cmap=plt.cm.inferno, density=0.66, zorder=1)

        ax.set_xlabel(r'$x$')
        ax.set_aspect('equal')

        if mu[i] > 0:
            ax.plot(np.sqrt(mu[i]), 0, marker='o', color='royalblue', zorder=2)
            ax.plot(-np.sqrt(mu[i]), 0, marker='o', color='royalblue', fillstyle='none', zorder=3, markeredgewidth=2)
            ax.set_title(r'$\mu > 0$', y=-0.5)
            ax.set_yticklabels([])

        elif mu[i] == 0:
            ax.plot(0, 0, marker='o', color='royalblue', fillstyle='right', zorder=2)
            ax.set_title(r'$\mu = 0$', y=-0.5)
            ax.set_yticklabels([])

        else:
            ax.set_ylabel(r'$y$')
            ax.set_title(r'$\mu < 0$', y=-0.5)


    plt.savefig('../imgs/saddle_node_phase_plane.pdf', bbox_inches='tight', dpi=300)
    plt.show()
