% Batten, Bang, Kopell et al (2024) Dopamine and serotonin in human
% substantia nigra track social context and value signals during economic
% exchange
%
% Figure 4
%
% Visualization and analysis of relative dopamine/serotonin
%
% Written in MATLAB 2023a
%
% Dan Bang danbang@cfin.au.dk 2024

%% -----------------------------------------------------------------------
%% PREPARATION

% Fresh memory
clear;

% Custom functions
addpath('Functions');

% Paths [edit 'getBase' according to local setup]
fs= filesep;
dirBase= getBase;
dirDataB= [dirBase,fs,'Data',fs,'Behaviour']; % behaviour
dirDataE= [dirBase,fs,'Data',fs,'Electrochemistry']; % electrochemistry

% Neuromodulators
v_NT_file= {'DA','SE'};
v_NT_plot= {'DA','5-HT'};
c_event= 'offer';

% Subjects
n_sbj= 4;

%% -----------------------------------------------------------------------
%% VISUALIZATION: PARSE DATA FOR PLOTTING

% Loop through NTs
for i_NT= 1:2

    % Initialise dataset id
    i_ds = 0;

    % Loop through subjects
    for i_sbj= 1:n_sbj

        % Loop through sessions
        for i_ses= 1:2

            % update dataset idx
            i_ds= i_ds+1;

            % Load data
            load([dirDataB,fs,'MSSM','_Sbj',num2str(i_sbj),'_Ses',num2str(i_ses),'.mat']);
            load([dirDataE,fs,'MSSM','_Sbj',num2str(i_sbj),'_Ses',num2str(i_ses),'_',v_NT_file{i_NT},'_',c_event,'.mat']);

            % RT outlier
            data.outlier= data.rt>14;
            data.outlierP= [0 data.outlier(1:end-1)];

            % Compute NT AUCs (31 = event onset)
            AUC= sum(timeSeries(:,32:41)-timeSeries(:,31),2);

            % Value difference
            data.valueD= [0 data.value(2:end)-data.value(1:end-1)];

            % Compute AUC in tercicles
            c_trials= find(data.trial>1 & ~data.outlier & ~data.outlierP);
            AUCz= zscore(AUC(c_trials));
            value= zscore(data.value(c_trials));
            valueD= zscore(data.valueD(c_trials));
            % Value
            var= value;
            quaz= quantile(var,2);
            binz= [];
            for i_trial= 1:length(var)
                binz(i_trial)= sum(var(i_trial)>quaz)+1; 
            end
            for i_bin= 1:length(unique(binz))
                stats4plot.NT{i_NT}.value(i_ds,i_bin)= mean(AUCz(binz==i_bin));
            end     
            % VALUE DIFFERENCE
            var= valueD;
            quaz= quantile(var,2);
            binz= [];
            for i_trial= 1:length(var)
                binz(i_trial)= sum(var(i_trial)>=quaz)+1; 
            end
            for i_bin= 1:length(unique(binz))
                stats4plot.NT{i_NT}.valueD(i_ds,i_bin)= mean(AUCz(binz==i_bin));
            end     
            
        end

    end

end

%% -----------------------------------------------------------------------
%% VISUALIZATION: PLOT DATA

%% General specifications
conColz= [0 1 1;  % computer
          1 0 1]; % human
alphaz= .6;
lw= 2;
axisFS= 24;
labelFS= 32;
titleFS= 16;
ms= 16;

%% Figure 4: value
% Loop through NTs
for i_NT= 1:2
    % Create figure
    figure('color',[1 1 1]);
    hold on;
    % Reference line
    plot([0 4],[0 0],'k-','LineWidth',lw);
    % Plot data
    dat= stats4plot.NT{i_NT}.value;
    mu= mean(dat);
    sem= std(dat)./sqrt(size(dat,1));
    plot(mu,'-','color','k','LineWidth',lw);
    for i_bin= 1:3
        plot([i_bin i_bin],[mu(i_bin)-sem(i_bin) mu(i_bin)+sem(i_bin)],'-','color','k','LineWidth',lw);
        plot(i_bin,mu(i_bin),'o','color','k','MarkerFaceColor',[146 155 255]./255,'MarkerSize',ms,'LineWidth',lw);
    end   
    % Tidy up
    xlim([0 4]);
    ylim([-.35 .35]);
    set(gca,'XTick',1:3,'XTickLabel',{'Low','Medium','High'});
    set(gca,'YTick',[-.3:.1:.3]);
    set(gca,'FontSize',axisFS,'LineWidth',lw);
    xlabel('Value','FontSize',labelFS);
    ylabel('Relative estimate [z]','FontSize',labelFS);
    axis square;
    % Save
    print('-djpeg','-r300',['Figures/Figure-4-Value-',v_NT_file{i_NT}]);
end

%% Figure 4: valueD
% Loop through NTs
for i_NT= 1:2
    % Create figure
    figure('color',[1 1 1]);
    hold on;
    % Reference line
    plot([0 4],[0 0],'k-','LineWidth',lw);
    % Plot data
    dat= stats4plot.NT{i_NT}.valueD;
    mu= mean(dat);
    sem= std(dat)./sqrt(size(dat,1));
    plot(mu,'-','color','k','LineWidth',lw);
    for i_bin= 1:3
        plot([i_bin i_bin],[mu(i_bin)-sem(i_bin) mu(i_bin)+sem(i_bin)],'-','color','k','LineWidth',lw);
        plot(i_bin,mu(i_bin),'o','color','k','MarkerFaceColor',[255 159 111]./255,'MarkerSize',ms,'LineWidth',lw);
    end   
    % Tidy up
    xlim([0 4]);
    ylim([-.35 .35]);
    set(gca,'XTick',1:3,'XTickLabel',{'Neg.','Zero','Pos.'});
    set(gca,'YTick',[-.3:.1:.3]);
    set(gca,'FontSize',axisFS,'LineWidth',lw);
    xlabel('Value difference','FontSize',labelFS);
    ylabel('Relative estimate [z]','FontSize',labelFS);
    axis square;
    % Save
    print('-djpeg','-r300',['Figures/Figure-4-ValueD-',v_NT_file{i_NT}]);
