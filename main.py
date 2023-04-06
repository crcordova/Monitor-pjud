import requests
import time
from sessionIdGeter import sessionid_get


def main(url='https://oficinajudicialvirtual.pjud.cl/programacionSalasN.php', wait=10):
    while True:  

        cookies = {
            'PHPSESSID': sessionid_get(),
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0',
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Language': 'es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'https://oficinajudicialvirtual.pjud.cl/indexN.php',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
        }

        response_sala = requests.get('https://oficinajudicialvirtual.pjud.cl/programacionSalasN.php', cookies=cookies, headers=headers)
        response_unif = requests.get('https://oficinajudicialvirtual.pjud.cl/consultaUnificada.php', cookies=cookies, headers=headers)

        if response_sala.status_code==200:
            print("Estado PJUD Programacion Salas OK")

        elif response_sala.status_code>= 400:
            print("PJUD Programacion Salas NO Responde")

        if response_unif.status_code==200:
            print("Estado PJUD Consulta OK")

        elif response_unif.status_code>= 400:
            print("PJUD Consulta NO Responde")

        print("********************")
        time.sleep(wait) 
if __name__ == '__main__':
    main()