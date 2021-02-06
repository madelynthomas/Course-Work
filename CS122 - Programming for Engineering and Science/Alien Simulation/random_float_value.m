% Calculate the value using random
function value = random_float_value(min_atk, max_atk)
    value = min_atk + (rand(1) * (max_atk - min_atk)); 
end