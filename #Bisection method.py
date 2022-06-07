#Bisection method

#input endboints a, b, tolerance tol, iterations n0
#output approx sol p, iterations i, or no solution and n0

def fof(x):                         #the function
    return ((x * x) - 3)

a = 0                               #interval start
b = 4                               #interval end

TOL = .000001                       #5 zeroes for 5 digits (by intuition and check)
N0 = 100                            #maximum iterations

i = 1               
FA = fof(a)                         #evaluate function at interval start

while (i <= N0):
    p = a + (b-a)/2                 #evaluate midpoint of interval
    FP = fof(p)                     #evaluate function at midpoint
    if ((FP == 0) or (((b-a)/2) < TOL)) :     #if this point is zero or the interval is smaller than the search tolerance
        print("The solution is", p, "after", i, "iterations.\n")  #print solution
        quit()
    else :
        i = i + 1                   #no solution reached, iterate
    if ((FA * FP) > 0) :            #if there was no change in sign of the function between ai and pi, no zero exists
        a = p                       #so search the other half next
        FA = FP                     #update function value at new interval start
    else :
        b = p                       #else there must be a zero, search this half (ai and pi)

print("There is no solution after", N0, "iterations.\n")
quit()