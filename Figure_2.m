% Batten, Bang, Kopell et al (2024) Dopamine and serotonin in human
% substantia nigra track social context and value signals during economic
% exchange
%
% Figure 2
%
% Visualization and analysis of behavioural data
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

% Subjects
n_sbj= 4;

%% -----------------------------------------------------------------------
%% VISUALIZATION: PARSE DATA FOR PLOTTING

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

        % RT outlier
        data.outlier= data.rt>14;

        % Decision: proportion accept as a function of value and condition 
        for i_con= 1:2
            c_trials= find(data.outlier~=1 & data.human==i_con-1);
            val= data.value(c_trials);
            dec= data.accept(c_trials);
            unique_val= sort(unique(val),'ascend');
            for i_val= 1:length(unique_val)
                stats4plot.dec.psych(i_ds,i_val,i_con)= mean(dec(val==unique_val(i_val)));
            end
        end

        % RT: mean reaction time as a function of decision
        c_trials= find(data.outlier~=1 & data.accept==0);
        stats4plot.rt.decision(i_ds,1)= mean(data.rt(c_trials));
        c_trials= find(data.outlier~=1 & data.accept==1);
        stats4plot.rt.decision(i_ds,2)= mean(data.rt(c_trials));
     
        % Emotion: mean emotion as a function of condition
        for i_con= 1:2
            c_trials= find(data.outlier~=1 & ~isnan(data.emotion) & data.human==i_con-1);
            stats4plot.emo.condition(i_ds,i_con)= mean(data.emotion(c_trials));
        end
    
    end

end

%% -----------------------------------------------------------------------
%% VISUALIZATION: PLOT DATA

%% General specifications
conColz= [0 1 1;  % computer
          1 0 1]; % human
decColz= [1 0 0;  % reject
          0 1 0]; % accept
alphaz= .6;
lw= 2;
axisFS= 24;
labelFS= 32;
titleFS= 16;
ms= 10;

%% Figure 2a
% Create figure
figure('color',[1 1 1]);
hold on;
% Plot data
% Computer
i_con= 1;
dat= squeeze(stats4plot.dec.psych(:,:,i_con));
shadedLineMeanSte(dat,lw,'-',conColz(i_con,:));
% Human
i_con= 2;
dat= squeeze(stats4plot.dec.psych(:,:,i_con));
shadedLineMeanSte(dat,lw,'-',conColz(i_con,:));
% Tidy up
xlim([0 10]);
ylim([0 1]);
set(gca,'XTick',1:9);
set(gca,'YTick',0:.2:1);
set(gca,'FontSize',axisFS,'LineWidth',lw);
ylabel('Accept','FontSize',labelFS);
xlabel('Offer value ($)','FontSize',labelFS);
axis square;
% Save
print('-djpeg','-r300',['Figures/Figure-2a']);

%% Figure 2b
% Create figure
figure('color',[1 1 1]);
hold on;
% Plot data
% Reject
i_con= 1;
dat= stats4plot.rt.decision(:,i_con);
mu= nanmean(dat);
sem= nanstd(dat)/sqrt(sum(~isnan(dat)));
bar(i_con,mu,'LineWidth',lw,'FaceColor',decColz(i_con,:),'EdgeColor','k','FaceAlpha',alphaz);
plot([i_con i_con],[mu-sem mu+sem],'k-','LineWidth',lw);
plot(ones(1,size(dat,1))*i_con,dat,'ko','MarkerSize',ms,'LineWidth',lw);
% Accept
i_con= 2;
dat= stats4plot.rt.decision(:,i_con);
mu= nanmean(dat);
sem= nanstd(dat)/sqrt(sum(~isnan(dat)));
bar(i_con,mu,'LineWidth',lw,'FaceColor',decColz(i_con,:),'EdgeColor','k','FaceAlpha',alphaz);
plot([i_con i_con],[mu-sem mu+sem],'k-','LineWidth',lw);
plot(ones(1,size(dat,1))*i_con,dat,'ko','MarkerSize',ms,'LineWidth',lw);
% Tidy up
xlim([0 3]);
ylim([1 7]);
set(gca,'XTick',1:2,'XTickLabel',{'Reject','Accept'});
set(gca,'YTick',1:1:7);
set(gca,'FontSize',axisFS,'LineWidth',lw);
ylabel('Reaction time (s)','FontSize',labelFS);
xlabel('Decision','FontSize',labelFS);
axis square;
% Save
print('-djpeg','-r300',['Figures/Figure-2b']);

