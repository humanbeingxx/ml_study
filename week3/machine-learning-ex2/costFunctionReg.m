function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta

for i = 1:m
  J = J + [(-y(i)) * log(sigmoid(X(i,:) * theta)) - (1 - y(i)) * log(1 - sigmoid(X(i,:) * theta))];
end

J = J / m + (lambda * (theta(2:size(theta))' * theta(2:size(theta)))) / (2*m);


for j = 1:size(theta)
  grad(j) = 0;
  for i = 1:m
    grad(j) = grad(j) + (sigmoid(X(i,:) * theta) - y(i)) * X(i, j);
  end
  if j > 1
    grad(j) = grad(j) / m + (lambda * theta(j)) / m;
  else
    grad(j) = grad(j) / m;
  end
end


% =============================================================

end
