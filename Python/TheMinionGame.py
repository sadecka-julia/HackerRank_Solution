# The Minion Game, Python, Medium, https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true


def minion_game(string):
    first_letter = 0
    kevin_score = 0   # consonans
    stuart_score = 0  # vowels (aeiou)

    # For every letter in word, we check if this letter is vowels, 
    # if so - Stuart gets points, else points are going to Kevin. 
    for first_letter in range(len(string)):
        if (string[first_letter] in 'aAeEoOuUiI'):
            kevin_score += len(string)-first_letter
        else:
            stuart_score += len(string)-first_letter
        first_letter += 1


    # We check who get more points.
    if(stuart_score > kevin_score):
        print("Stuart", stuart_score)
    elif(stuart_score < kevin_score):
        print("Kevin", kevin_score)
    else:
        print("Draw")

        

if __name__ == '__main__':
    s = input()
    minion_game(s)