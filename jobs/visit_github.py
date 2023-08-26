from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from save_file import SaveFile


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
    repository_info = { 'nome': '', 'descricao': '' }
    try:
        name = i.find_element(By.CSS_SELECTOR, '.wb-break-all a').text
        desc = i.find_element(By.CSS_SELECTOR, 'div p')
    except:
        repository_info['descricao'] = ''
    else:
        repository_info['descricao'] = desc.text
    finally:
        repository_info['nome'] = name
        repositories.append(repository_info)

sleep(3)
navigator.quit()


# Salvar o Resultado em um arquivo
new_file = input('Digite, APENAS o nome, do arquivo que sera salvo em (.csv e .json): ')
print('\n')

files = SaveFile()
files.save_file_csv(repositories, new_file)
files.save_file_json(repositories, new_file)