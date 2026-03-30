def solution(people, limit):
    people.sort()
    boat = 0
    left = 0
    right = len(people) - 1
    
    while(left <= right):
        if people[left] + people[right] <= limit:
            boat += 1
            left += 1
            right -= 1
        else:
            boat += 1
            right -= 1
    
    return boat
