function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
num_params = length(theta)
J_history = zeros(num_iters, 1);

for iter = 1:num_iters

    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %

    %create a row vector to .+ to each theta
    outside_term = alpha / m;
    
    %represents the sum of the inner sigma
    %row represents the ith training example in X * theta - y
    %which is the term h(x) - y
    %multiply this by the appropriate xj^i which is a matrix i x j
    %do this through evil vector math
    inner_sigma = ((X * theta - y)' * X )';
    
    %put it all together and win!
    change_vector = outside_term * inner_sigma;
    
    theta .-= change_vector;
    
    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);

end

end
