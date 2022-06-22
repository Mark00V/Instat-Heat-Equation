import numpy as np
import copy

def intnodes(intmethod):
    intnodes_gauss = np.array([0.1127016653792583, 0.5, 0.8872983346207417],dtype=np.double) # Gauss
    intweights_gauss = np.array([0.2777777777777778, 0.4444444444444444, 0.2777777777777778],dtype=np.double) # Gauss

    intnodes_lob = np.array([0.0, 0.5, 1.0],dtype=np.double) # Lobatto
    intweights_lob = np.array([0.1666666666666667, 0.6666666666666667, 0.1666666666666667],dtype=np.double) # Lobatto

    
    if intmethod == "gauss":
        return intnodes_gauss,intweights_gauss
    elif intmethod == "lob":
        return intnodes_lob,intweights_lob

def philequdist(knoten,xi):
    knoten = int(knoten)
    if knoten==1:
        f = -2*(1-xi)*(-(1/2)+xi)
    elif knoten==2:
        f = -4*(-1+xi)*xi
    elif knoten==3:
        f = 2*(-(1/2)+xi)*xi
    return f

def philequdistgrad(knoten,xi):
    knoten = int(knoten)
    if knoten==1:
        f = -2*(1-xi)+2*(-(1/2)+xi)
    elif knoten==2:
        f = -4*(-1+xi)-4*xi
    elif knoten==3:
        f = 2*(-(1/2)+xi)+2*xi
    return f

def main():
    print("Intnodes gauss:",intnodes("gauss"))
    print("Intnodes lob:",intnodes("lob"))

if __name__ == '__main__':
    main()