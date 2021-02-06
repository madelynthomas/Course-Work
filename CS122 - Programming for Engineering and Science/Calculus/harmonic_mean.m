%{
    Harmonic Mean
%}

function hm = harmonic_mean(data)
    x = 0;
    for index = 1:length(data)
        x = x + (1 / data(index));
    end
    hm = (length(data) / x);
end