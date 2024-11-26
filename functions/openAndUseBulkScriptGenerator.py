import os
import time 
from datetime import datetime
from selenium import webdriver 
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def open_and_use_bulk_script_generator(output_directory = 'C:\CustomPackages\Caboodle_DEV\BulkScriptGenerationDeploymentScriptsTest', 
                                        console_url = 'https://spn4cdw001.sp.local/Caboodle_DEV', 
                                        checkboxes_to_check = ['DmcsAndPackages']):
    """
    Automates the bulk script generation process on Caboodle.

    Arguments:
        console_url (str):          Base URL for the Caboodle console.
        output_directory (str):     Directory path where the scripts will be saved.
        checkboxes_to_check (str):  List of HTML ids of the checkboxes to select.

    Returns:
        None
    """
    try:
        # Get current date and time for unique folder naming
        current_date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_directory = f"{output_directory}\\{current_date_time}"

        # Initialize browser
        browser = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install())
        )

        # Navigate to the Bulk Script Generator page
        browser.get(console_url + "/tools/BulkScriptGeneration")

        # Wait for the checkboxes to load 
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "DmcsAndPackages"))
        )
        checkbox_dmcs = browser.find_element(By.ID, 'DmcsAndPackages')
        checkbox_component_config = browser.find_element(By.ID, 'ComponentConfiguration')
        checkbox_sources = browser.find_element(By.ID, 'Sources')
        checkbox_custom_sql = browser.find_element(By.ID, 'CustomSqlObjects')

        # Click checkbox if:
        #  1) Checkbox should be checked but is not checked
        #  2) Checkbox should not be checked but is checked 
        for checkbox_id, checkbox in checkbox_elements.items():
            if checkbox_id in checkboxes_to_check and not checkbox.is_selected():
                checkbox.click()
            elif checkbox_id not in checkboxes_to_check and checkbox.is_selected():
                checkbox.click()

        # Write the output directory path into the input element
        path_textbox = browser.find_element(By.ID, 'OutputDirectory')
        path_textbox.clear()
        path_textbox.send_keys(dynamic_output_directory)

        # Click the "Generate Scripts" button
        generate_btn = browser.find_element(By.ID, 'formAcceptBtn')
        generate_btn.click()

        # Wait until the final status is displayed
        WebDriverWait(browser, 3600).until(
            EC.invisibility_of_element_located((By.ID, "StatusUpdatesText"))
        )
        WebDriverWait(browser, 3600).until(
            EC.presence_of_element_located((By.ID, "FinalStatusText"))
        )

        print("Script generation completed successfully!")
        # input('Please press "Enter" to close program')

    except:
        print(f"Error! Script aborted because: {e}")

    finally:
        browser.quit()

if __name__ == 'main':
    # For testing purposes will run in Cab_Ironman sandbox and only for "Sources" (much faster!)
    open_and_use_bulk_script_generator(output_directory = 'C:\CustomPackages\Caboodle_DEV\BulkScriptGenerationDeploymentScriptsTest', 
                                        console_url = 'https://spn4cdw001.sp.local/Cab_Ironman', 
                                        checkboxes_to_check = 'Sources')