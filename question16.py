def erase_overlap_intervals(intervals):
    if not intervals:
        return 0

    # Sort intervals based on the ending times
    intervals.sort(key=lambda x: x[1])

    count = 0
    prev_end = float('-inf')

    for start, end in intervals:
        if start >= prev_end:
            prev_end = end  # Update the end time
        else:
            count += 1  # Overlapping interval found, remove it

    return count

# Example Usage
intervals = [[1,2], [2,3], [3,4], [1,3]]
print(erase_overlap_intervals(intervals))  # Output: 1
