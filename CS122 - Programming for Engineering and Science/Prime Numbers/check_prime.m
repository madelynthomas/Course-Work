%{
    Check Prime
%}

% Take user input and store it as num
num = input('Enter #: ');

% Takes num and calculates the square root
prime = all(mod(num,[2 3:2:sqrt(num)]));

%{
If the user inputs 1 it will immediately
return that 1 is not a prime number 
%}
if (num == 1)
    fprintf('%g is not prime \n', num)

%{
Otherwise prime will execute and if 1
is returned from the equation then num
is a prime number
%}
elseif (prime == 1)
    fprintf('%g is prime \n', num)

%{
If num is neither prime or num are not
equal to 0, the num is not a prime number
%}
else
    fprintf('%g is not prime \n', num)

%
end
% End of the CheckPrime.m script