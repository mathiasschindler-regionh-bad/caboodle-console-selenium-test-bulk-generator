import os
import time
from dotenv import load_dotenv
from selenium import webdriver 
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

try:
    # Initialize browser
    Browser = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install())
    )

    # Open the Caboodle console to initialize login process
    ConsoleURL = 'https://spn4cdw001.sp.local/Cab_Ironman'
    Browser.get(ConsoleURL)

    # Open Bulk Script Generator
    Browser.get(ConsoleURL + "/tools/BulkScriptGeneration")

    input('Please press "Enter" to close program')

except Exception as e:
    print(f"Error! Script aborted because: {e}")

finally:
    Browser.quit()
