from PyQt5.QtWidgets import* 
from PyQt5.QtCore import* 
app=QApplication([]) 
from main_window import* 
from random import choice, shuffle 
from time import sleep 
 
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
        global correct,attempts 
        self.attempts+=1 
        self.correct+=1 
        #print("Це правильна відповідь!") 
 
    def got_wrong(self): 
        global attempts 
        self.attempts+=1 
        #print("Відповідь невірна") 
 
def new_question(question): 
    random_question=choice(question) 
    text_qwestion.setText(random_question.question) 
    right_answer.setText(random_question.answer) 
     
    answer.setText(random_question.answer) 
    wrong_answer1.setText(random_question.w_answer1) 
    wrong_answer2.setText(random_question.w_answer2) 
    wrong_answer3.setText(random_question.w_answer3) 
    return random_question 
 
def check_result(): 
    global answer, wrong_answer1,wrong_answer2, wrong_answer3 
    print(answer.isChecked()) 
    if answer.isChecked(): 
        text_result.setText("Відповідь вірна!") 
        random_question.got_right() 
    else: 
        text_result.setText("Відповідь невірна!") 
        random_question.got_wrong() 
 
 
def switch_screen(): 
    global random_question 
    if btn_answer.text()=="Відповісти": 
        qwestion_group.hide() 
        answer_group.show() 
        check_result() 
        btn_answer.setText("Наступне запитання") 
 
    else: 
        random_question=new_question(question) 
        qwestion_group.show() 
        answer_group.hide() 
        btn_answer.setText("Відповісти") 
         
def rest(): 
    main_win.hide() 
    t=timer.value()*1000*60 
    T.setInterval(t) 
    T.start() 
 
def wake_up(): 
    T.stop() 
    main_win.show() 
 
 
 
 
 
 
 
 
 
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
answer=radio_list[0] 
wrong_answer1,wrong_answer2,wrong_answer3=radio_list[1],radio_list[2],radio_list[3] 
 
 
main_win=QWidget() 
main_win.resize(600,500) 
main_win.setWindowTitle("Memory Card") 
main_win.move(300,300) 
 
main_win.setLayout(line) 
T=QTimer() 
 
random_question=new_question(question) 
btn_answer.clicked.connect(switch_screen) 
btn_sleep.clicked.connect(rest) 
T.timeout.connect(wake_up) 
 
main_win.show() 
 
app.exec()
