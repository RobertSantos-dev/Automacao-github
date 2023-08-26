import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


print(
    f'\nAntes de começar, preciso que você digite o nome de usuario do GITHUB\n'
    f'Você deve digitar APENAS o nome de usuario. EX: Rocketseat, netlify\n'
)

user_name = input('Nome de usuario: ')
print('\n\n')

print('Repositories:\n')


# Navegador com robo
navigator = webdriver.Chrome()

navigator.implicitly_wait(5)
request = navigator.get(f'https://github.com/{user_name}')


element_navigator = navigator.find_elements(By.CLASS_NAME, 'js-responsive-underlinenav-item')
element_navigator[1].click()

sleep(5)
elements_list = navigator.find_elements(By.CSS_SELECTOR, '.public')

repositories = []


for i in elements_list:
    repository_info = { 'name': '', 'desc': '' }
    try:
        name = i.find_element(By.CSS_SELECTOR, '.wb-break-all a').text
        desc = i.find_element(By.CSS_SELECTOR, 'div p')
    except:
        repository_info['desc'] = ''
    else:
        repository_info['desc'] = desc.text
    finally:
        repository_info['name'] = name
        repositories.append(repository_info)


# Printar na tela o resultado final!
for i, repository in enumerate(repositories):
    results = json.dumps(repository, indent=4)
    print(f'{i + 1} - {results} \n')

sleep(3)

navigator.quit()

# Salvar o Resultado em um arquivo