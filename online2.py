import vk
import time

session = vk.Session(access_token='YOUR_TOKEN')
api = vk.API(session)
print('Успешный вход!!')
while True:
 api.account.setOnline()
 time.sleep(300)