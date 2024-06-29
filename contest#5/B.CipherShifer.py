#sheshbazzar
test_cases = int(input())
for x in range(test_cases):
    length = int(input())
    input_string = input().strip()

    repeated_chars = ""

    left = 0
    right = left + 1
    while right < length:
        if input_string[left] == input_string[right]:
            repeated_chars += input_string[left]
            left = right + 1
            right = left + 1
        else:
            right += 1

    print(repeated_chars)


