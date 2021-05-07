%===================================================================% 
% Registration : xxxx
% (CFD Exercise (in OCTAVE) from Hundsdorfer & Verwer)
% Solve: u_t = -a u_x, 0<x<1, u(0,t)=u(1,t), u(x,0) = sin(pi*x).^100;
% Author : AKB
%===================================================================%
clear; clf; close; 

% Use switch between different cases to compare
adv_euler         = 0; % Advection Euler Sine function
adv_beuler_upwind = 0; % Advection Backward Euler Sine function 
adv_cn_upwind     = 0; % Advection Crank-Nicholson 3rd order Upwind
dif_step_beuler   = 0; % Diffusion Backward Euler Step function
dif_step_cn       = 1; % Diffusion Crank Nicholson Step function
dif_sin_beuler    = 0; % Diffusion Backward Euler Sine function
dif_sin_cn        = 0; % Diffusion Crank Nicholson Sine function

%============== Advection for u(x,0) = sin(pi*x)^100 periodic BC ===============%

%%%%%% Forward Euler %%%%%
if(adv_euler)  

  fprintf('Advection for u(x,0) = sin(pi*x)^100 periodic BC Forward Euler\n');
  N=5e2; deltax=1/N; x=deltax*[1:N]; 
  a=1.0; tstep=1/(1*N); t=1;   
  nu=a*tstep/deltax
  
  % Initial condition
  u=sin(pi*x).^100; u=u(:);
  %plot(x, u, 'r.-'); hold on; `
  
  % Arrange circulant matrix A for solving Ax=B.
  c1 = ones(N,1)*(nu/6.0);
  c2 = ones(N,1)*(nu/2.0);
  c3 = ones(N,1)*(nu);
  A = spdiags([-2*c1 1-c2 c3 -c1], -1:2, N, N); 
  A=A';
  
  % Populate the corner elements
  A(N,1) = -2*c1(N); A(1,N) = c3(N); A(1,N-1) = -c1(N); A(2,N) = -c1(1); 
  %full(A)
  
  for p = 0:tstep:t

      u_new = A*u; u_new = u_new(:); u = u(:);
   
      % Check L2 norm & conservation
      err = norm((A*u_new)'-u', 2)
      %sum1=sum(u(:))
      %sum2=sum(u_new(:))
      
      u=u_new; 

      figure(1); plot(x, sin(pi*(x-a*p)).^100, 'r.-'); hold on; 
      plot(x, u, 'b.-'); hold off; axis tight; xlabel('x'); ylabel('u(x,t)');
      legend('True','Computed');
      title('Advection Forward Euler with Sine initial condition'); pause(.1);

  end
end 

%%%%%%%% Backward-Euler 3rd-order upwind scheme %%%%%%%%
if(adv_beuler_upwind)
  
  fprintf('Advection for u(x,0) = sin(pi*x)^100 periodic BC Backward Euler\n');
  N = 5e2; deltax=1/N; x=deltax*[1:N]; k=-N/2+1:N/2; a=1.0; t=1; 
  tstep=1/(1*N)
  nu=a*tstep/deltax
  
  % Initial condition
  u=sin(pi*x).^100; %plot(x, u, 'r.-'); hold on; `
  
  % Arrange circulant matrix A for solving Ax=B.
  c1 = ones(N,1)*(nu/6.0);
  c2 = ones(N,1)*(nu/2.0);
  c3 = ones(N,1)*(nu);
  A = spdiags([2*c1 1+c2 -c3 c1], -1:2, N, N); 
  A=A';
  
  % Populate the corner elements
  A(N,1) = 2*c1(N); A(1,N) = -c3(N); A(1,N-1) = c1(N); A(2,N) = c1(1); 
  
  % Check: whether correctly populated
  %full(A)
  [L,U] = lu(A);
  
  for p = 0:tstep:t
      u_new = (U\(L\u'))';
      
      % Check L2 norm & conservation
      err = norm(A*u_new'-u', 2)
      %sum1=sum(u(:))
      %sum2=sum(u_new(:))
      
      u=u_new; 
      
      % Plot results and compare with analytic expression
      figure(1); plot(x, sin(pi*(x-a*p)).^100, 'r.-'); hold on; 
      plot(x, u_new, 'b.-'); hold off; axis tight; xlabel('x'); ylabel('u(x,t)');
      legend('True','Computed');
      title('Advection Backward Euler with Sine initial condition'); pause(.1);
      
      % Check spectrum
      uk = fft(u); uk = uk.*conj(uk); uk = fftshift(uk);  
      figure(2); plot(k, uk, 'r.-'); axis tight; pause(.1)   
  end
end
  
%%%% Crank-Nicholson 3rd order upwind scheme %%%%
if(adv_cn_upwind)
  
  fprintf('Advection for u(x,0) = sin(pi*x)^100 periodic BC Crank-Nicholson\n');
  N=5e2; deltax=1/N; x=deltax*[1:N]; k=-N/2+1:N/2; a=1.0; t=1; 
  tstep=1/(1e-0*N)  
  nu=a*tstep/deltax
 
  % Initial condition
  u=sin(pi*x).^100; %plot(x, u, 'r.-'); hold on;
 
  % Arrange circulant matrix A for solving Ax=B.
  c1 = ones(N,1)*(nu/12.0); 
  c2 = ones(N,1)*(nu/4.0); 
  c3 = ones(N,1)*(nu/2.0); 
  A = spdiags([2*c1 1+c2 -c3 c1], -1:2, N, N); A=A';
  A(N,1) = 2*c1(N); A(1,N) = -c3(N); A(1,N-1) = c1(N); A(2,N) = c1(1); 
  %full(A)
 
  [L,U] = lu(A);
  
  for p = 0:tstep:t
     
     % One way (I prefer) to populate the right hand side
     B = spdiags([-2*c1 1-c2 c3 -c1], -1:2, N, N); B=B';
     B(N,1) = -2*c1(N); B(1,N) = c3(N); B(1,N-1) = -c1(N); B(2,N) = -c1(1);
     u = B*u(:); u=u';
     
     % Another way to populate the right hand side
     % w(1) = -(2*nu/12.0)*u(2) + (1-(nu/4.0))*u(1) + (nu/2.0)*u(N) - (nu/12.0)*u(N-1);
     % w(2) = -(2*nu/12.0)*u(3) + (1-(nu/4.0))*u(2) + (nu/2.0)*u(1) - (nu/12.0)*u(N);
     % w(N) = -(2*nu/12.0)*u(1) + (1-(nu/4.0))*u(N) + (nu/2.0)*u(N-1) - (nu/12.0)*u(N-2);
     % for i=3:N-1
     %     w(i) = -(2*nu/12.0)*u(i+1) + (1-(nu/4.0))*u(i) + (nu/2.0)*u(i-1) - (nu/12.0)*u(i-2);
     % end
     % u=w; clear w; % w is a dummy vector using which right hand side is computed.
 
     u_new = (U\(L\u'))';
     
     % Check error and conservation
     err = norm(A*u_new'-u', 2)
     %sum1=sum(u(:));
     %sum2=sum(u_new(:));
     
     u=u_new;
     
     figure(1); plot(x, sin(pi*(x-a*p)).^100, 'r.-'); hold on; 
     plot(x, u_new, 'b.-'); hold off; axis tight; xlabel('x'); ylabel('u(x,t)');
     legend('True','Computed');
     title('Advection Crank-Nicholson Upwind with Sine initial condition'); pause(.1);
     
     % Check spectrum
     %uk = fft(u); uk = uk.*conj(uk); uk = fftshift(uk);  
     %figure(2); plot(k, uk, 'r.-'); axis tight; pause(.1)
     
  end
end
%=====================================================================%

%============== Diffusion for Step function fixed BC =================%

%%%%% Backward Euler %%%%%%
if(dif_step_beuler)
  
  fprintf('Diffusion for u(x,0) = step fixed BC Backward Euler\n');
  N=1e2; deltax=1/N; x=deltax*[1:N]; t=1000; k=-N/2+1:N/2; 
  tstep=2/(1*N) 
  nu=tstep/(2*deltax^2)
 
  % Initial condition
  u = heaviside(x-.5); u(N/2)=0; %u=u(2:N-1); x = x(2:N-1); 

  c = ones(N,1)*nu;
  A = spdiags([-c 1+2*c -c], -1:1, N, N); A = A';
  %full(A)
 
  [L,U] = lu(A);
 
  for p = 0:tstep:t
     
     u(1) = 0.0; u(N) = u(N) + c(1); 
     
     u_new = (U\(L\u'))';
     
     % Check error and conservation
     err = norm(A*u_new'-u', 2)
     %sum1=sum(u(:))
     %sum2=sum(u_new(:))
     
     u=u_new; fx=.5*( 1+ (erf((x-.5)/sqrt(4*t))/erf(.5/sqrt(4*t))) );
     
     figure(1); plot(x, u, 'b.-'); hold on; plot(x, fx,'r.-'); 
     hold off; axis tight; xlabel('x'); ylabel('u(x,t)');
     legend('Computed','True');
     title('Diffusion Backward Euler with Step initial condition'); pause(.1);
    
     %uk = fft(u); uk=fftshift(uk); uk = uk.*conj(uk);   
     %figure(2); plot(k, uk, 'r.-'); pause(.1)
     
  end
end

%%%%%% Crank Nicholson %%%%%%
if(dif_step_cn)
  
  fprintf('Diffusion for u(x,0) = step fixed BC Crank Nicholson\n');
  N=100; deltax=1/N; x=deltax*[1:N]; t=1000; k=-N/2+1:N/2; 
  tstep=2/(10*N)
  nu=tstep/(2*deltax^2)

  % Initial condition
  u = heaviside(x-.5); u(N/2)=0; %u=u(2:N-1);

  c = ones(N,1)*nu;
  c1 = ones(N,1)*nu/2.0;
  A = spdiags([-c1 1+c -c1], -1:1, N, N);
  %full(A)

  [L,U] = lu(A);

  for p = 0:tstep:t
    
     B = spdiags([c1 1-c c1], -1:1, N, N); B=B';
     u = B*u(:); u=u'; 
     u(1) = 0.0; u(N) = u(N) + c(1); % Different factor than BE.

     u_new = (U\(L\u'))'; 
     err = norm(A*u_new'-u', 2)
     %sum1 = sum(u(:))
     %sum2 = sum(u_new(:))
     u = u_new; 
     fx=.5*( 1+ (erf((x-.5)/sqrt(4*t))/erf(.5/sqrt(4*t))) ); 
    
     figure(1); plot(x, u, 'b.-'); hold on; plot(x, fx,'r.-'); 
     hold off; axis tight; xlabel('x'); ylabel('u(x,t)');
     legend('Computed','True');
     title('Diffusion Crank Nicholson with Step initial condition'); pause(.1);
    
     uk = fft(u); uk=fftshift(uk); uk = uk.*conj(uk);   
     %figure(3); plot(k, uk, 'r.-'); pause(.1)

   end 
end

%============== Diffusion for sin(pi*x)^100 periodic BC =================%

%%%%%%% Diffusion backward Euler %%%%%%%%
if(dif_sin_beuler)
  
  fprintf('Diffusion for u(x,0) = sin(pi*x)^100 periodic BC Backward Euler\n');
  N=1e3; deltax=1/N;
  x=deltax*[1:N]; t=1; 
  tstep=1/(10*N)   
  nu=tstep/(deltax^2)
 
  % Initial condition
  u=sin(pi*x).^100;
 
  % Step function
  %u = heaviside(x-.5); u(N/2)=0; 
 
  c = ones(N,1)*nu;
  A = spdiags([-c 1+2*c -c],-1:1,N,N);
  A(N,1) = -c(N); A(1,N) = -c(1);
  %full(A)
  
  [L,U] = lu(A);
  k=-N/2+1:N/2;
 
  for p = 0:tstep:t
 
     u_new = (U\(L\u'))';
     err = norm(A*u_new'-u', 2)
     %sum1=sum(u(:))
     %sum2=sum(u_new(:))

     u=u_new;
     
     figure(1); plot(x, u, 'b.-'); ylim([0 1]); xlabel('x'); ylabel('u(x,t)');
     title('Diffusion Backward Euler with Sine initial condition'); pause(.1);
     if(p==0.16) 
        print -djpg image.jpg
     end
  
     %uk = fft(u); uk=fftshift(uk); uk = uk.*conj(uk);   
     %figure(3); plot(k, uk, 'r.-'); pause(.1);
 
  end
end

%%%%%%% Diffusion Crank Nicholson %%%%%%%%
if(dif_sin_cn)
  
  fprintf('Diffusion for u(x,0) = sin(pi*x)^100 periodic BC Crank Nicholson\n');
  N=1e3; deltax=1/N; x=deltax*[1:N]; t=1; tstep=1/(10*N) 
  nu=tstep/(deltax^2)
 
  % Initial condition
  u=sin(pi*x).^100; 
 
  % Step function
  %u = heaviside(x-.5); u(N/2)=0; 
 
  c = ones(N,1)*nu;
  c1 = ones(N,1)*nu/2.0;
  A = spdiags([-c1 1+c -c1], -1:1, N, N);
  A(N,1) = -c1(N); A(1,N) = -c1(1);
 
  [L,U] = lu(A);
 
  k=-N/2+1:N/2;
 
  for p = 0:tstep:t
      
     B = spdiags([c1 1-c c1], -1:1, N, N); B=B';
     B(N,1) = c1(N); B(1,N) = c1(N); 
     u = B*u(:); u=u';

     u_new = (U\(L\u'))';
     err = norm(A*u_new'-u', 2)
     %sum1 = sum(u(:))
     %sum2 = sum(u_new(:))
     u = u_new; 
     
     figure(1); plot(x, u, 'b.-'); ylim([0 1]); xlabel('x'); ylabel('u(x,t)');
     title('Diffusion Crank-Nicholson with Sine initial condition'); pause(.1);
     
     %uk = fft(u); uk=fftshift(uk); uk = uk.*conj(uk);   
     %figure(2); plot(k, uk, 'r.-'); pause(.1);
     
 end
end
%=====================================================================%

function y = heaviside(x)
  if (nargin < 1)
    print_usage ();
  end
  
  zero_value = 0.5;
  y = cast (x > 0, class (x));
  y (x == 0) = zero_value;
end

