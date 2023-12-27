% Batten, Bang, Kopell et al (2024) Dopamine and serotonin in human
% substantia nigra track social context and value signals during economic
% exchange
%
% Figure 3
%
% Visualization and analysis of overall dopamine/serotonin
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

            % Compute NT AUCs (31 = event onset)
            AUC= sum(timeSeries(:,32:41),2);

            % Compute mean NT by condition and order
            % Prepare
            c_trials= find(~data.outlier);
            zAUC= zscore(AUC(c_trials));
            cond= data.human(c_trials);
            if data.human(1)==1; humFirst = 1; else humFirst=0; end
            % Compute
            if humFirst
                stats4plot.NT{i_NT}.humFirst.mean(i_sbj,:)= [mean(zAUC(cond==1)) mean(zAUC(cond==0))];
            else
                stats4plot.NT{i_NT}.comFirst.mean(i_sbj,:)= [mean(zAUC(cond==0)) mean(zAUC(cond==1))];
            end

            % Computate trial-by-trial NT
            % Prepare
            c_trials= find(~data.outlier);
            zAUC= zscore(AUC(c_trials));
            tmp= NaN(1,60);
            tmp(c_trials)= zAUC;
            if data.human(1)==1; humFirst = 1; else humFirst=0; end
            % Compute
            if humFirst
                stats4plot.NT{i_NT}.humFirst.trial(i_sbj,:)= tmp;
            else
                stats4plot.NT{i_NT}.comFirst.trial(i_sbj,:)= tmp;
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

%% Figure 3a
% Loop through NTs
for i_NT= 1:2
    % Create figure
    figure('color',[1 1 1]);
    hold on;
    % Reference line
    plot([.5 2.5],[0 0],'k-','LineWidth',lw);
    % Human -> Computer
    mu= mean(stats4plot.NT{i_NT}.humFirst.mean);
    se= std(stats4plot.NT{i_NT}.humFirst.mean)./sqrt(size(stats4plot.NT{i_NT}.humFirst.mean,1));
    plot([1 1],[mu(1)-se(1) mu(1)+se(1)],'k-','LineWidth',lw);
    plot([2 2],[mu(2)-se(2) mu(2)+se(2)],'k-','LineWidth',lw);
    plot([1 2],[mu(1) mu(2)],'k-','LineWidth',lw);
    plot(1,mu(1),'ko','MarkerFaceColor',conColz(2,:),'MarkerSize',ms,'LineWidth',lw);
    plot(2,mu(2),'ko','MarkerFaceColor',conColz(1,:),'MarkerSize',ms,'LineWidth',lw);
    % Computer -> Human
    mu= mean(stats4plot.NT{i_NT}.comFirst.mean);
    se= std(stats4plot.NT{i_NT}.comFirst.mean)./sqrt(size(stats4plot.NT{i_NT}.comFirst.mean,1));
    plot([1 1],[mu(1)-se(1) mu(1)+se(1)],'k-','LineWidth',lw);
    plot([2 2],[mu(2)-se(2) mu(2)+se(2)],'k-','LineWidth',lw);
    plot([1 2],[mu(1) mu(2)],'k-','LineWidth',lw);
    plot(1,mu(1),'ko','MarkerFaceColor',conColz(1,:),'MarkerSize',ms,'LineWidth',lw);
    plot(2,mu(2),'ko','MarkerFaceColor',conColz(2,:),'MarkerSize',ms,'LineWidth',lw);
    % Tidy up
    xlim([.5 2.5]);
    ylim([-.8 .8]);
    set(gca,'XTick',1:2,'XTickLabel',{'First','Second'});
    set(gca,'YTick',-.6:.3:6);
    set(gca,'FontSize',axisFS,'LineWidth',lw);
    ylabel('Overall estimate [z]','FontSize',labelFS);
    xlabel(['Block'],'FontSize',labelFS);
    axis square;
    % Save
    print('-djpeg','-r300',['Figures/Figure-3a-',v_NT_file{i_NT}]);
end

