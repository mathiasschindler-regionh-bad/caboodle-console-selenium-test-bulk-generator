import os
import time 
from datetime import datetime
from selenium import webdriver 
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

try:
    # Get today's date
    current_date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Initialize browser
    Browser = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install())
    )

    # Open the Caboodle console to initialize login process
    #ConsoleURL = 'https://spn4cdw001.sp.local/Caboodle_DEV'
    ConsoleURL = 'https://spn4cdw001.sp.local/Cab_Ironman'
    Browser.get(ConsoleURL)

    # Open Bulk Script Generator
    Browser.get(ConsoleURL + "/tools/BulkScriptGeneration")

    # Select correct checkbox
    # Locate checkboxes by ID
    WebDriverWait(Browser, 10).until(
        EC.presence_of_element_located((By.ID, "DmcsAndPackages"))
    )
    checkbox_dmcs = Browser.find_element(By.ID, 'DmcsAndPackages')
    checkbox_component_config = Browser.find_element(By.ID, 'ComponentConfiguration')
    checkbox_sources = Browser.find_element(By.ID, 'Sources')
    checkbox_custom_sql = Browser.find_element(By.ID, 'CustomSqlObjects')

    # Check the sources checkbox:
    # NB: To be changed to "DMCs and Packages" at a later stage
    if not checkbox_dmcs.is_selected():
        checkbox_dmcs.click()

    # Uncheck undesired checkboxes if is checked
    if checkbox_sources.is_selected():
        checkbox_sources.click()
    if checkbox_component_config.is_selected():
        checkbox_component_config.click()
    if checkbox_custom_sql.is_selected():
        checkbox_custom_sql.click()

    # Write path into input element
    path_textbox = Browser.find_element(By.ID, 'OutputDirectory')
    path_textbox.send_keys(f"C:\CustomPackages\Caboodle_DEV\BulkScriptGenerationDeploymentScriptsTest\{current_date_time}")

    # Press "Generate Scripts" Button
    generate_btn = Browser.find_element(By.ID, 'formAcceptBtn')
    generate_btn.click()

    # Wait until final status text is existing
    WebDriverWait(Browser, 3600).until(
        EC.invisibility_of_element_located((By.ID, "StatusUpdatesText"))
    )
    WebDriverWait(Browser, 3600).until(
        EC.presence_of_element_located((By.ID, "FinalStatusText"))
    )

    #input('Please press "Enter" to close program')

except Exception as e:
    print(f"Error! Script aborted because: {e}")

finally:
    Browser.quit()
