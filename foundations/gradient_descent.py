class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places

        #Initialize
        minimizer = init

        # loop through previous iterations 
        for _ in range(iterations):
            # calculate the derivative. 
            delta = 2 * minimizer
            # Update The minimizer
            minimizer = minimizer - learning_rate * delta
        
        return round(minimizer,5)

        #pass
