# tidal-analysis
Using csv data file having ocean current data at one location to find the tidal constituents.

1. first take the csv file and read by pandas.read_csv()
2. get the tidal constituents from it, and save it as another csv file. this is later used to get the reconstructed tide.
3. use the data from both these files to plot
4. calculate residue from the difference of zonal and tidal_fit components(tide.u from reconstruction)



When it comes to handling multiple files.. please use the master_script.py

comments are given there itself. A brief steps are given below,
>>      input files 
>>      sort the files
>>      fetch files length(timesteps) and store it for further use
>>      define functions to replace the names, variables, etc
>>      define functions to copy/rewrite a text/(control file for TASK) file
>>      start the loop
>>            open files
>>            define variables
>>            copy tira1m.ctl file
>>            use date.dt.strftime to get timestep values
>>            write tide.txt by fetching the U, V values (separately for each current)
>>         $$   run task for zonal current
>>         $$ write the tira.pri(file that contains tidal constituents information) as csv file, further export 
>>            
>>         $$ do the above $$ steps for meridional component too
>>         Load the outputs of tide1.out and tide2.out to getch the u-raw, u-tide, u-residual currents, same for meridional data as well
>>         export the data using xarray.Dataset creation method.
>>       $ if neeeded add the dimension of depth( was necessary for mine)
>>         add attributes to the variable and its coordinates
>>         convert calendar if needed
>>         Change the tira1m.ctl files inside variables, so as to proceed to next file with a new control file       
>>            
