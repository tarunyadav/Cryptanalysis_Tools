# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:32:15 2021

@author: tarunyadav
"""
import numpy as np
import math
import sys

def print_DDT(table):
    for row in range(len(table)):
        for col in range(len(table[row])):
            print(table[row][col],end='');
            if col == len(table[row])-1:
                print("\n");

if (sys.argv[1] == "PRESENT"):
  s_box = ((0xC , 0x5 , 0x6 , 0xB , 0x9 , 0x0 , 0xA , 0xD , 0x3 , 0xE , 0xF , 0x8 , 0x4 , 0x7 , 0x1, 0x2),);     # PRESENT
if (sys.argv[1] == "WARP"):
  s_box = ((0xc,0xa, 0xd,0x3, 0xe,0xb, 0xf, 0x7, 0x8, 0x9, 0x1, 0x5, 0x0, 0x2, 0x4, 0x6),);     # WARP
elif (sys.argv[1] == "GIFT"):
  s_box = ((0x1,0xa, 0x4,0xc, 0x6,0xf, 0x3, 0x9, 0x2, 0xd, 0xb, 0x7, 0x5, 0x0, 0x8, 0xe),);       # GIFT       
elif (sys.argv[1] == "TWINE"):
  s_box = ((0xc,0x0, 0xf,0xa, 0x2,0xb, 0x9, 0x5, 0x8, 0x3, 0xd, 0x7, 0x1, 0xe, 0x6, 0x4),);       # TWINE         
elif (sys.argv[1] == "ASCON"):
  s_box = ((0x4,0xb,0x1f,0x14,0x1a,0x15,0x9,0x2,0x1b,0x5,0x8,0x12,0x1d,0x3,0x6,0x1c,), (0x1e,0x13,0x7,0xe,0x0,0xd,0x11,0x18,0x10,0xc,0x1,0x19,0x16,0xa,0xf,0x17));       # ASCON  
elif (sys.argv[1] == "FIDES-6"):
  s_box = ( (54,0,48,13,15,18,35,53,63,25,45,52,3,20,33,41),(8,10,57,37,59,36,34,2,26,50,58,24,60,19,14,42),(46,61,5,49,31,11,28,4,12,30,55,22,9,6,32,23),(27,39,21,17,16,29,62,1,40,47,51,56,7,43,38,44));#FIDES-6
elif (sys.argv[1] == "FIDES-5"):
  s_box = ((1,0,25,26,17,29,21,27,20,5,4,23,14,18,2,28),(15,8,6,3,13,7,24,16,30,9,31,10,22,12,11,19)); #FIDES-5
elif (sys.argv[1] == "SC2000-5"):
  s_box = ((20,26,7,31,19,12,10,15,22,30,13,14, 4,24, 9,18),(27,11, 1,21, 6,16, 2,28,23, 5, 8, 3, 0,17,29,25));
elif (sys.argv[1] == "SC2000-6"):
  s_box = ((47,59,25,42,15,23,28,39,26,38,36,19,60,24,29,56),(37,63,20,61,55, 2,30,44, 9,10, 6,22,53,48,51,11),(62,52,35,18,14,46, 0,54,17,40,27, 4,31, 8, 5,12),(3,16,41,34,33, 7,45,49,50,58, 1,21,43,57,32,13));
elif (sys.argv[1] == "APN-6"):
  s_box = ((0,54,48,13,15,18,53,35,25,63,45,52,3,20,41,33),(59,36,2,34,10,8,57,37,60,19,42,14,50,26,58,24),(39,27,21,17,16,29,1,62,47,40,51,56,7,43,44,38),(31,11,4,28,61,46,5,49,9,6,23,32,30,12,55,22));

DDT_SIZE = (len(s_box)*len(s_box[0]))
input_size = int(math.log(DDT_SIZE,2))
DDT = np.zeros( (DDT_SIZE,DDT_SIZE) )
DDT = DDT.astype(int)
sbox_val = []


for p2 in range(DDT_SIZE):
    row = p2 >> 4
    col = p2 & 15
    sbox_val.append(s_box[row][col]);

for p1 in range(DDT_SIZE):
	for p2 in range(DDT_SIZE):
		XOR_IN = np.bitwise_xor(p1,p2);
		XOR_OUT = np.bitwise_xor(sbox_val[p1],sbox_val[p2]);
		DDT[XOR_IN][XOR_OUT] += 1




#sys.exit()
# DDT_values=np.unique(DDT)[1:]
# for value in DDT_values:
#     indices = np.where(DDT==value)
#     f = open("DDT_"+str(value)+".txt","w")
#     f.write("x0\tx1\tx2\tx3\tx4\tx5\tx6\tx7\ty0\ty1\ty2\ty3\ty4\ty5\ty6\ty7\t\tF\n")
#     for i in range(0,len(indices[0])):
#         x_bin = bin(indices[0][i])[2:].zfill(8)
#         y_bin = bin(indices[1][i])[2:].zfill(8)
#         f.write(x_bin[0]+"\t"+x_bin[1]+"\t"+x_bin[2]+"\t"+x_bin[3]+"\t"+x_bin[4]+"\t"+x_bin[5]+"\t"+x_bin[6]+"\t"+x_bin[7]+"\t"+y_bin[0]+"\t"+y_bin[1]+"\t"+y_bin[2]+"\t"+y_bin[3]+"\t"+y_bin[4]+"\t"+y_bin[5]+"\t"+y_bin[6]+"\t"+y_bin[7]+"\t\t"+ "1\n")
#     f.close()
########DDT S-Box inequalities#########
indices = np.where(DDT!=0)
#indices = np.where(DDT==16)
f = open("DDT_TruthTable.txt","w")
#f.write(".i 16\n")
#f.write(".o 1\n")
#for i in range(0,len(indices[0])):
#    x_bin = bin(indices[0][i])[2:].zfill(8)
#    y_bin = bin(indices[1][i])[2:].zfill(8)
#    f.write(x_bin[0]+x_bin[1]+x_bin[2]+x_bin[3]+x_bin[4]+x_bin[5]+x_bin[6]+x_bin[7]+y_bin[0]+y_bin[1]+y_bin[2]+y_bin[3]+y_bin[4]+y_bin[5]+y_bin[6]+y_bin[7]+"|1\n")
#f.close()

if (input_size == 4):
    f.write("x3\tx2\tx1\tx0\ty3\ty2\ty1\ty0\t\tF\n")
    for i in range(0,len(indices[0])):
        x_bin = bin(indices[0][i])[2:].zfill(4)
        y_bin = bin(indices[1][i])[2:].zfill(4)
        
        f.write(x_bin[0]+"\t"+x_bin[1]+"\t"+x_bin[2]+"\t"+x_bin[3]+"\t"+y_bin[0]+"\t"+y_bin[1]+"\t"+y_bin[2]+"\t"+y_bin[3]+"\t"+"\t\t"+ "1\n")
    f.close()
        
#elif (input_size == 5):
    
#elif (input_size == 6):   
    
    


########DDT S-Box+Probabity inequalities#########
# indices = np.where(DDT!=0)
# f = open("DDT_all_prob.txt","w")
# f.write("x0\tx1\tx2\tx3\tx4\tx5\tx6\tx7\ty0\ty1\ty2\ty3\ty4\ty5\ty6\ty7\tz0\tz1\tz2\tz3\tz4\tz5\tz6\t\tF\n")
# for i in range(0,len(indices[0])):
#     x_bin = bin(indices[0][i])[2:].zfill(8)
#     y_bin = bin(indices[1][i])[2:].zfill(8)
#     z = DDT[indices[0][i]][indices[1][i]]
#     if (z==2):
#         z_bin = "0000001"
#     elif (z==4):
#          z_bin = "0000010"
#     elif (z==6):
#          z_bin = "0000100"
#     elif (z==8):
#          z_bin = "0001000"
#     elif (z==10):
#          z_bin = "0010000"
#     elif (z==12):
#          z_bin = "0100000"
#     elif (z==16):
#          z_bin = "1000000"
#     elif (z==256):
#          z_bin = "0000000"
#     f.write(x_bin[0]+"\t"+x_bin[1]+"\t"+x_bin[2]+"\t"+x_bin[3]+"\t"+x_bin[4]+"\t"+x_bin[5]+"\t"+x_bin[6]+"\t"+x_bin[7]+"\t"+y_bin[0]+"\t"+y_bin[1]+"\t"+y_bin[2]+"\t"+y_bin[3]+"\t"+y_bin[4]+"\t"+y_bin[5]+"\t"+y_bin[6]+"\t"+y_bin[7]+"\t"+z_bin[0]+"\t"+z_bin[1]+"\t"+z_bin[2]+"\t"+z_bin[3]+"\t"+z_bin[4]+"\t"+z_bin[5]+"\t"+z_bin[6]+"\t\t"+ "1\n")
# f.close()


