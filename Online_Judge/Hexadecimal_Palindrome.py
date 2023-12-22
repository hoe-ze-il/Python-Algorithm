def is_hex_palindrome(num):
    hex_num = hex(num)[2:]  
    return hex_num == hex_num[::-1] 

def solve(numbers):
    count = 0
    for num in numbers:
        if is_hex_palindrome(num):
            count += 1
    return count

N = int(input())
numbers = list(map(int, input().split()))
print(solve(numbers))
print()
