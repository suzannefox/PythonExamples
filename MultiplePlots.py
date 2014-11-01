# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 09:19:16 2014

@author: Suzanne
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


data_path = 'C:/Users/Public/Documents/MSc-DataScience/INM430/Data/'
data_file = 'censusCrimeClean.csv'
dirty_file = 'censusCrime.csv'

csv_census = pd.read_csv(data_path + data_file)

# --------------------------------------------------------------------------
numpyArray = csv_census.as_matrix(["medIncome", "ViolentCrimesPerPop"])
arr1 = numpyArray[:,0] # now this holds "medIncome" values
arr2 = numpyArray[:,1] # this holds "ViolentCrimesPerPop" values

# -----------------------------------------------------------------------
# Example of doing x and y histograms around the scatterplot
# -----------------------------------------------------------------------

# the random data
x = arr1
y = arr2

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
bottom_h = left_h = left+width+0.02

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom_h, width, 0.2]
rect_histy = [left_h, bottom, 0.2, height]

# start with a rectangular Figure
plt.figure(1, figsize=(8,8))

axScatter = plt.axes(rect_scatter)
axHistx = plt.axes(rect_histx)
axHisty = plt.axes(rect_histy)

# no labels
#axHistx.xaxis.set_major_formatter(nullfmt)
#axHisty.yaxis.set_major_formatter(nullfmt)

# the scatter plot:
axScatter.scatter(x, y)

binwidth = .1
xymax = np.max( [np.max(np.fabs(x)), np.max(np.fabs(y))] )
lim = ( int(xymax/binwidth) + 1) * binwidth

#axScatter.set_xlim( (-lim, lim) )
#axScatter.set_ylim( (-lim, lim) )

bins = np.arange(-lim, lim + binwidth, binwidth)
axHistx.hist(x, bins=bins)
axHisty.hist(y, bins=bins, orientation='horizontal')

axHistx.set_xlim( axScatter.get_xlim() )
axHisty.set_ylim( axScatter.get_ylim() )

plt.show()


# ------------------------------------------------------------
# Doing several plots on a page
# Arguments - 211 (which could also be written in 3-tuple form as (2,1,1) means two rows 
# of plot windows; one column; the third digit specifies the positining relative to the 
# other subplot windows--in this case, this is the first plot (which places it on row 1, 
# hence the 1. plot number one," and the argument passed to the second call to add_subplot, 
# differs from the first only by the trailing digit (a 2 instead of a 1, because this plot 
# is the second plot.
# A bigger example: if instead you wanted four plots on a page, in a 2x2 matrix configuration, 
# you would call the add_subplot method four times, passing in these four 
# arguments (221), (222), (223), and (224), to create four plots on a 
# page at 10, 2, 8, and 4 o'clock, respectively and in this order.
# ------------------------------------------------------------

fig = plt.figure()
plt.title("Four plots")

ax1 = fig.add_subplot(221)
ax1.plot([(1, 2), (3, 4)], [(4, 3), (2, 3)])
ax2 = fig.add_subplot(222)
ax2.plot([(7, 2), (5, 3)], [(1, 6), (9, 5)])
ax3 = fig.add_subplot(223)
ax3.plot([(7, 2), (5, 3)], [(1, 6), (9, 5)])
ax4 = fig.add_subplot(224)
ax4.plot([(7, 2), (5, 3)], [(1, 6), (9, 5)])

plt.show()

# Another multiple chars example

#import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=4, ncols=4)
fig.tight_layout() # Or equivalently,  "plt.tight_layout()"

plt.show()

# ===================================================================
# Multiple charts, 1 row
# ===================================================================

# Test data
x = np.random.random(10)
y = np.random.random(10)

# Four axes, returned as a 2-d array  
plot_rows = 1
plot_cols = 2

fig, axarr = plt.subplots(plot_rows, plot_cols)
fig.tight_layout()

# Histogram of the input data
# use azarr[r, c] if r > 1
axarr[0].hist(x)
axarr[0].set_title("x variable")

# Histogram of the normal distribution
axarr[1].hist(y)
axarr[1].set_title('y variable')

plt.show()

# ===================================================================
# Multiple charts, 2 x 3
# ===================================================================

# Test data
x = np.random.random(10)
y = np.random.random(10)

# Four axes, returned as a 2-d array  
plot_rows = 2
plot_cols = 3

fig, axarr = plt.subplots(plot_rows, plot_cols)
fig.tight_layout()

# ============================
# Row 0 
# ============================
# Scatter of x by y
axarr[0, 0].scatter(x, y)
axarr[0, 0].set_title('x x y variable')
# Histogram of the input data
axarr[0, 1].hist(x)
axarr[0, 1].set_title('x variable')


# ============================
# Row 1
# ============================
# Scatter of y by x
axarr[1, 0].scatter(y, x)
axarr[1, 0].set_title('y x x variable')
# Histogram of the normal distribution
axarr[1, 1].hist(y)
axarr[1, 1].set_title('y variable')

plt.show()