end

%% -----------------------------------------------------------------------
%% ANALYSIS: COLLATE DATA AND RUN GROUP-LEVEL ANALYSIS

% Loop through NTs
for i_NT= 1:2

    % Initialise variables for collating across datasets
    lmedatG= [];
    lmedatG.subject= [];
    lmedatG.dataset= [];
    lmedatG.block= [];
    lmedatG.trial= [];
    lmedatG.human= [];
    lmedatG.value= [];
    lmedatG.valueD= [];
    lmedatG.accept= [];
    lmedatG.rt= [];
    lmedatG.AUC= [];

    % Initialise dataset id
    i_ds = 0;

    % Loop through subjects
    for i_sbj= 1:n_sbj

        % Loop through sessions
        for i_ses= 1:2

            % update dataset idx
            i_ds= i_ds+1;

            % Load data
            load([dirDataB,fs,'MSSM','_Sbj',num2str(i_sbj),'_Ses',num2str(i_ses),'.mat']);
            load([dirDataE,fs,'MSSM','_Sbj',num2str(i_sbj),'_Ses',num2str(i_ses),'_',v_NT_file{i_NT},'_',c_event,'.mat']);

             % RT outlier
            data.outlier= data.rt>14;
            data.outlierP= [0 data.outlier(1:end-1)];

            % Compute NT AUCs (31 = event onset)
            AUC= sum(timeSeries(:,32:41)-timeSeries(:,31),2);

            % Value difference
            data.valueD= [0 data.value(2:end)-data.value(1:end-1)];

            % Collate
            % Decision
            idx= find(data.trial>1 & ~data.outlier & ~data.outlierP);
            lmedatG.subject= [lmedatG.subject data.subject(idx)];
            lmedatG.dataset= [lmedatG.dataset ones(1,length(idx)).*i_ds];
            lmedatG.block=   [lmedatG.block data.block(idx)];
            lmedatG.trial=   [lmedatG.trial data.trial(idx)];
            lmedatG.human=   [lmedatG.human data.human(idx)];
            lmedatG.value=   [lmedatG.value zscore(data.value(idx))];
            lmedatG.valueD=  [lmedatG.valueD zscore(data.valueD(idx))];
            lmedatG.accept=  [lmedatG.accept data.accept(idx)];
            lmedatG.rt=      [lmedatG.rt zscore(data.rt(idx))];
            lmedatG.AUC=     [lmedatG.AUC zscore(AUC(idx))'];

        end

    end

    %% MIXED-EFFECTS MODEL
    % Extract data
    idx         = 1:length(lmedatG.subject);
    subject     = lmedatG.subject(idx)';
    dataset     = lmedatG.dataset(idx)';
    block       = (lmedatG.block(idx)-1.5)';
    condition   = ((lmedatG.human(idx)*2-1)/2)';
    value       = lmedatG.value(idx)';
    valueD      = lmedatG.valueD(idx)';
    [b,dev,stats]= glmfit(value,valueD);
    valueDR     = stats.resid;
    valueA      = abs(lmedatG.valueD(idx))';
    choice      = ((lmedatG.accept(idx)*2-1)/2)';
    rt          = lmedatG.rt(idx)';
    NT          = lmedatG.AUC(idx)';
    % Transform to table
    datanames   = {'dataset','subject','block', ...
                   'condition','value','valueD','valueDR','valueA','choice','rt', 'NT'};
    datatab     = table(categorical(dataset),categorical(subject),block, ...
                  condition,value,valueD,valueDR,valueA,choice,rt,NT, ...
                  'VariableNames',datanames);
    % LME N-M3 (RELATIVE NT)
    % With Random effects
    formulaz= ['NT ~ 1 + value + valueD + (1 + value + valueD | dataset)'];
    lmehat1{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
    % Without random effects
    formulaz= ['NT ~ 1 + value + valueD + (1 | dataset)'];
    lmehat1NoRan{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
    % LME N-M3* (RELATIVE NT)
    % With Random effects
    formulaz= ['NT ~ 1 + value + valueDR + (1 + value + valueDR | dataset)'];
    lmehat2{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
    % Without random effects
    formulaz= ['NT ~ 1 + value + valueDR + (1 | dataset)'];
    lmehat2NoRan{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
    % LME N-M4 (RELATIVE NT)
    % With Random effects
    formulaz= ['NT ~ 1 + value + valueD + valueA + (1 + value + valueD + valueA | dataset)'];
    lmehat3{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
    % Without random effects
    formulaz= ['NT ~ 1 + value + valueD + valueA + (1 | dataset)'];
    lmehat3NoRan{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
    % LME N-M5 (RELATIVE NT)
    % With Random effects
    formulaz= ['NT ~ 1 + condition * (value + valueD) + (1 + condition * (value + valueD) | dataset)'];
    lmehat4{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
    % Without random effects
    formulaz= ['NT ~ 1 + condition * (value + valueD) + (1 | dataset)'];
    lmehat4NoRan{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');

end