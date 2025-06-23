"""
Calculate total score
Our football team has finished the championship. Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format x:y, where x is our team and y is our opponents score. The rules to calculate score is: 
1. If x > y: 3 points
2. If x < y: 0 point
3. If x = y: 1 point
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.
"""
def totalPoints(matches):
    total_points=0
    for results in matches:
        x,y=results.split(":")
        x=int(x)
        y=int(y)
        if x > y :
            total_points+=3
        elif x == y:
            total_points+=1
    return total_points
matches = ["1:2", "2:1", "2:2"]
total_points = totalPoints(matches)
print(total_points)