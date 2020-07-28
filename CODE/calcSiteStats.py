import numpy as np
import scipy as sp
from scipy import stats

def main(site_stats,site,lamda,agglev,P,H,O):
    Pmu = np.mean(P)            # means
    Hmu = np.mean(H)
    Omu = np.mean(O)
    
    Psigma = np.std(P)           # stds/sigmas
    Hsigma = np.std(H)
    Osigma = np.std(O)
    
    PH_pearson = sp.stats.pearsonr(P,H)[0]     # rhos
    PO_pearson = sp.stats.pearsonr(P,O)[0]  
    HO_pearson = sp.stats.pearsonr(H,O)[0] 
    
    site_stats.append([site,agglev,lamda,Pmu,Hmu,Omu,Psigma,Hsigma,Osigma,PH_pearson,PO_pearson,HO_pearson])
    
if __name__ == '__main__':
    main(site_stats,site,lamda,agglev,P,H,O)