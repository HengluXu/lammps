#!/usr/bin/env python
# coding: utf-8

import os
import sys

def convert(temp,np):
    Ek=temp*1.5*6.0221409*1.38064852*(np)/(1000*4.184)
    print("At %.2f K, Ek of %i CH4 is    %.3f    kcal/mol"%(temp,np,Ek))
    return Ek

temp=float(sys.argv[1])
np=int(sys.argv[2])
convert(temp,np)