%% Figure 2c
% Create figure
figure('color',[1 1 1]);
hold on;
% Computer
i_con= 1;
dat= stats4plot.emo.condition(:,i_con);
mu= nanmean(dat);
sem= nanstd(dat)/sqrt(sum(~isnan(dat)));
bar(i_con,mu,'LineWidth',lw,'FaceColor',conColz(i_con,:),'EdgeColor','k','FaceAlpha',alphaz);
plot([i_con i_con],[mu-sem mu+sem],'k-','LineWidth',lw);
plot(ones(1,size(dat,1))*i_con,dat,'ko','MarkerSize',ms,'LineWidth',lw);
% Human
i_con= 2;
dat= stats4plot.emo.condition(:,i_con);
mu= nanmean(dat);
sem= nanstd(dat)/sqrt(sum(~isnan(dat)));
bar(i_con,mu,'LineWidth',lw,'FaceColor',conColz(i_con,:),'EdgeColor','k','FaceAlpha',alphaz);
plot([i_con i_con],[mu-sem mu+sem],'k-','LineWidth',lw);
plot(ones(1,size(dat,1))*i_con,dat,'ko','MarkerSize',ms,'LineWidth',lw);
% Tidy up
xlim([0 3]);
ylim([20 100]);
set(gca,'XTick',1:2,'XTickLabel',{'Computer','Human'});
set(gca,'YTick',0:20:100);
set(gca,'FontSize',axisFS,'LineWidth',lw);
ylabel('Emotion [max 100]','FontSize',labelFS);
xlabel('Condition','FontSize',labelFS);
axis square;
% Save
print('-djpeg','-r300',['Figures/Figure-2c']);

%% -----------------------------------------------------------------------
%% ANALYSIS: COLLATE DATA FOR GROUP-LEVEL ANALYSIS

% Initialise variables for collating across datasets
% Decision
lmedatG.dec.subject= [];
lmedatG.dec.dataset= [];
lmedatG.dec.block=   [];
lmedatG.dec.trial=   [];
lmedatG.dec.human=   [];
lmedatG.dec.value=   [];
lmedatG.dec.accept=  [];
lmedatG.dec.rt=      [];
% Decision - value history
lmedatG.hdec.subject= [];
lmedatG.hdec.dataset= [];
lmedatG.hdec.block=   [];
lmedatG.hdec.trial=   [];
lmedatG.hdec.human=   [];
lmedatG.hdec.value=   [];
lmedatG.hdec.valueD=  []; % value difference
lmedatG.hdec.pvalue=  []; % previous value
lmedatG.hdec.accept=  [];
lmedatG.hdec.rt=      [];
% Reaction time
lmedatG.rt.subject=  [];
lmedatG.rt.dataset=  [];
lmedatG.rt.block=    [];
lmedatG.rt.trial=    [];
lmedatG.rt.human=    [];
lmedatG.rt.value=    [];
lmedatG.rt.accept=   [];
lmedatG.rt.rt=       [];
% Emotion
lmedatG.emo.subject= [];
lmedatG.emo.dataset= [];
lmedatG.emo.block=   [];
lmedatG.emo.trial=   [];
lmedatG.emo.human=   [];
lmedatG.emo.value=   [];
lmedatG.emo.accept=  [];
lmedatG.emo.emotion= [];

% Initialise dataset id
i_ds = 0;

