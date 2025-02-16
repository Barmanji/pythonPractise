string = "This is a protypical88 stri9ng"
str= ""
for i in string:
    if i in '0123456789':
        continue
    else:
        str+=i

print(str)

def print_double_d():
    print("  *****       *****  ")
    print(" *     *     *     * ")
    print("*       *   *       *")
    print("*   *   *   *   *   *")
    print("*       *   *       *")
    print(" *     *     *     * ")
    print("  *****       *****  ")

print_double_d()

