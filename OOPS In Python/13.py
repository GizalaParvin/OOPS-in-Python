#continue of ques 12 of using filter 
marks =[ 77,97,56,87,95]

def failing(score):
    return score < 60
result =filter(failing,marks)
print("Failing Scores:",list(result))
