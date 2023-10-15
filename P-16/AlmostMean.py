"""AlmostMean"""


def almost(value):
    """Function"""
    student_id = []
    score = []
    for _ in range(value):
        txt = input().split("\t")
        student_id.append(txt[0])
        score.append(float(txt[1]))
    mean = sum(score) / value
    score.append(mean)
    new_score = sorted(score)
    need = new_score[new_score.index(mean) - 1]
    print(student_id[score.index(need)] + "\t" + str(need))


almost(int(input()))
