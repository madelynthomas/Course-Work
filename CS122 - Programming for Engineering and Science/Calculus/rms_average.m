%{
    Root Mean Square
%}

function rms_avg = rms_average(data)
    x = 0;
    for index = 1:length(data)
        x = (x + data(index)^2);
    end
    rms_avg = sqrt((1/length(data)) * x);
end