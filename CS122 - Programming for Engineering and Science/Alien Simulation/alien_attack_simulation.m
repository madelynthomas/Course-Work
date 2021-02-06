%{
    Alien Attack Simulation
%}

fprintf('Welcome to the Alien Attack Simulation! \n \n');

% Set min/max simulation values
min_sim = 25;
max_sim = 5000;
prompt = ('Please enter the desired number of simulations (must be between 25 and 5000): ');

num_sim = get_user_value(prompt, min_sim, max_sim);

% Set min/max attack values
aRate = input('Please enter desired average rate of alien attacks: ');
min_atk = 5;
max_atk = 95;
prompt = ('Please enter the percent variance (between 5 and 95): ');

% Percent variance of the user values
percent_var = get_user_value(prompt, min_atk, max_atk);
minimum = aRate - percent_var;
maximum = aRate + percent_var;
x = random_float_value(min_atk, max_atk);

% Check the file name input by user includes .txt
file_name = input('Please enter the filname of the output file ending with .txt: ', 's');
while strcmp('.txt',file_name(end-3:end))==0
    file_name = input ('Re-enter text file, remember to use  .txt at the end: ', 's');
end

% Open the file and write the values to it as an array
fh = fopen(file_name, 'w');
v = [];
for i = 1:num_sim
    v(i) = random_float_value(min_atk, max_atk);
    fprintf(fh, '%f\n', v(i));
end

% Find the statistical values using built-ins
mean_set = mean(v);
max_set = max(v);
min_set = min(v);
std_set = std(v);

% Print outputs to the screen
fprintf('\n Simulation Values Sucessfully written: %g; see %s for results \n', num_sim, file_name);
fprintf('Analysis of Simulation Data: \n');
fprintf('Mean of data set: %g \n', mean_set);
fprintf('Max of data set: %g \n', max_set);
fprintf('Min of data set: %g \n', min_set);
fprintf('Standard Deviation of data set: %g \n', std_set);
fprintf('See plot for graph! \n')

% Plot the data
plot(v);
fclose(fh);