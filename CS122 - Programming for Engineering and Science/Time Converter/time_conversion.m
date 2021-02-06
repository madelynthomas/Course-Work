%{
    Time Conversion
%}

input_time = input('Enter the Eastern Standard Military time as ####: ')
conversion = (input_time/100);
hour = floor(conversion);
minute = mod(input_time, 100);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if (hour == 0)
    nyc = 12;
elseif (hour > 12)
    nyc = hour - 12;
else
    nyc = hour;
end

if (hour < 12)
    meridian = 'am';
else
    meridian = 'pm';
end

fprintf('New York City: %d:%02d%s \n', nyc, minute, meridian)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if (hour < 4)
     flg = hour + 9;
elseif (hour >= 4 && hour <= 15)
    flg = hour - 3;
elseif (hour > 15)
    flg = hour - 15;
end

if (hour > 2 && hour < 15)
    meridian = 'am';
elseif (hour <= 2)
    meridian = 'pm (-)';
elseif (hour >= 15)
    meridian = 'pm';
end

fprintf('Flagstaff: %d:%02d%s \n', abs(flg), minute, meridian)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if (hour < 8)
     lon = hour + 5;
elseif (hour >= 8 && hour <= 19)
    lon = hour - 7;
elseif (hour > 19)
    lon = hour - 19;
end

if (hour < 6)
    meridian = 'am';
elseif (hour > 19)
    meridian = 'am (+)';
elseif (hour > 6 && hour < 19)
    meridian 'pm';
end

fprintf('London: %d:%02d%s \n', lon, minute, meridian)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

if (hour < 12)
     tyo = hour + 1;
elseif (hour >= 12)
    tyo = tyo - 11;
end

if (hour > 10 && hour < 23)
    meridian = 'am (+)';
elseif (hour <= 10)
    meridian = 'pm';
elseif (hour >= 23)
    meridian = 'pm (+)'
end

fprintf('Tokyo: %d:%02d%s \n', tyo, minute, meridian)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%