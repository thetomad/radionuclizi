import pandas as p
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def tema1(year):
    
    # Reading data
    data = p.read_csv(f'./databases/{year}/AUDI{year}.csv')
    

    # Adding 2 columns for W(A, Z) and B(A, Z)
    d = np.array(data['D'])
    z = np.array(data['Z'])
    a = np.array(data['A'])
    w = z * data.iat[1,3] + ( a-z ) * data.iat[0,3] - d
    data['W'] = w
    b = ( w / a ) / 1000
    data['B'] = b
    data.to_csv(f'./databases/{year}/AUDI{year}.csv')
    
    # Plotting the first graph for an overview
    plt.figure(figsize=(20, 10))
    plt.xlabel('A',fontsize=20)
    plt.ylabel('B(Z,A) (MeV)',fontsize=20)

    ax = plt.subplot(111)

    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))

    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))

    ax.xaxis.grid(True,'minor',linestyle='-.')
    ax.yaxis.grid(True,'minor',linestyle='-.')
    ax.xaxis.grid(True,'major',linewidth=1.5,linestyle='-.')
    ax.yaxis.grid(True,'major',linewidth=1.5,linestyle='-.')

    plt.scatter(a,b, c='red')
    plt.xlim(0,270)
    plt.ylim(0,10)

    plt.savefig(f'./images/tema1/{year}/B_A_general.png')

    # Creating data for pairs odd-odd
    data.loc[(data['Z']%2 != 0) & (data['A']%2 != 0)].to_csv(f'./databases/{year}/odd-odd.csv')
    odd_data = p.read_csv(f'./databases/{year}/odd-odd.csv', index_col=[0])
    dist_odd = np.array(odd_data['D'])
    Z_odd = np.array(odd_data['Z'])
    A_odd = np.array(odd_data['A'])
    W_odd = Z_odd * 7288.9692 + ( A_odd - Z_odd ) * 8071.3232 - dist_odd
    B_odd = ( W_odd / A_odd ) / 1000
    odd_data['B'] = B_odd
    odd_data.to_csv(f'./databases/{year}/odd.csv')

    # Creating data for pairs odd-A
    data.loc[(data['Z']%2 == 0) & (data['A']%2 != 0)].to_csv(f'./databases/{year}/even-odd.csv')
    odd_A_data = p.read_csv(f'./databases/{year}/even-odd.csv', index_col=[0])
    dist_odd_A = np.array(odd_A_data['D'])
    Z_odd_A = np.array(odd_A_data['Z'])
    A_odd_A = np.array(odd_A_data['A'])
    W_odd_A = Z_odd_A * 7288.9692 + ( A_odd_A - Z_odd_A ) * 8071.3232 - dist_odd_A
    B_odd_A = ( W_odd_A / A_odd_A ) / 1000
    odd_A_data['B'] = B_odd_A
    odd_A_data.to_csv(f'./databases/{year}/even-odd.csv')

    # Creating data for pairs even-even
    data.loc[(data['Z']%2 == 0) & (data['A']%2 == 0)].to_csv(f'./databases/{year}/even-even.csv')
    even_data = p.read_csv(f'./databases/{year}/even-even.csv', index_col=[0])
    dist_even = np.array(even_data['D'])
    Z_even = np.array(even_data['Z'])
    A_even = np.array(even_data['A'])
    W_even = Z_even * 7288.9692 + ( A_even - Z_even ) * 8071.3232 - dist_even
    B_even = ( W_even / A_even ) / 1000
    even_data['B'] = B_even
    even_data.to_csv(f'./databases/{year}/even.csv')

    # Created overlayered structure graph
    plt.figure(figsize=(20, 10))
    plt.xlabel('A',fontsize=20)
    plt.ylabel('B(Z,A) (MeV)',fontsize=20)

    ax = plt.subplot(111)

    ax.xaxis.set_major_locator(MultipleLocator(50))
    ax.xaxis.set_minor_locator(MultipleLocator(10))

    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_minor_locator(MultipleLocator(0.2))

    ax.xaxis.grid(True,'minor',linestyle='-.')
    ax.yaxis.grid(True,'minor',linestyle='-.')
    ax.xaxis.grid(True,'major',linewidth=1.5,linestyle='-.')
    ax.yaxis.grid(True,'major',linewidth=1.5,linestyle='-.')

    plt.plot(A_odd,B_odd,'-o',markersize=10,label='odd-odd', c='#dfe615')
    plt.plot(A_odd_A,B_odd_A,'-v',markersize=10,label='even-odd', c='#eb0909')
    plt.plot(A_even,B_even,'-d',markersize=10,label='even-even', c='#1611b8')
    plt.legend(loc='lower right', prop={"size":20})
    plt.xlim(0,270)
    plt.ylim(0,10)

    plt.savefig(f'./images/tema1/{year}/overlayered_struct.png')


    # Create layered structure graph
    fig = plt.figure()
    fig.set_figheight(15)
    fig.set_figwidth(15)
    gs = fig.add_gridspec(3, hspace=0)
    axs = gs.subplots(sharex=True, sharey=True,)

    axs[0].scatter(A_odd,B_odd,label='odd-odd', c='#dfe615')
    axs[1].scatter(A_odd_A,B_odd_A,marker='v',label='even-odd', c='#eb0909')
    axs[2].scatter(A_even,B_even,marker='d',label='even-even', c='#1611b8')
    plt.xlabel('A',fontsize=20)
    fig.text(0.06, 0.5, 'B(Z,A) (MeV)', va='center', rotation='vertical',fontsize=20 )
    axs[0].legend(loc="lower right", prop={"size":15})
    axs[1].legend(loc="lower right", prop={"size":15})
    axs[2].legend(loc="lower right", prop={"size":15})

    for ax in axs:
        ax.label_outer()
        
    plt.savefig(f'./images/tema1/{year}/layered_struct.png')

    # Separating data for light-heavy nuclei
    new_odd = p.read_csv(f'./databases/{year}/odd.csv')
    new_A = p.read_csv(f'./databases/{year}/even-odd.csv')
    
    new_even = p.read_csv(f'./databases/{year}/even.csv')

    new_odd.loc[new_odd.A <= 80].to_csv(f'./databases/{year}/light_odd.csv')
    new_odd.loc[new_odd.A >= 80].to_csv(f'./databases/{year}/heavy_odd.csv')
    new_A.loc[new_A.A <= 80].to_csv(f'./databases/{year}/light_eo.csv')
    new_A.loc[new_A.A >= 80].to_csv(f'./databases/{year}/heavy_eo.csv')
    new_even.loc[new_even.A <= 80].to_csv(f'./databases/{year}/light_even.csv')
    new_even.loc[new_even.A >= 80].to_csv(f'./databases/{year}/heavy_even.csv')

    light_odd = p.read_csv(f'./databases/{year}/light_odd.csv')
    heavy_odd = p.read_csv(f'./databases/{year}/heavy_odd.csv')
    light_A = p.read_csv(f'./databases/{year}/light_eo.csv')
    heavy_A = p.read_csv(f'./databases/{year}/heavy_eo.csv')
    light_even = p.read_csv(f'./databases/{year}/light_even.csv')
    heavy_even = p.read_csv(f'./databases/{year}/heavy_even.csv')

    # Plotting the light and heavy nuclei
    plt.figure(figsize=(20, 10))
    plt.xlabel('A',fontsize=20)
    plt.ylabel('B(Z,A) (MeV)',fontsize=20)

    plt.scatter(light_odd.A,light_odd.B,s=70,label='light odd-odd', c='#dfe615')
    plt.scatter(light_A.A,light_A.B,marker='v',s=70,label='light even-odd', c='#eb0909')
    plt.scatter(light_even.A,light_even.B,marker='d',s=70,label='light even-even', c='#1611b8')
    plt.legend(loc='lower right', prop={"size":20})
    plt.xlim(0,80)
    plt.ylim(0,9)

    plt.savefig(f'./images/tema1/{year}/nuc_usoare.png')


    plt.figure(figsize=(20, 10))
    plt.xlabel('A',fontsize=20)
    plt.ylabel('B(Z,A) (MeV)',fontsize=20)

    plt.scatter(heavy_odd.A,heavy_odd.B,s=70,label='heavy odd-odd', c='#dfe615')
    plt.scatter(heavy_A.A,heavy_A.B,marker='v',s=70,label='heavy even-odd', c='#eb0909')
    plt.scatter(heavy_even.A,heavy_even.B,marker='d',s=70,label='heavy even-even',c='#1611b8')
    plt.legend(loc='upper right', prop={"size":20})
    plt.xlim(80,270)
    
    plt.ylim(7,9)

    plt.savefig(f'./images/tema1/{year}/nuc_grele.png')
