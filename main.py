from PyQt5.QtWidgets import* 
from PyQt5.QtCore import* 
app=QApplication([]) 
from main_window import* 
from menu_window import*
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
        attempts+=1 
        correct+=1 
        #print("Це правильна відповідь!") 
 
    def got_wrong(self): 
        global attempts 
        attempts+=1 
        #print("Відповідь невірна") 
 
def new_question(question):
    global answer, wrong_answer1,wrong_answer2,wrong_answer3 
    radio_list=[rbtn1,rbtn2,rbtn3,rbtn4] 
    shuffle(radio_list) 
    answer=radio_list[0] 
    wrong_answer1,wrong_answer2,wrong_answer3=radio_list[1],radio_list[2],radio_list[3] 
    random_question=choice(question) 
    text_qwestion.setText(random_question.question) 
    right_answer.setText(random_question.answer) 
     
    answer.setText(random_question.answer) 
    wrong_answer1.setText(random_question.w_answer1) 
    wrong_answer2.setText(random_question.w_answer2) 
    wrong_answer3.setText(random_question.w_answer3) 
    return random_question 
 
def clear_buttons():
    radio_group.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    radio_group.setExclusive(True)

def check_result(): 
    #global answer, wrong_answer1,wrong_answer2, wrong_answer3 
    print(answer.isChecked()) 
    if answer.isChecked(): 
        text_result.setText("Відповідь вірна!") 
        random_question.got_right() 
    else: 
        text_result.setText("Відповідь невірна!") 
        random_question.got_wrong() 
 
 
def switch_screen(): 
    #global random_question 
    if btn_answer.text()=="Відповісти": 
        qwestion_group.hide() 
        answer_group.show() 
        check_result() 
        btn_answer.setText("Наступне запитання") 
    else: 
        clear_buttons()
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
 
def menu_stat():
    global attempts,correct,p
    try:
        p=correct/attempts*100
        p=round(p,2)
    except:
        p=0
    main_win.hide()
    menu_win.show()
    stat_info.setText(f"Разів відповіли: {attempts} \n Вірних відповідей: {correct} \n Успішність: {p}%")
    
def back_to_main():
    main_win.show()
    menu_win.hide()
 
def clear_lines():
    q_red.clear()
    a_red.clear()
    w1_red.clear()
    w2_red.clear()
    w3_red.clear()

def add_question():
    global question
    question.append(Question(q_red.text(),a_red.text(),w1_red.text(),w2_red.text(),w3_red.text()))
    clear_lines()


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

attempts=0
correct=0
p=0

question=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10] 
 

 
 
main_win=QWidget() 
main_win.resize(600,500) 
main_win.setWindowTitle("Memory Card") 
main_win.move(300,300) 
 
 
menu_win=QWidget() 
menu_win.setLayout(line_menu) 
main_win.setLayout(line) 
T=QTimer() 
 
random_question=new_question(question) 
btn_answer.clicked.connect(switch_screen) 
btn_sleep.clicked.connect(rest) 
btn_menu.clicked.connect(menu_stat)
btn_back.clicked.connect(back_to_main)
btn_clear.clicked.connect(clear_lines)
btn_add.clicked.connect(add_question)
T.timeout.connect(wake_up) 
 
main_win.show() 
 
app.exec()
