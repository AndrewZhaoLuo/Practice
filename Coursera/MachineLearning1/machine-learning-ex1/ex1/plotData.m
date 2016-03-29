function plotData(x, y)
%PLOTDATA Plots the data points x and y into a new figure 
%   PLOTDATA(x,y) plots the data points and gives the figure axes labels of
%   population and profit.

% ====================== YOUR CODE HERE ======================
% Instructions: Plot the training data into a figure using the 
%               "figure" and "plot" commands. Set the axes labels using
%               the "xlabel" and "ylabel" commands. Assume the 
%               population and revenue data have been passed in
%               as the x and y arguments of this function.
%
% Hint: You can use the 'rx' option with plot to have the markers
%       appear as red crosses. Furthermore, you can make the
%       markers larger by using plot(..., 'rx', 'MarkerSize', 10);

figure; % open a new figure window, not needed?

data = load('ex1data1.txt');
x = data(:, 1);
y = data(:, 2);
m = length(y); %number of training examples

plot(x, y, 'b+', 'MarkerSize', 10); %format(x, y, format ... , property, value...)
xlabel('Population of City in 10000s');
ylabel('Profit in $10,000s');
title('Restaurant Profitability Based on City Population')

% ============================================================

end
