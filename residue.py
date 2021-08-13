# to solve the tide
coef = utide.solve(time, df['u_comp_all'], lat = 12, method='ols', conf_int='MC')

tide = utide.reconstruct(time,coef)

t = tide.t_mpl

fig, (ax0,ax1,ax2) = plt.subplots(nrows=3,sharey=False,sharex=True)

df['residue'] = df['u_comp_all'] - tide.h
