import requests


class sendcode:
    def send(phone,captcha):
        host = 'https://dfsns.market.alicloudapi.com'
        path = '/data/send_sms'
        appcode = '046bd45e5b1249848529cf5e4a85453a'
        bodys = {}
        url = host + path

        bodys['content'] = f'''code:{captcha}'''
        bodys['phone_number'] = phone
        bodys['template_id'] = '''TPL_0000'''

        heard = {'Authorization': 'APPCODE ' + appcode}

        try:
            request = requests.post(url, data=bodys, headers=heard)

            response = request.json()

            return response


        except Exception as e:
            print(e)


if __name__ == '__main__':
    pass
