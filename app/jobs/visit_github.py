from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# Navegador com robo
def visit_github(user_name: str):
    navigator = webdriver.Chrome()

    navigator.implicitly_wait(5)
    navigator.get(f'https://github.com/{user_name}')

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
    return repositories