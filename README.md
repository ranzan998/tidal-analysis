# tidal-analysis
Using csv data file having ocean current data at one location to find the tidal constituents.

1. first take the csv file and read by pandas.read_csv()
2. get the tidal constituents from it, and save it as another csv file. this is later used to get the reconstructed tide.
3. use the data from both these files to plot
4. calculate residue from the difference of zonal and tidal_fit components(tide.u from reconstruction)
