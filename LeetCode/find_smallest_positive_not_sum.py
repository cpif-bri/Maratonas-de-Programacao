def find_smallest_positive_not_sum(arr):
    smallest_sum = 1  # Initialize the smallest positive integer not in the subset
    
    for num in arr:
        # If the current number is less than or equal to the smallest_sum, we can form
        # all the sums in the range [smallest_sum, smallest_sum + num - 1].
        # So, we update smallest_sum to smallest_sum + num.
        if num <= smallest_sum:
            smallest_sum += num
        else:
            break

    return smallest_sum

# Example usage:
arr = [1, 2, 3, 10]
result = find_smallest_positive_not_sum(arr)
print(result)  # Output: 7