% Runge Phenomena 
% Author : AKB

n = 6;               % Number of grid points 
x = -1 + 2*(0:n)'/n; % x-grid [-1,1]
g = (-1:.02:1)';     % g-grid 100 points
y = Interpol(x, g);
plot(g, f(g), 'k', g, y, 'ro');
xlabel('x'); ylabel('f(x)'); legend('True','Interpolated');
title(['Runge phenomena with grid Points = ' num2str(n)]);

function y = Interpol(x,G)
   A = ones(length(x),1);
   for k = 1:length(x)-1
       A = [A x.^k];
   end;
   cf = A\f(x); cf = cf(end:-1:1);
   y = polyval(cf,G);
end

function y = f(x)
   a = 0.2; 
   y = 1./(x.*x+a*a);
end
