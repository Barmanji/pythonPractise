
def removenth(s, n):
    if n < 0 or n >= len(s):
        return s
    return s[:n] + s[n+1:]

# Examples
print(removenth("MANGO", 1))
print(removenth("MANGO", 3))
print(removenth("MANGO", 5))
