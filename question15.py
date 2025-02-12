def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    # Step 2: Merge overlapping intervals
    for i in range(1, len(intervals)):
        prev = merged[-1]
        curr = intervals[i]

        if curr[0] <= prev[1]:  # Overlapping intervals
            prev[1] = max(prev[1], curr[1])  # Merge intervals
        else:
            merged.append(curr)  # No overlap, add to result

    return merged

# Example Usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]
