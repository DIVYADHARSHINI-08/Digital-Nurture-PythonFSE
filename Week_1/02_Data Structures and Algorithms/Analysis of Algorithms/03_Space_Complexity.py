def create_list(n):
    numbers = []

    for i in range(n):
        numbers.append(i)

    return numbers


result = create_list(5)

print("Space Complexity: O(n)")
print(result)