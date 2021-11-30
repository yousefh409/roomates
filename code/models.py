class Question:
    def __init__(self, question, answer, weight):
        self.question = question
    
    def setAnswer(self, answer):
        self.answer = answer.trim().tolower()
    
    def setWeight(self, weight):
        if weight is None:
            self.weight = float("inf")
        else:
            self.weight = int(weight.split()[0])