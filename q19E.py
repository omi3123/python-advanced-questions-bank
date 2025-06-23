"""
STRING FIGHT
Write a function that accepts a fight string consisting of only small letters and return who wins the fight. When the left side wins, the Left side wins!, when the right side wins, the Right side wins!, in other cases, Let's fight again!.
Left side letters
 w - 4
 p - 3 
 b - 2
 s - 1
 t - 0 (pretty word)
Right side letters:
 m - 4
 q - 3 
 d - 2
 z - 1
 j - 0 (pretty word)
The other letters don't have power and are only victims.
The priest units t and j change the adjacent letters from hostile letters to friendly letters with the same power.
alphabet_war("z") #=>  "z"  => "Right side wins!"
Explanation:
Letter z belongs to the right side letters and the left side has no letter so the right side wins.
alphabet_war("tz")        #=>  "ts" => "Left side wins!"
Explanation:
Letter t is a pretty letter belonging to the left side. Pretty letters convert hostile letters to friendly letters with the same power. Z is a hostile letter with power 1. T will convert it to s a friendly letter with the same power.
"""
def alphabet_war(fight):
    left_power = {'w': 4, 'p': 3, 'b': 2, 's': 1}
    right_power = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

    for i in range(len(fight)):
        if fight[i] in left_power:
            if i > 0 and fight[i - 1] in right_power:
                fight[i - 1] = 's'
            if i < len(fight) - 1 and fight[i + 1] in right_power:
                fight[i + 1] = 's'

    left_score = sum(left_power.get(c, 0) for c in fight)
    right_score = sum(right_power.get(c, 0) for c in fight)

    return 'Left side wins!' if left_score > right_score else 'Right side wins!' if right_score > left_score else "Let's fight again!"
print(alphabet_war("tz"))
