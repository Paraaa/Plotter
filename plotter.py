import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import dataframe_image as dfi
from seaborn.relational import lineplot


"""
This class is used to visualize data.
@author: Andrej Schwanke
"""
class Plotter:
    
    """
    Creates a directory to save plots to
    
    Optional parameters
    ----------
    save_plots: if set to true every plot made is saved in 
    path: this value specifies the path the plots are stored
    format: specifies the image format the plots are stored with
    
    @author: Andrej Schwanke
    """
    def __init__(self, save_plots=False, path="./plots/", format="svg"):
        sns.set_style("darkgrid")
        self.save_plots = save_plots
        self.path = path
        self.format = format
        
        if self.save_plots: 
            try: 
                os.mkdir(self.path) 
            except FileExistsError:
                print("Directory", self.path, " already exists")

      
    """
    Create pairplot of given data
    @author: Andrej Schwanke
    """
    def pairplot(self, data, title=None):
        plot = sns.pairplot(data)
        if title:
            plot.fig.subplots_adjust(top=0.9)
            plot.fig.suptitle(title)

        if self.save_plots: 
            self.save_plot(plot, "pairplot")
        plt.clf()

       
    """
    Create scatterplot of given data
    @author: Andrej Schwanke
    """
    def scatterplot(self, data, x=None, y=None, title=None):
        plot = sns.scatterplot(x,y,data=data,legend="full") 
        if title:
            plot.set_title(title)

        if self.save_plots:
            self.save_plot(plot.get_figure(), "scatterplot")
        plt.clf()
    

    """
    Create lineplot of given data
    @author: Andrej Schwanke
    """
    def lineplot(self, data, x=None, y=None, title=None):
        plot = sns.lineplot(x,y, data=data)
        if title: 
            plot.set_title(title)

        if self.save_plots:
            self.save_plot(plot.get_figure(), "lineplot")
        plt.clf()

    """
    Create lineplot of given data
    @author: Andrej Schwanke
    """
    def catplot(self, data, x=None, y=None, title=None):
        plot = sns.catplot(x,y, data=data)
        if title: 
            plot.fig.subplots_adjust(top=0.9)
            plot.fig.suptitle(title)

        if self.save_plots:
            self.save_plot(plot, "catplot")
        plt.clf()

    """
    Create stripplot of given data
    @author: Andrej Schwanke
    """
    def stripplot(self, data, x=None, y=None, title=None):
        plot = sns.stripplot(x,y, data=data, jitter = 0.2)
        if title: 
            plot.set_title(title)

        if self.save_plots:
            self.save_plot(plot.get_figure(), "stripplot")
        plt.clf()


    """
    Create swarmplot of given data
    @author: Andrej Schwanke
    """
    def swarmplot(self, data, x=None, y=None, title=None):
        plot = sns.swarmplot(x,y, data=data)
        if title: 
            plot.set_title(title)

        if self.save_plots:
            self.save_plot(plot.get_figure(), "swarmplot")
        plt.clf()


    """
    Create violinplot of given data
    @author: Andrej Schwanke
    """
    def violinplot(self, data, x=None, y=None, title=None):
        plot = sns.violinplot(x,y, data=data)
        if title: 
            plot.set_title(title)

        if self.save_plots:
            self.save_plot(plot.get_figure(), "violinplot")
        plt.clf()

    """
    Create boxplot of given data
    @author: Andrej Schwanke
    """
    def boxplot(self, data, x=None, y=None, title=None):
        plot = sns.boxplot(x,y, data=data)
        if title: 
            plot.set_title(title)

        if self.save_plots:
            self.save_plot(plot.get_figure(), "boxplot")
        plt.clf()


    """
    Create boxenplot of given data
    @author: Andrej Schwanke
    """
    def boxenplot(self, data, x=None, y=None, title=None):
        plot = sns.boxenplot(x,y, data=data)
        if title: 
            plot.set_title(title)

        if self.save_plots:
            self.save_plot(plot.get_figure(), "boxenplot")
        plt.clf()

    """
    Create countplot of given data
    @author: Andrej Schwanke
    """
    def countplot(self, data, x=None, y=None, title=None):
        plot = sns.countplot(x,y, data=data)
        if title: 
            plot.set_title(title)

        if self.save_plots:
            self.save_plot(plot.get_figure(), "countplot")
        plt.clf()

    """
    Create barplot of given data
    @author: Andrej Schwanke
    """
    def barplot(self, data, x=None, y=None, title=None):
        plot = sns.barplot(x,y, data=data)
        if title: 
            plot.set_title(title)

        if self.save_plots:
            self.save_plot(plot.get_figure(), "barplot")
        plt.clf()


    """
    Create barplot of given data
    @author: Andrej Schwanke
    """
    def pointplot(self, data, x=None, y=None, title=None):
        plot = sns.pointplot(x,y, data=data)
        if title: 
            plot.set_title(title)

        if self.save_plots:
            self.save_plot(plot.get_figure(), "pointplot")
        plt.clf()

    """
    This method provide a oppertunity to save a pandas dataframe
    as an image. It uses the dataframe_image modul to do so. 
    Currently it is only possible to export the dataframe as an .png
    file.
    This method can only be called if save_plots is enabled. 
    The optional parameter sample specifies the amount of sample data
    should be visualized in the image file. A high sample size is not
    recommended.
    @author: Andrej Schwanke
    """
    def export_table_as_png(self, data, sample=25):
        if self.save_plots:
            data_styled = data.head(sample).style.background_gradient()
            self.save_plot(data_styled, "table")

    """
    Saves a plot in a given format 
    @author: Andrej Schwanke
    """
    def save_plot(self, plot, plot_type):
        d = datetime.now()
        timeStamp = f"{d.day}_{d.month}_{d.year}-{d.hour}:{d.minute}:{d.second}" 
        filename  = f"{plot_type}-{timeStamp}"  
        path      = f"{self.path}{filename}.{self.format}" 

        if plot_type == "table":
            path = f"{self.path}{filename}.png"
            dfi.export(plot, path)
        else: 
            plot.savefig(path) 
      

if __name__ == "__main__":
    plotter = Plotter(save_plots=True, format="png")

    #dataset = pd.read_csv("./dataset/data.csv")
    dataset = sns.load_dataset("iris")
    dataset_2 = sns.load_dataset("tips")

    plotter.export_table_as_png(dataset_2)
    plotter.pairplot(dataset, title="pairplot")
    plotter.scatterplot(dataset_2,title="Test123", x = "total_bill", y ="tip")
    plotter.lineplot(dataset_2,title="testdfsdf", x="tip" , y="total_bill")
    plotter.catplot(dataset_2, title="Test123", x = "tip", y ="sex")
    plotter.stripplot(dataset_2, title="Test123", x = "tip", y ="sex")
    plotter.swarmplot(dataset_2, title="Test123", x = "tip", y ="sex")
    plotter.violinplot(dataset_2, title="Test23123", x="total_bill")
    plotter.boxplot(dataset_2, title="Test23123")
    plotter.boxenplot(dataset_2, title="BOX", y="tip")
    plotter.countplot(dataset_2, y="sex")
    plotter.barplot(dataset_2, y="total_bill", x="sex")
    plotter.pointplot(dataset_2, y="total_bill", x="tip")