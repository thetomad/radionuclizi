import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def tema3(year):

    
    data =pd.read_csv(f"./databases/{year}/AUDI{year}.csv")

    d_vld_n = []

    for i in range(0,len(data.D)):
        
        current_row = data.iloc[i]
        
        x = data.loc[(data['Z'] == current_row.Z) & (data['A'] == (current_row.A-1))].S_n
        y = data.loc[(data['Z'] == current_row.Z) & (data['A'] == (current_row.A))].S_n
        
        if x.empty:
            
            d_vld_n.append(np.nan)
            
        else:
            
            z = y.iat[0] - x.iat[0]
            
            if z>0 :
            
                d_vld_n.append(abs(z))
            
            else:
                
                d_vld_n.append(np.nan) 

    d_vld_p = []

    for i in range(0,len(data.D)):
        
        current_row = data.iloc[i]
        
        x = data.loc[(data['Z'] == (current_row.Z-1)) & (data['A'] == (current_row.A-1))].S_p
        y = data.loc[(data['Z'] == current_row.Z) & (data['A'] == (current_row.A))].S_p
        if x.empty:
            
            d_vld_p.append(np.nan)
            
        else:
            
            z = y.iat[0] - x.iat[0]
            
            if z>0:
            
                d_vld_p.append(abs(z))
            
            else:
                
                d_vld_p.append(np.nan)

    d_gut_n = []

    for i in range(0,len(data.D)):
        
        current_row = data.iloc[i]
        
        x = data.loc[(data['Z'] == current_row.Z) & (data['A'] == (current_row.A-1))].S_n
        y = data.loc[(data['Z'] == current_row.Z) & (data['A'] == current_row.A)].S_n
        w = data.loc[(data['Z'] == current_row.Z) & (data['A'] == (current_row.A+1))].S_n
        
        if x.empty or w.empty:
            
            d_gut_n.append(np.nan)
            
        else:
            
            z = (1/4) * ( w.iat[0] - 2*y.iat[0] + x.iat[0])
            
            if z>0:
            
                d_gut_n.append(abs(z))
            
            else:
                
                d_gut_n.append(np.nan)

    d_gut_p = []

    for i in range(0,len(data.D)):
        
        current_row = data.iloc[i]
        
        x = data.loc[(data['Z'] == (current_row.Z-1)) & (data['A'] == (current_row.A-1))].S_p
        y = data.loc[(data['Z'] == current_row.Z) & (data['A'] == current_row.A)].S_p
        w = data.loc[(data['Z'] == (current_row.Z+1)) & (data['A'] == (current_row.A+1))].S_p
        
        if x.empty or w.empty:
            
            d_gut_p.append(np.nan)
            
        else:
            
            z = (1/4) * ( w.iat[0] - 2*y.iat[0] + x.iat[0])
            
            if z>0:
                
                d_gut_p.append(abs(z))
            
            else:
                
                d_gut_p.append(np.nan)

    data['Delta_n_VLD'] = d_vld_n
    data['Delta_p_VLD'] = d_vld_p
    data['Delta_n_GUT'] = d_gut_n
    data['Delta_p_GUT'] = d_gut_p


    plt.figure(figsize=(20, 15))
    plt.xlabel('A',fontsize=20)
    plt.ylabel('Pairing energy (MeV)',fontsize=20)

    plt.scatter(data.A, (data.Delta_n_VLD + data.Delta_p_VLD)/1000, s=200, color='white', edgecolors='red', label='even-even')
    plt.scatter(data.A, data.Delta_p_VLD/1000, s=200, marker='s', color='white', edgecolors='blue', label='even-odd')
    plt.scatter(data.A, data.Delta_n_VLD/1000, s=200, marker='d', color='white', edgecolors='yellowgreen', label='odd-even')

    plt.plot(data.A, 12/(np.sqrt(data.A)), color='black', linewidth='2',label = r'2 * 12/A$^{1/2}$')
    plt.plot(data.A, 24/(np.sqrt(data.A)), color='brown', linewidth='2.5',label = r'12/A$^{1/2}$')

    plt.legend(loc='upper right', prop={"size":20})
    plt.xlim(0,275)
    plt.ylim(0,10)

    

    plt.text(100, 8, "Vladuca \n" + r"$\Delta_n (A,Z) = S_n (A,Z) -S_n (A-1,Z)$" + "\n" +  r"$\Delta_p (A,Z) = S_p (A,Z) -S_p (A-1,Z-1)$", fontsize = 20)
    plt.savefig(f'./images/tema3/{year}/Pairing_VLD.png')


    plt.figure(figsize=(20, 15))
    plt.xlabel('A',fontsize=20)
    plt.ylabel('Pairing energy (MeV)',fontsize=20)

    plt.scatter(data.A, (data.Delta_n_GUT + data.Delta_p_GUT)/1000, s=200, color='white', edgecolors='red', label='even-even')
    plt.scatter(data.A, data.Delta_p_GUT/1000, marker='s', s=200, color='white', edgecolors='blue', label='even-odd')
    plt.scatter(data.A, data.Delta_n_GUT/1000, marker='d', s=200, color='white', edgecolors='yellowgreen', label='odd-even')

    plt.plot(data.A, 12/(np.sqrt(data.A)), color='black', linewidth='2', label = r'2 * 12/A$^{1/2}$')
    plt.plot(data.A, 24/(np.sqrt(data.A)), color='brown', linewidth='2.5', label = r'12/A$^{1/2}$')

    plt.legend(loc='upper right', prop={"size":20})
    plt.xlim(0,275)
    plt.ylim(0,10)

    plt.text(50, 8, "Guttormsen \n" + r"$\Delta_n (A,Z) = [S_n (A+1,Z) - 2S_n (A,Z) + S_n (A-1,Z)]/4$" + "\n" + r"$\Delta_p (A,Z) = [S_p (A+1,Z+1) - 2S_p (A,Z) + S_p (A-1,Z-1)]/4$", fontsize = 20)
    plt.savefig(f'./images/tema3/{year}/Pairing_GUT.png')
