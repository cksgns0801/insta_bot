import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from instabot import Bot

bot=Bot()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(360, 360))    #타이틀 이름
        self.setWindowTitle("instabot")

        self.nameLabel_1 = QLabel(self)         #id 글자 표시
        self.nameLabel_1.setText('ID:')

        self.nameLabel_2 = QLabel(self)         #pw 글자표시
        self.nameLabel_2.setText('PW:')

        self.nameLabel_3 = QLabel(self)         #tag 글자 표시
        self.nameLabel_3.setText('tag:')

        self.nameLabel_4 = QLabel(self)         #log 글자 표시
        self.nameLabel_4.setText('log:')


        self.line_1 = QLineEdit(self)       #id 입력창
        self.line_2 = QLineEdit(self)       #pw 입력창
        self.line_3 = QLineEdit(self)       #tag 입력창
        self.line_4 = QLineEdit(self)       #log 출력창

        #각 입력창 죄표및 크기 지정
        self.line_1.move(80, 20)
        self.line_1.resize(200, 32)

        self.line_2.move(80, 60)
        self.line_2.resize(200, 32)

        self.line_3.move(80, 160)
        self.line_3.resize(200, 32)

        self.line_4.move(80, 320)
        self.line_4.resize(200, 32)

        self.nameLabel_1.move(20, 20)
        self.nameLabel_2.move(20, 60)
        self.nameLabel_3.move(20, 160)
        self.nameLabel_4.move(20, 320)

        login = QPushButton('LOGIN', self)              #로그인버튼
        login.clicked.connect(self.clickMethod_login)
        login.resize(200, 32)
        login.move(80, 100)

        follow = QPushButton('follow', self)            #팔로우버튼
        follow.clicked.connect(self.clickMethod_follow)
        follow.resize(100, 100)
        follow.move(20, 200)

        unfollow = QPushButton('unfollow', self)        #언팔로우버튼
        unfollow.clicked.connect(self.clickMethod_unfollow)
        unfollow.resize(100, 100)
        unfollow.move(120, 200)

        like = QPushButton('like', self)                #좋아요 버튼
        like.clicked.connect(self.clickMethod_like)
        like.resize(100, 100)
        like.move(220, 200)

    def clickMethod_login(self):  #로그인 함수
        ID = self.line_1.text() #아이디 저장
        PW = self.line_2.text() #패스워드 저장
        bot.login(username=ID, password=PW) #로그인 기능
        self.line_4.setText('login success')

    def clickMethod_follow(self):       #팔로우 매크로 함수
        tag=self.line_3.text()
        follow_tag = bot.get_hashtag_users(tag) #해쉬태그를 사용한 유저 검색
        friends = []
        for i in range(0, len(follow_tag)):
            aa = bot.get_username_from_user_id(follow_tag[i])   #유저ID->닉네임 변환
            friends.append(aa)      #리스트 추가

        bot.follow(follow_tag)  #유저id를 이용한 팔로우 기능
        self.line_4.setText('follow success')  # 로그 출력
    def clickMethod_unfollow(self):     #언팔로우 매크로 함수
        bot.unfollow_non_followers()    #상대가 나랑 팔로우가 아닐경우 언팔로우
        self.line_4.setText('unfollow success')#로그 출력

    def clickMethod_like(self):        #좋아요 매크로 함수
        tag=self.line_3.text()          #태그 입력받아옴
        like_tag=bot.get_hashtag_medias(tag) #태그가 포함된 미디어를 받아옴
        bot.like_medias(like_tag)       #미디어 리스트를 이용하여 좋아요
        self.line_4.setText('like success')#로그 출력

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

