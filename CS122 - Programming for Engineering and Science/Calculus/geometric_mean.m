%{
    Geometric Mean
%}

function geo_mean = geometric_mean(data)
    x = 1;
    for index = 1:length(data)
        x = x * data(index);
    end
    geo_mean = nthroot(x, length(data));
end