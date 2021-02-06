%{
    Say Hundreds
%}

function output = say_hundreds(num) % displays hundred for numbers >= 100
    h = sayones(num);
    output = strcat(h,' hundred');
% end say_hundreds