% Loop through subjects
for i_sbj= 1:n_sbj

    % Loop through sessions
    for i_ses= 1:2

        % Update dataset idx
        i_ds= i_ds+1;

        % Load data
        load([dirDataB,fs,'MSSM','_Sbj',num2str(i_sbj),'_Ses',num2str(i_ses),'.mat']);

        % Value history
        data.pvalue= [0 data.value(1:end-1)];
        data.valueD= [0 data.value(2:end)-data.value(1:end-1)];

        % RT outlier
        data.outlier= data.rt>14;
        data.poutlier= [0 data.outlier(1:end-1)];

        % Collate
        % Decision
        idx= find(~data.outlier);
        lmedatG.dec.subject= [lmedatG.dec.subject data.subject(idx)];
        lmedatG.dec.dataset= [lmedatG.dec.dataset ones(1,length(idx)).*i_ds];
        lmedatG.dec.block=   [lmedatG.dec.block data.block(idx)];
        lmedatG.dec.trial=   [lmedatG.dec.trial data.trial(idx)];
        lmedatG.dec.human=   [lmedatG.dec.human data.human(idx)];
        lmedatG.dec.value=   [lmedatG.dec.value zscore(data.value(idx))];
        lmedatG.dec.accept=  [lmedatG.dec.accept data.accept(idx)];
        lmedatG.dec.rt=      [lmedatG.dec.rt zscore(data.rt(idx))];
        % Decision - task history
        idx= find(~data.outlier & ~data.poutlier & data.trial>1);
        lmedatG.hdec.subject= [lmedatG.hdec.subject data.subject(idx)];
        lmedatG.hdec.dataset= [lmedatG.hdec.dataset ones(1,length(idx)).*i_ds];
        lmedatG.hdec.block=   [lmedatG.hdec.block data.block(idx)];
        lmedatG.hdec.trial=   [lmedatG.hdec.trial data.trial(idx)];
        lmedatG.hdec.human=   [lmedatG.hdec.human data.human(idx)];
        lmedatG.hdec.value=   [lmedatG.hdec.value zscore(data.value(idx))];
        lmedatG.hdec.valueD=  [lmedatG.hdec.valueD zscore(data.valueD(idx))];
        lmedatG.hdec.pvalue=  [lmedatG.hdec.pvalue zscore(data.pvalue(idx))];
        lmedatG.hdec.accept=  [lmedatG.hdec.accept data.accept(idx)];
        lmedatG.hdec.rt=      [lmedatG.hdec.rt zscore(data.rt(idx))];
        % Reaction time
        idx= find(~data.outlier);
        lmedatG.rt.subject= [lmedatG.rt.subject data.subject(idx)];
        lmedatG.rt.dataset= [lmedatG.rt.dataset ones(1,length(idx)).*i_ds];
        lmedatG.rt.block=   [lmedatG.rt.block data.block(idx)];
        lmedatG.rt.trial=   [lmedatG.rt.trial data.trial(idx)];
        lmedatG.rt.human=   [lmedatG.rt.human data.human(idx)];
        lmedatG.rt.value=   [lmedatG.rt.value zscore(data.value(idx))];
        lmedatG.rt.accept=  [lmedatG.rt.accept data.accept(idx)];
        lmedatG.rt.rt=      [lmedatG.rt.rt zscore(log(data.rt(idx)))];
        % Emotion
        idx= find(~data.outlier & ~isnan(data.emotion));
        lmedatG.emo.subject= [lmedatG.emo.subject data.subject(idx)];
        lmedatG.emo.dataset= [lmedatG.emo.dataset ones(1,length(idx)).*i_ds];
        lmedatG.emo.block=   [lmedatG.emo.block data.block(idx)];
        lmedatG.emo.trial=   [lmedatG.emo.trial data.trial(idx)];
        lmedatG.emo.human=   [lmedatG.emo.human data.human(idx)];
        lmedatG.emo.value=   [lmedatG.emo.value zscore(data.value(idx))];
        lmedatG.emo.accept=  [lmedatG.emo.accept data.accept(idx)];
        lmedatG.emo.emotion= [lmedatG.emo.emotion zscore(data.emotion(idx))];
    
    end

