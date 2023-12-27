function ste = ste(dat)
% function ste = ste(dat)

for i= 1:size(dat,2)
    ste(i) = nanstd(dat(:,i))/ sqrt(sum(~isnan(dat(:,i))));
end

return