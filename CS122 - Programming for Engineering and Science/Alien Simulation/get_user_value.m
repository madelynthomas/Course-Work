% Getting the user input and throwing an exception if not between min/max
function output = get_user_value(prompt, min_sim, max_sim)
    output = input(prompt);
    while (output < min_sim) || (output > max_sim)
        fprintf('Error: Integer must be betwen minimum and maximum. Try again. \n')
        output = input(prompt);
    end
end