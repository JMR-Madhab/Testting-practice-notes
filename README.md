# Cloning & Pushing-practice
The main objective of creating this repo is to practice cloning repos, taking them into my local system, making changes using VScode and then pushing it back to repo finally commiting changes. This will help me understand how does all these process takes place in the industry level (though I am well aware of the fact that in this whole process everyone has their own different role and task, following the protocols).

1. Performed my 1st change
2. Performed my 2nd change in primeno.py file
3. Performed my 3rd change in readme file by describing the core idea & logic of the latest code to check if prime or not.
    - Previous code was basic trial division based i.e., Check divisibility from 2 up to num-1.
        -- Major drawback was inefficient for large numbers.
    - Current code uses square root of n.
        -- The Core Idea:
If a number n is not prime, it can be expressed as:
n=a*b
- If both a and b were greater than sqrt{n}, then their product would be greater than n.
- Similarly, if both were smaller than sqrt{n}, their product would be less than n.
- Therefore, at least one factor must be less than or equal to sqrt{n}.
This means:
To check if n is prime, you only need to test divisibility up to sqrt{n}. If no divisor is found in that range, n must be prime.

Step-by-Step Logic
- Handle small cases
- Numbers ≤ 1 are not prime.
- 2 and 3 are prime.
- Loop from 2 to √n
- For each number i in this range, check if n % i==0.
- If divisible, n is not prime.
- If no divisor is found, n is prime.

Example: Check if 29 is prime
- √29 ≈ 5.38 → check divisibility up to 5.
- Test divisors: 2, 3, 4, 5.
- None divide 29 evenly → ✅ 29 is prime.