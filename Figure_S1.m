% Batten, Bang, Kopell et al (2024) Dopamine and serotonin in human
% substantia nigra track social context and value signals during economic
% exchange
%
% Figure S1
%
% Visualization of in-vitro evaluation of signal prediction model
%
% Written in MATLAB 2023a
%
% Dan Bang danbang@cfin.au.dk & Seth R. Batten srbatten10@vt.edu 2024

%% -----------------------------------------------------------------------
%% PREPARATION

% Fresh memory
clear;

% Custom functions
addpath('Functions');

% Paths [edit 'getBase' according to local setup]
fs= filesep;
dirBase= getBase;
dirDataC= [dirBase,fs,'Data',fs,'Calibration']; % calibration

% Analytes
v_NT_file= {'DA','SE','NE'};
v_NT_plot= {'DA','5-HT','NE'};

%% -----------------------------------------------------------------------
%% VISUALIZATION: PARSE AND PLOT DATA

% Indices for extracting data from files
tableidx_true= 2; % column: true concentration
tableidx_pred= [4 6 10 8]; % columns: predicted DA/5-HT/NE/pH

% Visual specifications
col_DA= [137 168 255]./255;
col_SE= [255 153 151]./255;
col_NE= [125 255 125]./255;
colz= [col_DA; col_SE; col_NE];
alphaz= .2;
lw= 2;
axisFS= 22;
labelFS= 32;
titleFS= 16;
ms= 10;

% Loop through true NTs
for i_true= 1:3
    
    % Initialise figure
    figure('color',[1 1 1]);
    hold on;
    
    % Load data
    c_data= importdata([dirDataC,fs,'Invitro_Calibration_',v_NT_file{i_true},'.csv']);
    
    % Reference line
    plot([-500 2750],[-500 2750],'k-','LineWidth',lw);
    
    % Loop through predicted NTs
    for i_pred= [1 2 3]
        % Plot
        x_data= c_data.data(:,tableidx_true);
        y_data= c_data.data(:,tableidx_pred(i_pred));
        plot(x_data,y_data,'o','MarkerSize',ms,'MarkerEdgeColor',colz(i_pred,:),'MarkerFaceColor',colz(i_pred,:)),
        % Tidy up
        xlim([-250 2750]);
        ylim([-250 2750]);
        set(gca,'XTick',0:500:2500);
        set(gca,'YTick',0:500:2500);
        set(gca,'FontSize',axisFS,'LineWidth',lw);
        xlabel(['True DA or 5-HT or NE [nM]'],'FontSize',labelFS);
        ylabel(['Predicted ',v_NT_plot{i_true},' [nM]'],'FontSize',labelFS);
        axis square;
    end
    print('-djpeg','-r300',['Figures/Figure-S1-',v_NT_file{i_true}]);
  
end