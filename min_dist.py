def min_distance(arr):
    indices = {}
    min_dist = float('inf')

    for i, val in enumerate(arr):
        if val in indices:
            min_dist = min(min_dist, i - indices[val])
        indices[val] = i

    return min_dist if min_dist != float('inf') else -1

user_input = input("Enter the elements of the array separated by spaces: ")
arr = list(map(int, user_input.split()))

result = min_distance(arr)
print("Minimum distance:", result)
