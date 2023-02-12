
mark = 85
passing_score = 35
distiction = 80

if mark > distiction:
    print("passing score is:{p_score}, you got distiction  with {mark}".format(mark=mark, p_score=passing_score))
    print("passing score is:{}, you got distiction  with {}".format(passing_score,mark))
    print(f"distiction with {mark}")

elif mark>passing_score:
    print("you are passed with {arg_mark}".format(arg_mark=mark))
else:
    print("You failed with {arg_mark}".format(arg_mark=mark))

