import os
import matplotlib as mpl
import matplotlib.pyplot as plt

# from PIL import Image

fontDict1 = {
    "family": "Verdana",
    "weight": "bold",
    "size": 20
}

plt.rc("font", **fontDict1)
mpl.rcParams["ytick.major.pad"] = "8"
mpl.rcParams["xtick.major.pad"] = "8"

imagePos1 = 0


class plot():

    def __init__(self, stub1, rlen1=1, clen1=1, dpi1=72, width1=640, height1=480):
        self.stub1 = stub1
        self.rlen1 = rlen1
        self.clen1 = clen1
        self.dpi1 = dpi1
        self.width1 = width1
        self.height1 = height1
        self.figSize1 = (self.width1 / self.dpi1, self.height1 / self.dpi1)
        self.fig1, self.ax1 = plt.subplots(self.rlen1, self.clen1, figsize=self.figSize1, dpi=self.dpi1)

    def save(self, type1="png", tight1="tight"):
        global imagePos1
        imagePos1 += 1
        self.type1 = type1
        self.tight1 = tight1
        self.saveFs1 = "./{0:s}-0{1:d}.{2:s}".format(self.stub1, imagePos1, self.type1)
        self.fig1.savefig(self.saveFs1, bbox_inches=tight1)
        # self.savedImage1 = Image.open(self.saveFs1)
        # self.savedWidth1, self.savedHeight1= self.savedImage1.size
        # (_, _, _, _, _, _, self.savedSize1, _, self.savedTime1, _) = os.stat(self.saveFs1)
        print("\t{0:s} ".format(self.saveFs1))


print("(module rsPlot imported)")
