function h = shadedLineMeanSte(dat,linewid,linez,colz)
% function h = shadedLineMeanSte(dat,linewid,linez,colz)

m=nanmean(dat);
    
hold on; 
plot(m,'color',colz,'LineWidth',linewid,'linestyle',linez);
fillAroundLine(m,ste(dat),colz);
        
return