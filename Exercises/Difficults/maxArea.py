# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section)
# the container can contain is 49.


# The problem is to find the maximum amount of water that can be stored in a
# container formed by two vertical lines drawn on a plane. The input is an
# array of integers representing the heights of the vertical lines.
# The output should be the maximum amount of water that can be stored in the container.
# The container must be formed by two vertical lines and the x-axis, and it cannot be slanted.


# Define a function named maxArea that takes a list of integers as input and returns an integer.
def maxArea(heights: list[int]) -> int:
    # Initialize a variable named max_area to 0.
    max_area = 0
    # Loop through the indices of the input list using the range function.
    for i in range(len(heights)):
        # Loop through the indices of the input list starting from i+1 using the range function.
        for j in range(i + 1, len(heights)):
            # Calculate the area of the container formed by the two vertical lines at indices i and j.
            # The area is the minimum of the heights of the two lines multiplied by the distance between them.
            area = min(heights[i], heights[j]) * (j - i)
            # Update the max_area variable if the current area is greater than the previous max_area.
            max_area = max(max_area, area)
    # Return the maximum area that was found.
    return max_area


# The maxArea function takes a list of integers as input and returns an integer.
# It calculates the maximum amount of water that can be stored in a container formed by
# two vertical lines drawn on a plane. The input is an array of integers representing the
# heights of the vertical lines. The output should be the maximum amount of water that can
# be stored in the container. The container must be formed by two vertical lines and the
# x-axis, and it cannot be slanted.

# To calculate the maximum amount of water, the function loops through the indices of the
# input list using the range function. For each index, it loops through the indices of the
# input list starting from the next index using the range function. It calculates the area of
# the container formed by the two vertical lines at the current indices. The area is the
# minimum of the heights of the two lines multiplied by the distance between them. It updates
# the maximum area variable if the current area is greater than the previous maximum area.
# Finally, it returns the maximum area that was found.


# Call the maxArea function with the input list [1, 8, 6, 2, 5, 4, 8, 3, 7] and print the result.
# print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([6, 3, 7]))
