# HW9_Task1_weston_rullman
# File: Task1_weston_rullman.py
# Date: 04 03 2023
# By: Weston Rullman
# ID: 234660
# Team: 6
#
# ELECTRONIC SIGNATURE
# Weston Rullman
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# The purpose of this script is to calculate the intrinsic impedence using the amplitude of the incident wave, the permittivity, and the permeability of mediums 1 and 2.

# input the inputs
E = float(input('Amplitude of the Incident Wave (V/m): '))
e1 = float(input('Permittivity of Medium 1: '))
e2 = float(input('Permittivity of Medium 2: '))
mu1 = float(input('Permiability of Medium 1: '))
mu2 = float(input('Permiability of Medium 2: '))

# This calculates the intrinsic impedence of mediums 1(n1) and 2(n2)
n1 = 377.14 * (mu1/e1)**.5
n2 = 377.14 * (mu2/e2)**.5
# Do the Math
# This calculates the amplitude of the reflected wave(E1) and the transmitted wave(E2)
Et = ((2 * n2)/(n2 + n1)) * E
Er = ((n2 - n1)/(n2 + n1)) * E

#Display Outputs
print('Intrinsic Impedance 1: ' + str(n1) + ' Ohms')
print('Intrinsic Impedance 2: ' + str(n2) + ' Ohms')
print('Reflected Amplitude: ' + str((Er)) + ' V/m')
print('Transmitted Amplitude: ' + str((Et)) + ' V/m')