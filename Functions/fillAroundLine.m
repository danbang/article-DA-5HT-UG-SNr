function hh = fillAroundLine(dat,err,colz)
% h = fillAroundLine(dat,err,color)

hh = [];

xn = 1:length(err);

for i = 1:length(err)-1
    hold on;
    yplus1 = dat(i)+err(i);
    yplus2 = dat(i+1)+err(i+1);
    yminus1 = dat(i)-err(i);
    yminus2 = dat(i+1)-err(i+1);
    hh(end+1) = fill([xn(i) xn(i) xn(i+1) xn(i+1)],[yminus1 yplus1 yplus2 yminus2],colz,'Edgecolor','none','FaceAlpha',.3);
end

return

