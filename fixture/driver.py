from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from helpers.config_parser import ApplicationConfig

app_config = ApplicationConfig()


class ChromeDriver:
    def __init__(self, env):
        # silent run
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        # visualized run
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # --------------------------------------------------
        self.driver.get(self.env_identification(env))
        self.driver.implicitly_wait(15)

    @staticmethod
    def env_identification(env):
        start_link = app_config.environments[env]
        return start_link
