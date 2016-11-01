import numpy as np

'''
Input Parameter Setting

concNaClO4  # Concentration of NaClO4
preCO2  # Partial Pressure of CO2
concSO4  # Concentration of Sulfate
concF  # Concentration of Fluoride
concCl  # Concentration of Chloride
pH_gap
pH_initial
pH_terminal
NatureThlimit  # Total Amount of Thorium in System
'''

def main(input_dictionary):

    concNaClO4 = input_dictionary['concNaClO4']
    preCO2 = input_dictionary['preCO2']
    concSO4 = input_dictionary['concSO4']
    concF = input_dictionary['concF']
    concCl = input_dictionary['concCl']
    pH_gap = input_dictionary['pH_gap']
    pH_initial = input_dictionary['pH_initial']
    pH_terminal = input_dictionary['pH_terminal']
    NatureThlimit = input_dictionary['NatureThlimit']

    # Calculation of Ionic Strength

    concNa = concNaClO4
    concClO4 = concNaClO4
    I = concNaClO4
    D = 0.509*I**(1/2)/(1+1.5*I**(1/2))  # Debye-Hueckel Term

    # Data of thorium species

    num = 11  # Number of thorium hydroxide species
    numc = 5  # Number of thorium carbonate species
    nums = 4  # Number of thorium sulfate species
    numf = 4  # Number of thorium fluoride species
    numcl = 1  # Number of thorium chloride species
    num = num + numc + nums + numf + numcl

    Th  = np.array([    1,    1,    1,     1,     1,     2,     2,     4,     4,     6,     6,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,     1,      1,     1,     0,     0,     0,     0,     0,     0])
    H   = np.array([    0,    0,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,      0,     0,     1,     0,     0,     0,     0,     0])
    OH  = np.array([    0,    1,    2,     3,     4,     2,     3,     8,    12,    14,    15,     0,     1,     2,     4,     3,     0,     0,     0,     0,     0,     0,     0,      0,     0,     0,     0,     0,     0,     0,     0])
    CO3 = np.array([    0,    0,    0,     0,     0,     0,     0,     0,     0,     0,     0,     5,     4,     2,     1,     1,     0,     0,     0,     0,     0,     0,     0,      0,     0,     0,     1,     0,     0,     0,     0])
    F   = np.array([    0,    0,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     1,     2,     3,     4,     0,     0,     0,      0,     0,     0,     0,     1,     0,     0,     0])
    Cl  = np.array([    0,    0,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     1,     0,     0,      0,     0,     0,     0,     0,     0,     0,     1])
    SO4 = np.array([    0,    0,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     1,     2,      3,     4,     0,     0,     0,     1,     0,     0])
    Na  = np.array([    0,    0,    0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,     0,      0,     0,     0,     0,     0,     0,     1,     0])
    K   = np.array([    0, -2.5, -6.2,   -11, -17.4,  -5.9,  -6.8, -20.4, -26.6, -36.8, -36.8,    31,  21.6,   8.8, -15.6, -2.78,  8.87, 15.63, 20.67, 25.58,   1.7,  6.17,  9.69,  10.75,  8.44,     0,     0,     0,     0,     0,     0])
    eps = np.array([  0.7, 0.48, 0.33,  0.15,     0,  1.22,  0.91,  1.69,  0.56,   2.2,  1.85,   0.3, -0.22,  -0.1,  -0.1, -0.05,  0.48,   0.3,   0.1,     0,  0.62,   0.3,     0, -0.091, -0.18,  0.14, -0.08,  0.02, -0.12,  0.01,  0.03])

    #  Ionic Strength Correction of Formation Constants

    SIT_K = np.zeros(num)
    for i in range(num):
        SIT_K[i] = K[i] + ((4*Th[i] - OH[i] - 2*CO3[i] - F[i] - Cl[i] - 2*SO4[i])**2 + OH[i] - (16*Th[i] + F[i] + Cl[i] + 4*SO4[i] + 4*CO3[i]))*D - (eps[i] + eps[25]*OH[i] - Th[i]*eps[0] - CO3[i]*eps[26] - F[i]*eps[27] - Cl[i]*eps[30] - SO4[i]*eps[28])*I

    # Data of Solubility Limiting Phases

    SLP_num = 4  # Number of Solubility Limiting Phases

    SLP_Th  = np.array([     1,      1,     1,     1])
    SLP_H   = np.array([     0,      0,     0,     4])
    SLP_F   = np.array([     4,      0,     0,     0])
    SLP_SO4 = np.array([     0,      2,     0,     0])
    SLP_Na  = np.array([     0,      0,     6,     0])
    SLP_CO3 = np.array([     0,      0,     5,     0])
    SLP_K   = np.array([-31.68, -11.25, -42.2,   8.9])

    #  Ionic Strength Correction of Solubility Limiting Phases

    SIT_SLP_K = np.zeros(SLP_num)
    for i in range(SLP_num):
        SIT_SLP_K[i] = SLP_K[i] + (16*SLP_Th[i] + SLP_F[i] + 4*SLP_SO4[i] + SLP_Na[i] + 4*SLP_CO3[i] - SLP_H[i])*D - (SLP_Th[i]*eps[0] + SLP_F[i]*eps[27] + SLP_SO4[i]*eps[28] + SLP_Na[i]*eps[29] + SLP_CO3[i]*eps[26] - SLP_H[i]*eps[25])*I;

    #  Calculation Results Save

    M1 = np.zeros((int((pH_terminal - pH_initial)/pH_gap)+1, num + 1))
    M2 = np.zeros((int((pH_terminal - pH_initial)/pH_gap)+1, num + 1))

    #  Calculation

    pH = pH_initial
    index = 0

    while index <= int((pH_terminal - pH_initial)/pH_gap):
        concTh = float('inf')
        Th_total = 0
        H = 10**(-pH)
        concCO3 = 10**(-18.14)*preCO2/H**2
        concH = H

        for i in range(SLP_num):
            tempSLP = (10**SIT_SLP_K[i]*concH**SLP_H[i]/(concF**SLP_F[i]*concNa**SLP_Na[i]*concCO3**SLP_CO3[i]*concSO4**SLP_SO4[i]))**(1/SLP_Th[i])
            if tempSLP != 0:
                if concTh > tempSLP:
                    concTh = tempSLP

        for i in range(num):
            Th_total += (concTh**Th[i]*concSO4**SO4[i]*concF**F[i]*concCl**Cl[i]*concCO3**CO3[i]*10**SIT_K[i])/H**OH[i]

        if Th_total > NatureThlimit:
            k = NatureThlimit
            while True:
                Th_total = 0
                for i in range(num):
                    Th_total += (k**Th[i]*concSO4**SO4[i]*concF**F[i]*concCl**Cl[i]*concCO3**CO3[i]*10**SIT_K[i])/H**OH[i]
                if (Th_total/NatureThlimit < 1.001) and (Th_total/NatureThlimit > 0.999):
                    concTh = k
                    break
                elif Th_total/NatureThlimit >= 1.001:
                    k /= 2
                else:
                    k *= 1.5

        M1[index][0] = np.log10(Th_total)
        M2[index][0] = np.log10(Th_total)

        for i in range(num):
            M1[index][i + 1] = np.log10((concTh**Th[i]*concSO4**SO4[i]*concF**F[i]*concCl**Cl[i]*concCO3**CO3[i]*10**SIT_K[i])/H**OH[i])
            M2[index][i + 1] = ((concTh**Th[i]*concSO4**SO4[i]*concF**F[i]*concCl**Cl[i]*concCO3**CO3[i]*10**SIT_K[i])/H**OH[i])/Th_total
        pH += pH_gap
        index += 1
    return (M1, M2)
