from PyQt5.QtWidgets import*
app=QApplication([])
from main_window import*
from random import choice, shuffle

class Question():
    def __init__(self,question,answer,w_answer1,w_answer2,w_answer3):
        self.question=question
        self.answer=answer
        self.w_answer1=w_answer1
        self.w_answer2=w_answer2
        self.w_answer3=w_answer3
        self.attempts=0
        self.correct=0
    def got_right(self):
        self.attempts+=1
        self.correct+=1
        print("Це правильна відповідь!")

    def got_wrong(self):
        self.attempts+=1
        print("Відповідь невірна")

def new_question(question,radio_list):
    random_question=choice(question)
    text_qwestion.setText(random_question.question)
    right_answer.setText(random_question.answer)
    answer=radio_list[0]
    wrong_answer1,wrong_answer2,wrong_answer3=radio_list[1],radio_list[2],radio_list[3]
    answer.setText(random_question.answer)
    wrong_answer1.setText(random_question.w_answer1)
    wrong_answer2.setText(random_question.w_answer2)
    wrong_answer3.setText(random_question.w_answer3)
    return random_question

def switch_screen():
    global random_question
    if btn_answer.text()=="Відповісти":
        qwestion_group.hide()
        answer_group.show()
        btn_answer.setText("Наступне запитання")
    else:
        qwestion_group.show()
        answer_group.hide()
        btn_answer.setText("Відповісти")
        random_question=new_question(question,radio_list)










q1=Question("яблуко","apple","aple","application","applle")
q2=Question("Машина","car","mashina","lamborgini","caar")
q3=Question("Будинок","house","home","horse","homework")
q4=Question("Ліжко","bed","bad","hores","home")
q5=Question("Гараж","garage","home","son","garden")
q6=Question("Вікно","window","winndow","win","python")
q7=Question("Україна","Ukraine","ukr","Uraine","Ukrayna")
q8=Question("Син","Son","Sun","horse","Ivan")
q9=Question("Кінь","horse","home","hores","hoser")
q10=Question("Слон","elephant","elefant","elf","elefont")
question=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]

radio_list=[rbtn1,rbtn2,rbtn3,rbtn4]
shuffle(radio_list)



main_win=QWidget()
main_win.resize(600,500)
main_win.setWindowTitle("Memory Card")
main_win.move(300,300)

main_win.setLayout(line)
random_question=new_question(question,radio_list)
btn_answer.clicked.connect(switch_screen)


main_win.show()

app.exec()
