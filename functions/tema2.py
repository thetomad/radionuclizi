import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy.optimize import curve_fit

def objective(x, a, b, c):
	return a * np.exp(-b * x) + c


def tema2(year, linie):
    data = pd.read_csv(f'./databases/{year}/AUDI{year}.csv')

    D = data['D']

    S_n = [np.nan for i in range(linie)]
    for i in range(linie, len(D)):

        row = data.iloc[i]

        a = data.loc[(data['A'] == row.A-1) & (data["Z"] == row.Z)].D
        b = data.loc[(data['A'] == row.A)   & (data['Z']== row.Z)].D
        
        if a.empty:
            S_n.append(np.nan)
        else:
            s = a.iat[0] + data.iat[0,4] - b.iat[0]
            S_n.append(s)

    S_p = [np.nan for i in range(linie)]
    for i in range(linie, len(D)):

        row = data.iloc[i]

        a = data.loc[(data['A'] == row.A-1) & (data["Z"] == row.Z-1)].D
        b = data.loc[(data['A'] == row.A)   & (data['Z']== row.Z)].D
        
        if a.empty:
            S_p.append(np.nan)
        else:
            s = a.iat[0] + data.iat[1,4] - b.iat[0]
            S_p.append(s)
            
    S_alpha = [np.nan for i in range(linie)]
    for i in range(linie, len(D)):

        row = data.iloc[i]

        a = data.loc[(data['A'] == row.A-4) & (data["Z"] == row.Z-2)].D
        b = data.loc[(data['A'] == row.A)   & (data['Z']== row.Z)].D
        
        if a.empty:
            S_alpha.append(np.nan)
        else:
            s = a.iat[0] + data.iat[6,4] - b.iat[0]
            S_alpha.append(s)

    S_d = [np.nan for i in range(linie)]
    for i in range(linie, len(D)):

        row = data.iloc[i]

        a = data.loc[(data['A'] == row.A-2) & (data["Z"] == row.Z-1)].D
        b = data.loc[(data['A'] == row.A)   & (data['Z']== row.Z)].D
        
        if a.empty:
            S_d.append(np.nan)
        else:
            s = a.iat[0] + data.iat[2,4] - b.iat[0]
            S_d.append(s)
            
    N = []

    for i in range(len(D)):
        n=data.iloc[i].A - data.iloc[i].Z
        N.append(n)


    data['N'] = N

    data['S_n'] = S_n
    data['S_p'] = S_p
    data['S_alpha'] = S_alpha
    data['S_d'] = S_d

    N_Z = []
    for i in range(len(D)):

        n_z = data.iloc[i].N  /  data.iloc[i].Z
        N_Z.append(n_z)

    data['N_Z'] = N_Z

    data.to_csv(f'./databases/{year}/AUDI{year}.csv')
    
    ee_data=data.loc[(data['A'] % 2 == 0) & (data['Z'] % 2 == 0)]
    eo_data=data.loc[(data['A'] % 2 == 0) & (data['Z'] % 2 == 1)]
    oe_data=data.loc[(data['A'] % 2 == 1) & (data['Z'] % 2 == 0)]
    oo_data=data.loc[(data['A'] % 2 == 1) & (data['Z'] % 2 == 1)]

    plt.figure(figsize=(20, 10))
    plt.xlabel('A',fontsize=20)
    plt.ylabel('Neutron separation energy (MeV)',fontsize=20)

    ax = plt.subplot(111)

    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))

    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))

    ax.xaxis.grid(True,'minor',linestyle='-.')
    ax.yaxis.grid(True,'minor',linestyle='-.')
    ax.xaxis.grid(True,'major',linewidth=1.5,linestyle='-.')
    ax.yaxis.grid(True,'major',linewidth=1.5,linestyle='-.')

    plt.scatter(ee_data.A, ee_data.S_n/1000, label='e_e')
    plt.scatter(eo_data.A, eo_data.S_n/1000, label='e_o')
    plt.scatter(oe_data.A, oe_data.S_n/1000, label='o_e')
    plt.scatter(oo_data.A, oo_data.S_n/1000, label='o_o')

    plt.legend(loc = 'upper right')
    plt.xlim(0,270)
    plt.ylim(0,25)
    plt.savefig(f'./images/tema2/{year}/Neutron_separation.png')

    
    plt.figure(figsize=(20, 10))
    plt.xlabel('A',fontsize=20)
    plt.ylabel('Protron separation energy (MeV)',fontsize=20)

    ax = plt.subplot(111)

    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))

    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))

    ax.xaxis.grid(True,'minor',linestyle='-.')
    ax.yaxis.grid(True,'minor',linestyle='-.')
    ax.xaxis.grid(True,'major',linewidth=1.5,linestyle='-.')
    ax.yaxis.grid(True,'major',linewidth=1.5,linestyle='-.')

    plt.scatter(ee_data.A, ee_data.S_p/1000, label='e_e')
    plt.scatter(eo_data.A, eo_data.S_p/1000, label='e_o')
    plt.scatter(oe_data.A, oe_data.S_p/1000, label='o_e')
    plt.scatter(oo_data.A, oo_data.S_p/1000, label='o_o')

    plt.legend(loc = 'upper right')
    plt.xlim(0,270)
    plt.ylim(0,25)
    plt.savefig(f'./images/tema2/{year}/Protron_separation.png')

    plt.figure(figsize=(20, 10))
    plt.xlabel('A',fontsize=20)
    plt.ylabel('Alpha separation energy (MeV)',fontsize=20)

    ax = plt.subplot(111)

    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))

    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))

    ax.xaxis.grid(True,'minor',linestyle='-.')
    ax.yaxis.grid(True,'minor',linestyle='-.')
    ax.xaxis.grid(True,'major',linewidth=1.5,linestyle='-.')
    ax.yaxis.grid(True,'major',linewidth=1.5,linestyle='-.')

    plt.scatter(data.A, data.S_alpha/1000)

    # plt.legend(loc = 'upper right')
    plt.xlim(0,270)
    plt.ylim(-15,25)
    plt.savefig(f'./images/tema2/{year}/Alpha_separation.png')


    plt.figure(figsize=(20, 10))
    plt.xlabel('A',fontsize=20)
    plt.ylabel('Deuteron separation energy (MeV)',fontsize=20)

    ax = plt.subplot(111)

    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))

    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))

    ax.xaxis.grid(True,'minor',linestyle='-.')
    ax.yaxis.grid(True,'minor',linestyle='-.')
    ax.xaxis.grid(True,'major',linewidth=1.5,linestyle='-.')
    ax.yaxis.grid(True,'major',linewidth=1.5,linestyle='-.')

    plt.scatter(data.A, data.S_d/1000)


    # plt.legend(loc = 'upper right', prop ={'size':30})
    plt.xlim(0,270)
    plt.ylim(0,30)
    plt.savefig(f'./images/tema2/{year}/Deuteron_separation.png')

    plt.figure(figsize=(20, 10))
    plt.xlabel('N/Z', fontsize = 20)
    plt.ylabel('Neutron separation energy (MeV)',  fontsize = 20)

    plt.scatter(data.N_Z, data.S_n/1000)
    
    

    datac = data
    datac.dropna(inplace=True)


    popt, pcov = curve_fit(objective, datac.N_Z, datac.S_n/1000)
    x_line = np.arange(min(datac.N_Z),max(datac.N_Z), 0.001)
    plt.plot(x_line, objective(x_line, *popt), 'r-', label='fit')

    plt.xlim(0.54, 2.12)
    plt.ylim(-1, 25)

    # plt.legend(loc = 'upper right', prop ={'size':30})
    plt.savefig(f"./images/tema2/{year}/Neutron_separation_NZ.png")


    fig, axs = plt.subplots(2, 2)

    axs[0,0].scatter(ee_data.N_Z, ee_data.S_n/1000, label='e_e')
    axs[0,0].set_xlim(0.6, 2.3)
    axs[0,0].set_ylim(0, 25)
    axs[0,1].scatter(eo_data.N_Z, eo_data.S_n/1000, label='e_o')
    axs[0,1].set_xlim(0.6, 2.3)
    axs[0,1].set_ylim(0, 25)
    axs[1,0].scatter(oe_data.N_Z, oe_data.S_n/1000, label='o_e')
    axs[1,0].set_xlim(0.6, 2.3)
    axs[1,0].set_ylim(0, 25)
    axs[1,1].scatter(oo_data.N_Z, oo_data.S_n/1000, label='o_o')
    axs[1,1].set_xlim(0.6, 2.3)
    axs[1,1].set_ylim(0, 25)

    ee_datac = ee_data
    ee_datac.dropna(inplace=True)
    eo_datac = eo_data
    eo_datac.dropna(inplace=True)
    oe_datac = oe_data
    oe_datac.dropna(inplace=True)
    oo_datac = oo_data
    oo_datac.dropna(inplace=True)

    popt, pcov = curve_fit(objective, ee_datac.N_Z, ee_datac.S_n/1000)
    x_line = np.arange(min(ee_datac.N_Z),max(ee_datac.N_Z), 0.001)
    axs[0,0].plot(x_line, objective(x_line, *popt), 'r-', label='fit')

    popt, pcov = curve_fit(objective, eo_datac.N_Z, eo_datac.S_n/1000)
    x_line = np.arange(min(eo_datac.N_Z),max(eo_datac.N_Z), 0.001)
    axs[0,1].plot(x_line, objective(x_line, *popt), 'r-', label='fit')

    popt, pcov = curve_fit(objective, oe_datac.N_Z, oe_datac.S_n/1000)
    x_line = np.arange(min(oe_datac.N_Z),max(oe_datac.N_Z), 0.001)
    axs[1,0].plot(x_line, objective(x_line, *popt), 'r-', label='fit')

    popt, pcov = curve_fit(objective, oo_datac.N_Z, oo_datac.S_n/1000)
    x_line = np.arange(min(oo_datac.N_Z),max(oo_datac.N_Z), 0.001)
    axs[1,1].plot(x_line, objective(x_line, *popt), 'r-', label='fit')


    for ax in axs.flat:
        ax.set(xlabel='N/Z', ylabel='Neutron separation energy (MeV)')

    for ax in axs.flat:
        ax.label_outer()

    # plt.legend(loc = 'upper right', prop ={'size':30})
    plt.savefig(f"./images/tema2/{year}/Neutron_NZ_4.png")


    fig, ((ax1), (ax2)) = plt.subplots(2, 1)

    ax1.scatter(data.Z, data.S_n/1000)
    ax1.set_xlim(0, 110)
    ax1.set_ylim(0, 25)

    ax2.scatter(data.N, data.S_n/1000)
    ax2.set_xlim(0, 110)
    ax2.set_ylim(0, 25)

    # for ax in axs.flat:
    #     ax.set(ylabel = "Sn (MeV)")

    ax1.set(xlabel="Z", ylabel="Sn (MeV)")
    ax2.set(xlabel="N", ylabel="Sn (MeV)")

    plt.savefig(f"./images/tema2/{year}/Sn_func_ZN.png")


    fig, ((ax3), (ax4)) = plt.subplots(2, 1)

    ax3.scatter(data.Z, data.S_p/1000)
    ax3.set_xlim(0, 110)
    ax3.set_ylim(0, 35)

    ax4.scatter(data.N, data.S_p/1000)
    ax4.set_xlim(0, 160)
    ax4.set_ylim(0, 35)


    ax3.set(xlabel="Z", ylabel="Sp (MeV)")
    ax4.set(xlabel="N", ylabel="Sp (MeV)")

    plt.savefig(f"./images/tema2/{year}/Sp_func_ZN.png")

    
    