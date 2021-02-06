%{
    Say Tens
%}

function output = say_tens(num) % display the number inputed in tens place
    if num == 2
        output = 'twenty';
    elseif num == 3
        output = 'thirty';
    elseif num == 4
        output ='forty';
    elseif num == 5
        output = 'fifty';
    elseif num == 6
        output = 'sixty';
    elseif num == 7
        output = 'seventy';
    elseif num == 8
        output = 'eighty';
    elseif num == 9
        output = 'ninety';
    end
% end say_tens