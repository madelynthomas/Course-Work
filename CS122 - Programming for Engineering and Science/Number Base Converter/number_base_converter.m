function number_base_converter()
    fprintf('Welcome to the Number Base Converter App! \n \n');
    disp('Use: %num for binary conversion');
    disp('     $num for hexidecimal conversion');
    disp('      num for decimal conversion');
    fprintf('\n');
    while true
        num = input('Enter #: ', 's');
        if num(1) == '%'
            dec = (bin2dec(num(2:end)));
            bin = (num(2:end));
            hex = (dec2hex(bin2dec(num(2:end))));
        elseif num(1) == '$'
            dec = (hex2dec(num(2:end)));
            bin = (dec2bin((hex2dec(num(2:end)))));
            hex = num(2:end);
        elseif num == 'q'
            break;
        else
            dec = (str2double(num));
            bin = (dec2bin(str2double(num)));
            hex = (dec2hex(str2double(num)));
        end
        fprintf('\n');
        fprintf('Decimal: %d \n', dec);
        fprintf('Binary: %s \n', bin);
        fprintf('Hexadecimal: %s \n \n', hex);
        continue;
    end
end