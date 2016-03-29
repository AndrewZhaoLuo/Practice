function plotData(X, y)
%PLOTDATA Plots the data points X and y into a new figure 
%   PLOTDATA(x,y) plots the data points with + for the positive examples
%   and o for the negative examples. X is assumed to be a Mx2 matrix.

% Create New Figure
figure; hold on;

% ====================== YOUR CODE HERE ======================
% Instructions: Plot the positive and negative examples on a
%               2D plot, using the option 'k+' for the positive
%               examples and 'ko' for the negative examples.
%

pos_rows = find(y == 1);
neg_rows = find(y == 0);

%plotting people who got in
plot(X(pos_rows,1), X(pos_rows, 2), "k+");

%plotting those who did not
plot(X(neg_rows,1), X(neg_rows, 2), "ko", "MarkerFaceColor", "r");

% =========================================================================



hold off;

end
