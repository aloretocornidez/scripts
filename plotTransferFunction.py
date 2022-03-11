# Name: Alan Manuel
# File: plotTransferFunction.py
# Purpose: A script to plot a transfer function's bode magnitude and phase plots. Uses the scipy and matplot libraries.

import argparse
import sys
from numpy import double
from scipy import signal
import matplotlib.pyplot as plt



def plotTransferFunction(numerator, denominator):


    s1 = signal.lti(numerator, denominator)
    w, mag, phase = s1.bode()

    plt.figure()
    plt.semilogx(w, mag)    # Bode magnitude plot
    plt.title("Bode Magnitude Plot")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Gain [dB]")


    plt.figure()
    plt.semilogx(w, phase)  # Bode phase plot
    plt.title("Bode Phase Plot")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Phase [degrees")

    plt.show()
    return



##Parses the arguments in script call.
def getArgs():
    
    parser = argparse.ArgumentParser(description='Generate Bode Plots of a Transfer Function')
    
    required = parser.add_argument_group("Required Aruments")

    required.add_argument('-n', '--numerator', nargs = "+", default = ['a', 'b'], required=True, help = 'Coefficients of the numerator of the transfer function. [A_n, A_n-1, ..., A_1, A_0]')
    required.add_argument('-d', '--denominator', nargs = "+", default = ["a", "b"], required=True, help = 'Coefficients of the denominator of the transfer function. [A_n, A_n-1, ..., A_1, A_0]')
    

    if len(sys.argv)== 1:
        # parser.print_usage()
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()
    


def main():
    #print("In main")
    args = getArgs()
    
    numerator = args.numerator
    print(f'Numerator before mapping:\n{numerator}')
    
    numerator = list(map(double, numerator))
    print(f'Numerator after mapping: \n{numerator}')

    
    denominator = args.denominator
    print(f'Denominator before mapping:\n{denominator}')
    
    denominator = list( map(double, denominator))
    print(f'Denominator after mapping:\n{denominator}')

    print('Calling plotTransferFunction()')
    plotTransferFunction(numerator, denominator)


    
if __name__ == '__main__':
    main()
