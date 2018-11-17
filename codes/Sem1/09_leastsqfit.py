"""
Roll Number: xxxx 
Description: Least square fitting
@author: AKB
"""

import math, time
sx = sy = sxy = sxx = syy = a = b = s = aSE = bSE = 0.0

# Input the x & y coordinates
x = list(); y = list(); # Create empty list to populate
n = int(input("Enter the number of points :"))
print 'Enter numbers in array: '
for i in range(int(n)):
    xi = float(input("x"+str(i)+" :"))
    yi = float(input("y"+str(i)+" :"))
    x.append(xi)
    y.append(yi)
print 'x coordinates: ',x
print 'y coordinates: ',y

# n=10; x=[8,2,11,6,5,4,12,9,6,1]; y = [3,10,3,6,8,12,1,4,9,14]; # DEBUGGING

# Calculate sum of sx,sy,sx*sy,sx*sx
start_time = time.time()
for i in range(n):
    sx  += x[i]
    sy  += y[i]
    sxy += x[i]*y[i]
    sxx += x[i]*x[i]
    syy += y[i]*y[i] # for error estimate
  
b = (float(n)*sxy - sx*sy)/(float(n)*sxx - sx*sx)
a = (sy*sxx - sx*sxy)/(float(n)*sxx - sx*sx)

# Print the solution
print 'Least square fit is f = ', b, '* x + ', a
exec_time = time.time() - start_time
print 'Execution time is = ', exec_time, ' seconds'

# Error estimates
sxx    = sxx - float(n)*sx*sx 
syy    = syy - float(n)*sy*sy 
sxy    = sxy - float(n)*sx*sy
s      = math.sqrt(abs((syy - sxy*sxy/sxx)/(n-2))); # variance of residue 
aSE    = s*math.sqrt(abs(float(1.0)/n + sx*sx/sxx)) # standard error in a
bSE    = s/math.sqrt(abs(sxx))                      # standard error in b
apbx   = list([(a+i*b) for i in x])                 # a + bx by list comprehension
yresid = list([(i-j) for i,j in zip(y,apbx)])       # residue = y - (a+bx)
Sresid = sum(list([math.pow(i,2) for i in yresid])) # sum of square of residue 
avgy   = sum(y)/len(y)                              # <y> 
vary   = sum(math.pow(avgy-i,2) for i in y)/len(y)  # <y^2>
Stot   = (len(y)-1)*vary  
Rsq    = 1 - Sresid/Stot                            # Goodness of fit

print 'Standard error for b and a is', bSE, 'and', aSE
print 'Correlation coefficient is', sxy*sxy/(sxx*syy),', Determination coefficient is', Rsq 
print 'Linear equation ', b, '* x + ', a, 'predicts ', Rsq*100, '% of the variance in the variable y'

"""
Results
Check for x=[8,2,11,6,5,4,12,9,6,1], 
          y=[3,10,3,6,8,12,1,4,9,14], 
Least square fit f = -1.10641891892*x + 14.0810810811;
Standard error for b and a is 0.0429212485802 and 0.311881280309
Correlation coefficient is 1.01232586267 , Determination coefficient is 0.859042023952
Linear equation  -1.10641891892 * x +  14.0810810811 predicts  85.9042023952 % of the variance in the variable y

GNUPLOT
=======
f(x) = b*x + a
fit f(x) 'input.dat' u 1:2 via b,a
plot 'input.dat' u 1:2 title 'Experimental data' with points, f(x) title 'Straight line fit'
set xlabel "x"
set ylabel "y=f(x)"
set tics font "Helvetica,16"
set output 'figure.eps'
set terminal postscript color
replot
quit

OCTAVE
=======
data = load('input.dat');
x = data(:,1); y = data(:,2);
yy = -1.10641891892 * x + 14.0810810811; 
plot(x, y, 'bo'); hold on; plot(x, yy, 'r-'); hold off; xlabel('x'); ylabel('y=f(x)');
p = polyfit(x, y, 1)   % straight line i 1 is polynomial of degree 1
yprime = p(1)*x + p(2) % this can also be obtained as, yprime = polyval(p,x);
yresidue = y - yprime; % residuals
Sresidue = sum(yresidue.^2); 
Stotal   = (length(y)-1)*var(y,1);
Rsq = 1 - Sresidue/Stotal

"""
