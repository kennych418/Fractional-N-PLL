fref = 100e6;
f0 = 5e9;   %Currently unused
fbw = 5e6;   %Arbitrary
S1MHz = -120;   %Arbitrary
N = 10;

KVCO_SS = 8.484e9;    
KVCO_NN = 11.403e9;
KVCO_FF = 16.289e9;   

b = 25;

zero1 = fbw / sqrt(b);
zero2 = fbw * sqrt(b);

PM = atand((sqrt(b)-1/sqrt(b))/2); 
IcpR = (b/(b-1))*(2*pi*N*fbw/KVCO_NN);
RC2 = sqrt(b)/(2*pi*fbw);

%% Calculate Capacitances + Resistance + Icp based on max area
Cmax = 20e-12;
C2 = Cmax*(b-1)/b;
C1 = C2/(b-1);
R = RC2/C2;
Icp = IcpR / R;

%% Verify Noise Contributions

%% Open Loop Response
Tau2 = RC2;
Taup = Tau2/b;
K = ((b-1)/b)*IcpR*KVCO_NN/(2*pi*N);

n = [K*Tau2, K];
d = [Tau2*Taup, Tau2, 0, 0];
T = tf(n,d);
figure(1);
bode(T);

%% Closed Loop Response
n = [N*Tau2, N];
d = [(Tau2*Taup/K), (Tau2/K), (Tau2), 1];
A = tf(n,d);
figure(2);
bode(A);
%freqs(n,d,w);