from astroplan.plots import plot_sky
import matplotlib.pyplot as plt
from astropy.time import Time


class AllSky:

    def __init__(self, height=400, width=400, objects=None):
        '''
        Initialize self with a height and width of the map and a list of
        objects to plot

        Parameters
        ----------
        height: int (optional)
            Height of the map in pixels

        width: int (optional)
            Width of the map in pixels

        objects: dictionary (optional)
            Dictionary holding objects with an RA and Dec for each
        '''

        self.height = height
        self.width = width
        self.objects = objects

    def draw(self, observer, time=None):
        '''
        Draw the plot to the screen

        Parameters
        ----------
        observer: `~astroplan.Observer`
            Astroplan observer object determining the location of the map

        time: `~astropy.time.Time` (optional)
            Time of the observation. If no time is given, it will default to
            the current local time
        '''

        if (time is None):
            time = Time(datetime.now())

        plt.ion()
        for key, val in self.objects.items():
            if (observer.target_is_up(time, val)):
                plot_sky(val, observer, time)
