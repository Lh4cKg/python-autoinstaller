#!usr/bin/env python3.3

import os
import sys
import subprocess

# text color
R  = '\033[31m' # წითელი
G  = '\033[32m' # მწვანე
O  = '\033[33m' # ფორთოხლის
B  = '\033[34m' # ლურჯი
P  = '\033[35m' # ალისფერი
C  = '\033[36m' #
GR = '\033[37m' # თეთრი
T  = '\033[93m'
# version
v = ' ვერსია: v0.1'
# logo
logo = '''
\033[31m ******************************************************************************\033[m\033[1;36m
*                                                                              *
*                         ______   ___     ____                                *
*                        |  _ \ \ / / |   / ___|                               *
*                        | |_) \ V /| |  | |  _                                *
*                        |  __/ | | | |__| |_| |                               *
*                        |_|    |_| |_____\____|                               *
*       __  __.      .__  .__   __   __  __   __  __   __. __  __.             *
*      |  |/ _|____  |  | |__| |  | |  ||  \ |  ||  | |  |\  \/  /             *
*      |    < \__  \ |  | |  | |  | |  ||   \|  ||  | |  | \ -- /              *
*      |  |  \ / __ \|  |_|  | |  |_|  ||  |\   ||  |_|  | / -- \              *
*      |__|__ (____  /____/__| |____/__/|__| \__/ \_____/ /__/\__\             *
*            \/    \/                                                          *
*                                                                              *
\033[31m ******************************************************************************\033[m                                        
                                                '''
print(logo)
# author
print('\t\t\t\t\t\t\tScript',R+'by'+GR+'..'+G+'L'+B+'h'+T+'4'+P+'c'+C+'K'+O+'g'+G)
print('ოპერაციული სისტემა')
subprocess.call('cat /etc/issue',shell=True)

#*************************************************************************#
#                              script                                     #
#*************************************************************************#

# update system

