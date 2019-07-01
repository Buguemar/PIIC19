"""
 Link generated by : https://www.cfa.harvard.edu/~avanderb/k2.html
"""
import pandas as pd
import numpy as np

df_planet = pd.read_csv("../../K2_Data/k2_planets_search.txt")
df_planet.drop(0,axis=0, inplace=True)
df_planet.drop([1,2], axis=0, inplace=True)

lines = []
for i,value in df_planet.iterrows():
    id_v = value["K2 ID"]
    c_number = "c"+ value["K2 Campaign"].zfill(2)
    if c_number[1:] == "10":
        c_number += "2"
    if c_number[1:] == "11": #está dividida en 2...
        c_number += "2" # hay solo 1 dato
    url = "http://archive.stsci.edu/missions/hlsp/k2sff/"
    url += c_number+ "/"
    url += id_v[:4]+ "00000" + "/"
    url += id_v[4:] + "/"
    url += "hlsp_k2sff_k2_lightcurve_"+id_v+"-"+c_number+"_kepler_v1_llc-default-aper.txt"
    lines.append(url)

time = []
lc_norm = []
for line in lines:
    print("Leyendo un archivo de url: ",line)
    aux = pd.read_csv(line,index_col=False)
    time.append(aux['BJD - 2454833'].values)
    lc_norm.append(aux[" Corrected Flux"].values)
time = np.asarray(time)
lc_norm = np.asarray(lc_norm)

np.save("/work/work_teamEXOPLANET/K2_mission/K2_PLANET_time.npy",time)
np.save("/work/work_teamEXOPLANET/K2_mission/K2_PLANET_lc_detr.npy",lc_norm)