end

%% -----------------------------------------------------------------------
%% ANALYSIS: RUN GROUP-LEVEL ANALYSIS

% LME C-M1 (CHOICE)
% Variables
dataset= lmedatG.dec.dataset';
condition= ((lmedatG.dec.human')*2-1)/2;
value= lmedatG.dec.value';
choice= lmedatG.dec.accept';
% Format
datanames= {'dataset','condition','value','choice'};
datatab= table(categorical(dataset),condition,value,choice,'VariableNames',datanames);
% Fit - with random effects
formulaz    = 'choice ~ 1 + value * condition + (1 + value * condition | dataset)';
lmehat.dec.ran = fitglme(datatab,formulaz,'distribution','binomial','Link','logit','FitMethod','REMPL');
% Fit - without random effects
formulaz    = 'choice ~ 1 + value * condition + (1 | dataset)';
lmehat.dec.noRan = fitglme(datatab,formulaz,'distribution','binomial','Link','logit','FitMethod','REMPL');

% LME C-M2 (CHOICE - VALUE HISTORY)
% Variables
dataset= lmedatG.hdec.dataset';
condition= ((lmedatG.hdec.human')*2-1)/2;
value= lmedatG.hdec.value';
valueD= lmedatG.hdec.valueD';
choice= lmedatG.hdec.accept';
% Format
datanames= {'dataset','condition','value','valueD','choice'};
datatab= table(categorical(dataset),condition,value,valueD,choice,'VariableNames',datanames);
% Fit - with random effects
formulaz    = 'choice ~ 1 + condition * (value + valueD) + (1 + condition * (value + valueD) | dataset)';
lmehat.hdec.ran = fitglme(datatab,formulaz,'distribution','binomial','Link','logit','FitMethod','REMPL');
% Fit - without random effects
formulaz    = 'choice ~ 1 + condition * (value + valueD) + (1 | dataset)';
lmehat.hdec.noRan = fitglme(datatab,formulaz,'distribution','binomial','Link','logit','FitMethod','REMPL');

% LME RT-M1 (REACTION TIME)
% Variables
dataset= lmedatG.rt.dataset';
condition= ((lmedatG.rt.human')*2-1)/2;
value= lmedatG.rt.value';
choice= ((lmedatG.rt.accept')*2-1)/2;
rt= lmedatG.rt.rt';
% Format
datanames= {'dataset','condition','value','choice','rt'};
datatab= table(categorical(dataset),condition,value,choice,rt,'VariableNames',datanames);
% Fit - with random effects
formulaz    = 'rt ~ 1 + choice * value * condition + (1 + choice * value * condition | dataset)';
lmehat.rt.ran = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
% Fit - without random effects
formulaz    = 'rt ~ 1 + choice * value * condition + (1 | dataset)';
lmehat.rt.noRan = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');

% LME E-M1 (EMOTION RATINGS)
% Variables
dataset= lmedatG.emo.dataset';
condition= ((lmedatG.emo.human')*2-1)/2;
value= lmedatG.emo.value';
choice= ((lmedatG.emo.accept')*2-1)/2;
emotion= lmedatG.emo.emotion';
% Format
datanames= {'dataset','condition','value','choice','emotion'};
datatab= table(categorical(dataset),condition,value,choice,emotion,'VariableNames',datanames);
% Fit - with random effects
formulaz    = 'emotion ~ 1 + choice * value * condition + (1 + condition * value * choice | dataset)';
lmehat.emo.ran = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');
% Fit - without random effects
formulaz    = 'emotion ~ 1 + choice * value * condition + (1 | dataset)';
lmehat.emo.noRan = fitglme(datatab,formulaz,'distribution','normal','Link','identity','FitMethod','REMPL');