class ControllPackage:

  def AptUpd(prompt):
    print('[* გსურთ სისტემის განახლება? {Y:კი/N:არა} *]')
    print("")
    while True:   
      option = input(prompt)
      if option in ('y', 'Y', 'yes','YES','კი'):
        print("მიმდინარეობს სისტემის განახლება")
        os.system('xterm -e apt-get update')
        print("სისტემის განახება დასრულებულია")
        return True
      elif option in ('n', 'N', 'no', 'NO','არა'):
        return False
      elif option in ('q','Q','quit','QUIT','გასვლა'):
        print("")
        print("Bye!")
        sys.exit()
        return True
      else:
        os.system("clear")
        print("\033[22;31m გაფრთხილება: ბრძანება არასწორია!\033[22;32m")
        print('[*] გთხოვთ გამოიყენოთ ქვემოთ მოცემული ბრძანებები: ')
        print(' თანხმობა:','y, Y, yes, YES, კი')
        print(' უარყოფა:','n, N, no, NO, არა')
        
  def InstallPackage():
    os.system("clear")
    info = '''
  [ მთავარი მენიუ - MAIN MENU ]
    აირჩიეთ მოდული:
   _________________________
  |  კოდი  | მოდულის სახელი |
  |-------------------------|
     [1]   |  Python-2.7
  |-------------------------|
     [2]   |  Python-3.3.4
  |-------------------------|
     [A]   |  PYLG 
  |-------------------------|
     [H]   |  დახმარება
  |-------------------------|
     [V]   |  ვერსია
  |-------------------------| 
     [Q]   |  გასვლა
  |-------------------------|
           '''
    print(G+info+G)
    while True:
      type = input(R+" მოდული > "+G)
      if type == '1':
        os.system("clear")
        infok2= ''' PYTHON 2.7
              _________________________
             |  კოდი  | მოდულის სახელი |
             |-------------------------|
                [1]   |  Python-2.7
             |-------------------------|
                [2]   |  IDLE
             |-------------------------|
                [3]   |  Pip 
             |-------------------------|
                [4]   |  Setuptools
             |-------------------------|
                [5]   |  Virtualenv
             |-------------------------|
                [6]   |  Sip-4.13
             |-------------------------|
                [7]   |  PyQt-4
             |-------------------------|
                [8]   |  Qt Design
             |-------------------------|
                [M]   | მთავარი მენიუ
             |-------------------------|
              '''
        print(T+infok2+G)
        option = input(R+" შეიყვანეთ კოდი: "+G)
        if option == '1':
          print("არჩეული მოდული: python2.7",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Python 2.7 ინსტალაცია "+G)
            os.system("xterm -e sudo apt-get install python")
            os.system("clear")
            print(GR+" Python 2.7 წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+" შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '2':
          print("არჩეული მოდული: IDLE",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს IDLE ინსტალაცია "+G)
            os.system("xterm -e sudo apt-get install idle")
            os.system("clear")
            print(GR+" IDLE 2 წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '3':
          print("არჩეული მოდული: Pip",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Pip ინსტალაცია "+G)
            os.system("xterm -e curl -O http://python-distribute.org/distribute_setup.py")
            os.system("xterm -e sudo python distribute_setup.py")
            os.system("xterm -e wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py")
            os.system("xterm -e sudo python  get-pip.py")
            os.system("clear")
            print(GR+" Pip წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '4':
          print("არჩეული მოდული: Setuptools",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Setuptools ინსტალაცია "+G)
            os.system("xterm -e sudo pip install -U setuptools")
            os.system("clear")
            print(GR+" Setuptools წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '5':
          print("არჩეული მოდული: Virtualenv",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Virtualenv ინსტალაცია "+G)
            os.system("xterm -e sudo pip install virtualenv")
            os.system("clear")
            print(GR+" Virtualenv წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '6':
          print("არჩეული მოდული: Sip-4.13",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Sip-4.13 ინსტალაცია "+G)
            os.system("xterm -e sudo apt-get install libqt4-dev")
            os.system("xterm -e wget http://sourceforge.net/projects/pyqt/files/sip/sip-4.13.3/sip-4.13.3.tar.gz")
            os.system("xterm -e tar xzvf sip-4.13.3.tar.gz")
            os.system("xterm -e cd sip-4.13.3")
            os.system("xterm -e sudo python configure.py")
            os.system("sudo make")
            os.system("sudo make install")
            os.system("clear")
            print(GR+" Sip-4.13 წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '7':
          print("არჩეული მოდული: PyQt4",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს PyQt4 ინსტალაცია "+G)
            os.system("xterm -e wget sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.9.4/PyQt-x11-gpl-4.9.4.tar.gz")
            os.system("xterm -e tar xzvf PyQt-x11-gpl-4.9.4.tar.gz")
            os.system("xterm -e cd PyQt-x11-gpl-4.9.4")
            os.system("xterm -e sudo python configure.py")
            os.system("xterm -e sudo make")
            os.system("xterm -e sudo make install")
            os.system("clear")
            print(GR+" PyQt4 წარმატებით დაყენდა"+G)
            print(info)
        elif option == '8':
          print("არჩეული მოდული: Qt Design",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Qt Design ინსტალაცია "+G)
            os.system("xterm -e sudo apt-get install python-qt4 qt4-dev-tools python-qt4-dev pyqt4-dev-tools")
            os.system("clear")
            print(GR+" Qt Design წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == 'm' or option == 'M':
            os.system("clear")
            print(info)
        else:
          os.system("clear")
          print(R+" შეცდომა! "+G)
          print(B+" თქვენ უნდა აირჩიოთ ჩამოთვლილი მოდულები"+G)
          print(info)
      elif type == '2':
        os.system("clear")
        infok3 = ''' PYTHON 3.3.4
              _________________________
             |  კოდი  | მოდულის სახელი |
             |-------------------------|
                [1]   |  Python-3.3.4
             |-------------------------|
                [2]   |  IDLE 3
             |-------------------------|
                [3]   |  Pip
             |-------------------------|
                [4]   |  Setuptools
             |-------------------------|
                [5]   |  Virtualenv
             |-------------------------|
                [6]   |  Sip-4.13
             |-------------------------|
                [7]   |  PyQt-4
             |-------------------------|
                [8]   |  Qt Design
             |-------------------------|
                [M]   | მთავარი მენიუ
             |-------------------------|
                      '''
        print(T+infok3+G)
        option = input(R+" შეიყვანეთ კოდი: "+G)
        if option == '1':
          print("არჩეული მოდული: Python-3.3.4",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Python 3.3.4 ინსტალაცია "+G)
            os.system("xterm -e sudo apt-get install python")
            os.system("clear")
            print(GR+" Python 3.3.4 წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+" შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '2':
          print("არჩეული მოდული: IDLE 3",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს IDLE 3 ინსტალაცია "+G)
            os.system("xterm -e sudo apt-get install idle3")
            os.system("clear")
            print(GR+" IDLE 3 წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '3':
          print("არჩეული მოდული: Pip",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Pip ინსტალაცია "+G)
            os.system("xterm -e curl -O http://python-distribute.org/distribute_setup.py")
            os.system("xterm -e sudo python3 distribute_setup.py")
            os.system("xterm -e wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py")
            os.system("xterm -e sudo python3  get-pip.py")
            os.system("clear")
            print(GR+" Pip წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '4':
          print("არჩეული მოდული: Setuptools",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Setuptools ინსტალაცია "+G)
            os.system("xterm -e sudo pip3 install -U setuptools")
            os.system("clear")
            print(GR+" Setuptools წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '5':
          print("არჩეული მოდული: Virtualenv",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Virtualenv ინსტალაცია "+G)
            os.system("xterm -e sudo pip3 install virtualenv")
            os.system("clear")
            print(GR+" Virtualenv წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '6':
          print("არჩეული მოდული: Sip-4.13",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Sip-4.13 ინსტალაცია "+G)
            os.system("xterm -e sudo apt-get install libqt4-dev")
            os.system("xterm -e wget http://sourceforge.net/projects/pyqt/files/sip/sip-4.13.3/sip-4.13.3.tar.gz")
            os.system("xterm -e tar xzvf sip-4.13.3.tar.gz")
            os.system("xterm -e cd sip-4.13.3")
            os.system("xterm -e sudo python3 configure.py")
            os.system("sudo make")
            os.system("sudo make install")
            os.system("clear")
            print(GR+" Sip-4.13 წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == '7':
          print("არჩეული მოდული: PyQt4",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს PyQt4 ინსტალაცია "+G)
            os.system("xterm -e wget sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.9.4/PyQt-x11-gpl-4.9.4.tar.gz")
            os.system("xterm -e tar xzvf PyQt-x11-gpl-4.9.4.tar.gz")
            os.system("xterm -e cd PyQt-x11-gpl-4.9.4")
            os.system("xterm -e sudo python3 configure.py")
            os.system("xterm -e sudo make")
            os.system("xterm -e sudo make install")
            os.system("clear")
            print(GR+" PyQt4 წარმატებით დაყენდა"+G)
            print(info)
        elif option == '8':
          print("არჩეული მოდული: Qt Design",B+"\ti ან install - არჩეული მოდულის დაყენება"+G)
          inm = input(R+" დაყენება : "+G)
          if inm == 'i' or inm == 'install':
            print(P+"მიმდინარეობს Qt Design ინსტალაცია "+G)
            os.system("xterm -e sudo apt-get install python-qt4 qt4-dev-tools python-qt4-dev pyqt4-dev-tools")
            os.system("clear")
            print(GR+" Qt Design წარმატებით დაყენდა"+G)
            print(info)
          else:
            os.system("clear")
            print(R+"შეცდომა!"+G)
            print(B+" თქვენ უნდა გამოიყენოთ შესაბამისი ბრძანება"+G)
            print(info)
        elif option == 'm' or option == 'M':
            os.system("clear")
            print(info)
        else:
          os.system("clear")
          print(R+" შეცდომა! "+G)
          print(B+" თქვენ უნდა აირჩიოთ ჩამოთვლილი მოდულები"+G)
          print(info)
      elif type == 'a' or type == 'A' or type == 'about':
        os.system("clear")
        about = '''
       *---------------------------------------------------------------*
      #          PYLG - Python AutoInstaller Script                     #
       *---------------------------------------------------------------*
    **********************************************************************
    **********************************************************************
    **                         გამოყენება                               **
    **##################################################################**
    **აღწერა: PYLG - არის პითონზე დაწერილი სკრიპტი, რომელიც ავტომატურად **
    **        აყნებს მის რამდენიმე ძირითად ბიბლიოთეკას. მაგ. PVM -ს.    **
    **        აქვს მხოლოდ LINUX მხარდაჭერა. გამოყენება შეიძლბეა         **
    **        Ubuntu/Debian -ის დისტრიბუტივებზე.                        **
    **##################################################################**
    **       გასაშვებად საჭიროა ROOT                                    **
    **    1. python3 pylg.py or sudo chmod +x pylg.py                   **
    **    2. ./pylg.py                                                  **
    **********************************************************************
    **********************************************************************
    ######################################################################
    ## Contact me: lhackg@yandex.com or Lh4cKg@gmail.com                ##
    ######################################################################
                                                        ** autor:lh4ckg **
                                                        ******************'''
        print(about)
        print(O+"\t\t{ M } = { მთავარი მენიუ }"+G)
      elif type == '-h' or type == 'h' or type == 'H' or type == 'help':
        os.system("clear")
        print("")
        print(" ბრძანებები ")
        c_com = '''
          1. { სისტემის განახლება:
             საჭირო ბრძანებები: უარყოფა: n,N,no,NO,არა
                               თანხმობა: y,Y,yes,YES,კი }
          2. { მოდულის არჩევა:
             საჭირო ბრძანებები: 1,2,3,4,5,6,7,8 }
          3. { პროგრამის შესახებ:
             საჭირო ბრძანებები: a,A,about }
          4. { ვერსია:
             საჭირო ბრძანებები: -v,v,version }
          5. { დახმარება:
             საჭირო ბრძანებები: -h,h,H,help }
          6. { გასვლა:
             საჭირო ბრძანებები: q,quit,Q,QUIT }
                '''
        print(c_com)
        print(R+"\t  7. { M : მთავარი მენიუ }"+G)
        print("")
      elif type == '-v' or type == 'v' or type == 'version':
        print(v)
      elif type == 'm' or type == 'M':
        os.system("clear")
        print(info)
      elif type == 'q' or type == 'Q' or type == 'quit' or type == 'QUIT':
        print("")
        print("Bye!")
        sys.exit()
        break
      else:
        print(R+" გაფრთხილება: ბრძანება არასწორია!"+G)

if __name__ == "__main__":
    ControllPackage.AptUpd('[*] ბრძანება \033[22;31m>\033[22;32m ')
    ControllPackage.InstallPackage()
