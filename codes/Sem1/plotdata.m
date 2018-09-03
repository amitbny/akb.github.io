% Octave/MATLAB file to plot and check data

x  = [8,2,11,6,5,4,12,9,6,1]; 
y  = [3,10,3,6,8,12,1,4,9,14]; 
yy = -1.10641891892 * x + 14.0810810811; 
plot(x, y, 'bo'); hold on; plot(x, yy, 'r-'); hold off;
p = polyfit(x, y, 1) % straight line i 1 is polynomial of degree 1

