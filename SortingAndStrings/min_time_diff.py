# Given a list of 24-hour clock time points in "HH:MM" format, 
# return the minimum minutes difference between any two time-points in the list.

def findMinDifference(timePoints):
    if len(timePoints) > 1440:
        return 0
    
    # convert to minutes
    minutes = [] 
    for t in timePoints:
        h, m = map(int, t.split(':'))
        minutes.append(h * 60 + m)

    # O(nlogn)
    minutes.sort()

    # 4. Initialize min_diff with the wrap-around case
    # Example: "23:59" (1439) and "00:00" (0) -> (1440 + 0) - 1439 = 1
    min_diff = (1440 - minutes[0]) - minutes[-1]

    for i in range(1, len(minutes)):
        diff = minutes[i] - minutes[i-1]
        if diff < min_diff:
            min_diff = diff
        if min_diff == 0:
            return 0
        
    return min_diff