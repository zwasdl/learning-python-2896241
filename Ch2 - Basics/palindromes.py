def is_palindrome(lst: list) -> bool:
    if lst == lst[::-1]:
        return True
    return False


s = ""
while s.lower() != 'exit':
    s = input("Enter string to test for palindrome or exit: ").lower()
    s_lst = []
    for c in s:
        if c.isalnum():
            s_lst.append(c)
    print("Palindrome test: ", is_palindrome(s_lst))
