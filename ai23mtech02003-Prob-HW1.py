# Define a function to check if a number is prime
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Define the number of sides on each die
num_sides = 6
# Calculate the total number of possible outcomes
num_outcomes = num_sides ** 2
prime_outcomes = -1
sum_one = 0
# Calculate the number of outcomes where the sum is the target
num_target_outcomes = 0
for die1 in range(1, num_sides + 1):
    for die2 in range(1, num_sides + 1):
        if die1 + die2 == 7:
            num_target_outcomes += 1
        if prime(die1 + die2):
            prime_outcomes += 1
        if die1+die2 == 1:
            sum_one += 1
# Calculate the probability of getting the target sum
prob_target_sum_A = num_target_outcomes / num_outcomes
prob_target_sum_B = prime_outcomes / num_outcomes
prob_target_sum_C = sum_one / num_outcomes
# Print the result
print(f"The probability of getting a sum of 7 is {prob_target_sum_A:.4f}")
print(f"The probability of getting a prime no. is {prob_target_sum_B:.4f}")
print(f"The probability of getting a sum of 1 is {prob_target_sum_C:.4f}")

