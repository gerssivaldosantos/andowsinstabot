#Author: Gerssivaldo Oliveira dos Santos
#Github: github.com/andows159     linlkedin:https://www.linkedin.com/in/gerssivaldo-santos-a75921130/ 

#In this code, I used geckodriver, this webdriver work with Firefox browser
#The code is working with this web driver, but you can change it to another web driver of your preference

from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from random import randint
from random import choice
from time import sleep

class BotInstagramBackEnd:
    def __init__(self, login, password, url,comments, like_option, number_roll_page):
#Parameters of the webdriver and selenium    
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.browser = Firefox(firefox_profile=firefoxProfile)
        self.counter_comments = 0
        self.list_of_posts = list
        self.like_option = like_option
        self.number_roll_page = number_roll_page       
        self.login = login
        self.password = password
        self.url = url
        self.comments = comments
        self.start_login()
        self.extract_data_from_page()
        self.comment_on_posts()
        #self.follow_profile_users()

#access the site and log in    
    def start_login(self):
        self.browser.get('https://www.instagram.com/?hl=pt-br')
        sleep(5)
        login_box = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input') 
        login_box.click()
        login_box.clear()
        login_box.send_keys(self.login)
        password_box = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        password_box.click()
        password_box.clear()
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.RETURN)
        sleep(5)
        self.browser.get(self.url)

    def write_as_human(self,single_input_field):
        for letter in self.comments:
            single_input_field.send_keys(letter)
            sleep(randint(1, 5) / 30)

    def roll_page(self):
        for _ in range(0, self.number_roll_page):  
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(3)

    def close_browser(self):
        self.browser.quit()

    def extract_data_from_page(self):
        self.links_of_posts = []
        driver = self.browser
        sleep(5)
        self.roll_page()
        hrefs = driver.find_elements_by_tag_name("a")
        hrefs_posts = [elem.get_attribute("href") for elem in hrefs]
        for link in hrefs_posts:
            try:
                if link.index("/p/") != -1:
                    self.links_of_posts.append(link)
            except:
                pass 

    def like_post(self):
        like_button = self.browser.find_element_by_class_name("fr66n")
        like_button.click()

    def breaker(self):
        self.parameter_break_comment = True
    
    def comment_on_posts(self):
        driver = self.browser
        self.list_of_posts = list()
        self.parameter_break_comment = False
        for href_post in self.links_of_posts:
            driver.get(href_post)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_class_name("Ypffh").click()
                comment_input_box = driver.find_element_by_class_name("Ypffh")
                sleep(randint(2, 5))
                self.write_as_human(comment_input_box)
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                self.list_of_posts.append(str(href_post))
                self.counter_comments += 1
                if self.like_option == True:
                    self.like_post()
                    print(f'post {href_post} comentado e curtido',end=" ")
                else:
                    print(f'post {href_post} comentado',end=" ")
                sleep(randint(3, 5))
                print(f" post nª{self.counter_comments}")
                #print(f"List of post released {self.list_of_posts}")
            except:
                print(f"Não foi possível comentar em {href_post}")
                sleep(5)
            if self.parameter_break_comment == True:
                break
        print(f"a lista de todas as publicações comentadas é:\n {self.links_of_posts}")
        

    #this is a future feature, will be implanted on the next code version
        
    def follow_profile_users(self):
        button = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        button.click()
        sleep(3)
        #self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li[3]").click(
        self.browser.find_element_by_class_name("m82CD").click()
        self.roll_page()
        follow_buttons = self.browser.find_elements_by_xpath("//button[contains(text(), 'Seguir')]")
        for follow_button in follow_buttons:
            try:
                print(f"follow button clicked {follow_button}")
                #click fuction used for solution error with normal click fuction
                self.browser.execute_script("arguments[0].click();",follow_button)
                self.roll_page()
                follow_buttons = self.browser.find_elements_by_xpath("//button[contains(text(), 'Seguir')]")
                sleep(1/4)
            except:
                print("all accounts followed")
   

class ConsolInterface():
    def __init__(self):
        print("""    _              _                   ___           _        ____        _   
   / \   _ __   __| | _____      _____|_ _|_ __  ___| |_ __ _| __ )  ___ | |_ 
  / _ \ | '_ \ / _` |/ _ \ \ /\ / / __|| || '_ \/ __| __/ _` |  _ \ / _ \| __|
 / ___ \| | | | (_| | (_) \ V  V /\__ \| || | | \__ \ || (_| | |_) | (_) | |_ 
/_/   \_\_| |_|\__,_|\___/ \_/\_/ |___/___|_| |_|___/\__\__,_|____/ \___/ \__|
                                                                              
"""
        )
        print("="*74)
        print("               Versão Alpha Teste 1.0, seja Bem Vindo(a)")
        print("="*74)

        titulos = ('Login','Senha','hashtag','Comentário', 'Like ?[S/N]','Número de rolagens')
        aviso = ('Dado de email, número de telefone ou nome de usuário de sua conta',
        'Dado da senha', 'A hashtag que deseja extrair as publicações para serem comentadas',
        'Qual comentário deseja que seja inserido nas públicações?',
        'Deseja que além de comentado, seja curtido ?',
        'qual o número de rolagens na página você deseja que sejam efetuadas ? \n o robô vai extrair os dados quando forem carregados na tela \n o instagram carrega estes dados conforme o usuário vai rolando a página \n isso significa que este número influencia em quantos posts serão acessados')
        dados = list()
        for dado in range(0,6):
            print("="*74)
            print(f"{aviso[dado]}")
            print("")
            dados.append(input(f"{(titulos[dado])} : "))
            

        dados[5] = int(dados[5])
        dados[2] = f"https://www.instagram.com/explore/tags/{dados[2]}/?hl=pt-br"

        if dados[4] == 'S':
            dados[4] = True
        elif dados[4] == 's':
            dados[4] = True

        else:
            dados[4] = False
            
        print("="*74)
        print(""" ____                                          
        |  _ \ _ __ ___   __ _ _ __ ___  ___ ___  ___  
        | |_) | '__/ _ \ / _` | '__/ _ \/ __/ __|/ _ \ 
        |  __/| | | (_) | (_| | | |  __/\__ \__ \ (_) |
        |_|   |_|  \___/ \__, |_|  \___||___/___/\___/ 
                        |___/                         
        """)
        print("")
        

        a = BotInstagramBackEnd(dados[0],dados[1],dados[2],dados[3],dados[4],dados[5])




a = ConsolInterface()



