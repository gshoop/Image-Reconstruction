def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_two_highest_common_factors(number):
    factors = []
    
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    
    if len(factors) < 2:
        return None  # Not enough factors to find two highest common factors
    
    factors.sort(reverse=True)
    highest_common_factor = factors[0]
    
    # Find the second highest common factor
    for factor in factors[1:]:
        if gcd(highest_common_factor, factor) == factor:
            second_highest_common_factor = factor
            break
    
    return highest_common_factor, second_highest_common_factor

# Example usage
number = int(input("Enter a number: "))
result = find_two_highest_common_factors(number)

if result:
    highest_factor, second_highest_factor = result
    print(f"The two highest common factors of {number} are {highest_factor} and {second_highest_factor}.")
else:
    print(f"There are not enough factors to find two highest common factors for {number}.")
