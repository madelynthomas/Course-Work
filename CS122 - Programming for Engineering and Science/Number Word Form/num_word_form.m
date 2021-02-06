%{
    Num Word Form
%}

function num_word_form() % begin numwordform
    num = input('Enter a # between (0,999): '); % take user input
    if num >= 1 && num <= 19 % check num between 1 and 19
        so = sayones(num); % call sayones
        fprintf('%s \n', so) % print number
    elseif num > 19 && num < 100
        n = floor(num / 10); % return the floor of n
        st = saytens(n); % take n and call saytens
        if mod(num, 10) > 0 % check num mod
            a = sayones(mod(num, 10)); % call sayones
            fprintf('%s %s \n', st, a) % print number
        else % otherwise
            fprintf('%s \n', st) % print number
        end %end if/else
    elseif num >= 100 && num < 1000 % check num between 100 and 1000
        n1 = floor(num / 100); % floor num 
        sh = sayhundreds(n1); % call sayhundreds on num
        if mod(num, 100) >= 20 % mod num and check if greater/equal to 20
            b = saytens(mod(n1, 100)); % mod saytens 
            if mod(num, 10) > 0 % check if mod num is greater than 0
                c = sayones(mod(num, 10)); % call sayones, mod num
                fprintf('%s %s %s \n', sh, b, c) % print number
            else % otherwise
                fprintf('%s %s \n', b, c) % print number
            end % end of if/else
        else % otherwise
            if mod(num, 10) > 0 % mod num
                d = sayones(mod(num, 100)); % call sayones, mod num
                fprintf('%s %s \n', sh, d) % print number
            else % otherwise
                fprintf('%s \n', sh) % print number
            end % end if/else
        end % end if/else
    end %end if/elseif/elseif/else
% end numwordform