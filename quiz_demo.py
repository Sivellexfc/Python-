class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer == answer


class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def DisplayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex +1}: {question.text}')

        for q in question.choices:
            print('- '+q)
        answer = str(input('cevap ='))
        self.guess(answer)
        self.loadQuestion()



    def guess(self,answer):
        question = self.getQuestion()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1


    def loadQuestion(self):
        if self.questionIndex == len(self.questions):
            self.ShowScore()
        else:
            self.DisplayQuestion()

    def ShowScore(self):
        print('score: ', self.score)
        

q1 = Question("en iyi programlama dili nedir ?", ["C","JAVA","python","PHP"],"python")
q2 = Question("en kolay programlama dili nedir ?", ["python","C","JAVA","PHP"],"python")
q3 = Question("en popüler programlama dili nedir ?", ["JAVA","C","python","PHP"],"python")
questions = [q1,q2,q3]

quiz = Quiz(questions)
quiz.DisplayQuestion()