%% Figure 3b: Human -> Computer
% Loop through NTs
for i_NT= 1:2
    % Create figure
    figure('color',[1 1 1]);
    hold on;
    % Reference line and shading
    fill([1 1 30.5 30.5],[-3 3 3 -3],conColz(2,:),'Edgecolor','none','FaceAlpha',.3);
    fill([30.5 30.5 60 60],[-3 3 3 -3],conColz(1,:),'Edgecolor','none','FaceAlpha',.3);
    plot([0 61],[0 0],'k-','LineWidth',2);
    % Plot data
    dat= stats4plot.NT{i_NT}.humFirst.trial;
    shadedLineMeanSte(dat,lw,'-',[0 0 0])
    % Tidy up
    set(gca,'XTick',[1 15 31 45 60]);
    set(gca,'YTick',-2:1:2);
    ylim([-2.5 2.5]);
    xlim([0 61]);
    set(gca,'FontSize',axisFS,'LineWidth',lw);
    xlabel('Trial','FontSize',labelFS);
    ylabel('Overall estimate [z]','FontSize',labelFS);
    axis square;
    % Save
    print('-djpeg','-r300',['Figures/Figure-3b-HumCom-',v_NT_file{i_NT}]);
end

%% Figure 3b: Computer -> Human
% Loop through NTs
for i_NT= 1:2
    % Create figure
    figure('color',[1 1 1]);
    hold on;
    % Reference line and shading
    fill([1 1 30.5 30.5],[-3 3 3 -3],conColz(1,:),'Edgecolor','none','FaceAlpha',.3);
    fill([30.5 30.5 60 60],[-3 3 3 -3],conColz(2,:),'Edgecolor','none','FaceAlpha',.3);
    plot([0 61],[0 0],'k-','LineWidth',2);
    % Plot data
    dat= stats4plot.NT{i_NT}.comFirst.trial;
    shadedLineMeanSte(dat,lw,'-',[0 0 0])
    % Tidy up
    set(gca,'XTick',[1 15 31 45 60]);
    set(gca,'YTick',-2:1:2);
    ylim([-2.5 2.5]);
    xlim([0 61]);
    set(gca,'FontSize',axisFS,'LineWidth',lw);
    xlabel('Trial','FontSize',labelFS);
    ylabel('Overall estimate [z]','FontSize',labelFS);
    axis square;
    % Save
    print('-djpeg','-r300',['Figures/Figure-3b-ComHum-',v_NT_file{i_NT}]);
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

            % Compute NT AUCs (31 = event onset)
            AUC= sum(timeSeries(:,32:41),2);

            % Collate
            % Decision
            idx= find(~data.outlier);
            lmedatG.subject= [lmedatG.subject data.subject(idx)];
            lmedatG.dataset= [lmedatG.dataset ones(1,length(idx)).*i_ds];
            lmedatG.block=   [lmedatG.block data.block(idx)];
            lmedatG.trial=   [lmedatG.trial data.trial(idx)];
            lmedatG.human=   [lmedatG.human data.human(idx)];
            lmedatG.value=   [lmedatG.value zscore(data.value(idx))];
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
    choice      = ((lmedatG.accept(idx)*2-1)/2)';
    rt          = lmedatG.rt(idx)';
    NT          = lmedatG.AUC(idx)';
    % Transform to table
    datanames   = {'dataset','subject','block', ...
                   'condition','value','choice','rt', 'NT'};
    datatab     = table(categorical(dataset),categorical(subject),block, ...
                  condition,value,choice,rt,NT, ...
                  'VariableNames',datanames);
    % LME N-M1 (OVERALL NT)
    % With Random effects
    formulaz= ['NT ~ 1 + choice*condition + (1 + choice*condition | dataset)'];
    lmehat1{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
    % Without random effects
    formulaz= ['NT ~ 1 + choice*condition + (1 | dataset)'];
    lmehat1NoRan{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
    % LME N-M2 (OVERALL NT)
    % With Random effects
    formulaz= ['NT ~ 1 + choice*condition*block + (1 + choice*condition*block | dataset)'];
    lmehat2{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
    % Without random effects
    formulaz= ['NT ~ 1 + choice*condition*block + (1 | dataset)'];
    lmehat2NoRan{i_NT} = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');

end