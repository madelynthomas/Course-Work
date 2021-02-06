%{
    Dice Roll
%}

% Initialize the attack rolls
atk_roll_1 = 0; 
atk_roll_2 = 0;
atk_roll_3 = 0;

% Initialize the defense rolls
def_roll_1 = 0;
def_roll_2 = 0;

% Initalize win and tie counters
atk_win = 0;
def_win = 0;
tie = 0;

% Use nested for loops to consider every possibility
for atk_roll_1 = [1:6]
    for atk_roll_2 = [1:6]
        for atk_roll_3 = [1:6]
            for def_roll_1 = [1:6]
                for def_roll_2 = [1:6]
                    % Sort atack and defense rolls
                    atk_rolls = sort([atk_roll_1,atk_roll_2,atk_roll_3])
                    def_rolls = sort([def_roll_1,def_roll_2])
                    % Take the two highest rolls from both sides
                    atk1 = atk_rolls(3)
                    atk2 = atk_rolls(2)
                    def1 = def_rolls(2)
                    def2 = def_rolls(1)
                    % Increment atk_win, def_win, and tie counters
                    if atk1 > def1 && atk2 > def2
                        atk_win = atk_win + 1;
                    elseif def1 >= atk1 && def2 >= atk2
                        def_win = def_win + 1;
                    elseif (atk1 > def1 && atk2 <= def2)
                        tie = tie + 1;
                    elseif (atk1 <= def1 && atk2 > def2)
                        tie = tie+1;
                    end
               end
            end
        end
    end
end

% Determine probability of atk_win, def_win, and tie
probability1= (atk_win/6^5);
probability2= (def_win/6^5);
probability3= (tie/6^5);

% Display pie chart
pie([probability1, probability2, probability3])