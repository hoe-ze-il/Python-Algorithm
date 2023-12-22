def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

def count_palindromes(input_str):
    count = 0
    n = len(input_str)
    
    for i in range(n):
        for j in range(i, n + 1):
            substring = input_str[i:j]
            if is_palindrome(substring):
                count += 1

    return count

input_str = input()
result = count_palindromes(input_str)
print(result)
f