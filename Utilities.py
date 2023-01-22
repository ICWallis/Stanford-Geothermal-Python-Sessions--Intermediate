import matplotlib.pyplot as plt

# 
# Use frictional faulting theory to constrain limits of the stress polygon
# 

# Extension limit of the stress polygon
# S_hmin = S_Hmax << S_v

def minstress(S1,Pp,mu):
    '''Use the stress ratio and frictional faulting theroy to constrain minimum stress
    
    My calculations assume MPa, but other pressure units (Pa, psi) could be used
    
        Args:       Pp pore pressure 
                    S1 maximum stress
        
        Returns:    S3 minimum stress
    '''
    S3 = ((S1-Pp)/(((mu**2 + 1.)**0.5 + mu)**2))+Pp
    return S3


# Compression limit of the stress polygon
# S_hmin = S_Hmax >> S_v

def maxstress(S3,Pp,mu):
    '''Use the stress ratio and frictional faulting theory to constrain the maximum stress
    
        My calculations assume MPa, but other pressure units (Pa, psi) could be used
    
        Args:       Pp pore pressure 
                    S3 minimum stress
        
        Returns:    S1 maximum stress
    '''
    S1 = ((S3-Pp)*(((mu**2 + 1.)**0.5 + mu)**2))+Pp
    return S1

#
# Generate stress polygon
#

def stress_polygon(Sv, Pp, mu):
    '''
    Draws stress polygon (Zoback-a-gram)


        Args:
            Sv (float) vertical stress in MPa
            Pp (float) pore pressure in MPa
            mu (float) Coefficient of friction

        Returns: 
            matplotlib.pyplot plt object

    '''
    # define stress limits
    minSh = minstress(Sv,Pp,mu)
    maxSh = maxstress(Sv,Pp,mu)
    minSH = minSh 
    maxSH = maxSh

    fig, ax = plt.subplots(1,1,figsize=(6,6))

    # Vertical stress
    ax.plot(Sv,Sv,'o',color='k')         # 2. Central point $ S_hmin = S_Hmax = S_v $

    # Connecting lines
    ax.plot([minSh,minSh],[minSh,Sv],color='k',alpha=0.5) 
    ax.plot([minSh,Sv],[Sv,maxSH],color='k',alpha=0.5)
    ax.plot([Sv,maxSh],[maxSH,maxSH],color='k',alpha=0.5)
    ax.plot([minSh,Sv],[Sv,Sv],color='k',linestyle=':',alpha=0.5)
    ax.plot([Sv,Sv],[Sv,maxSH],color='k',linestyle=':',alpha=0.5)
    ax.plot([minSh,maxSH],[minSh,maxSH],color='k',alpha=0.5)

    # Labels
    ax.text((maxSH-Sv)/4+Sv,(maxSH-Sv)/1.5+Sv, 'RF', fontsize=10)
    ax.text((Sv-minSh)/2+minSh,(maxSH-Sv)/8+Sv, 'SS', fontsize=10)
    ax.text((Sv-minSh)/4+minSh,(Sv-minSh)/1.5+minSh, 'NF', fontsize=10)

    # Format plot

    ax.set_xlim(minSh-20, maxSh+20)
    ax.set_ylim(minSh-20, maxSh+20)

    ax.set_xlabel('$S_{hmin}$ [MPa]')
    ax.set_ylabel('$S_{Hmin}$ [MPa]')

    return plt