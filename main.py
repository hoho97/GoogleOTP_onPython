# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:32:36 2018

@author: Kaho
"""

import OTP
secret = input("Please enter the secret from your QR code\n")
print(OTP.OTP(secret))
input('Press ENTER to exit')