import os
import time 
from datetime import datetime
from selenium import webdriver 
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def open_and_use_bulk_script_generator(output_directory = 'Z:\Caboodle_DEV\BulkScriptGenerationDeploymentScripts', 
                                        console_url = 'https://spn4cdw001.sp.local/Caboodle_DEV', 
                                        checkboxes_to_check = ['DmcsAndPackages'],
                                        headless = True,
                                        max_retries = 5, 
                                        retry_delay_secs = 5):
    """
    Automates the bulk script generation process on Caboodle, , with retry mechanism if it fails.

    Arguments:
        console_url (str):          Base URL for the Caboodle console.
        output_directory (str):     Directory path where the scripts will be saved.
        checkboxes_to_check (str):  List of HTML ids of the checkboxes to select.
        headless (bool):            Whether to run web browser with GUI or in the background (i.e. "headless").
        max_retries (int):          Maximum number of retry attempts.
        retry_delay_secs (int):     Delay in seconds between retries.

    Returns:
        dict: A dictionary with the final status and directory contents or error details.

    Author: Mathias Schindler (mathias.schindler.01@regionh.dk)
    Creation Date: 27-11-2024
    """

    attempt = 0
    while attempt < max_retries:
        try:
            # CRUCIAL: Increment the attempt counter (otherwise will end in infinite loop)
            attempt += 1
            print(f"Bulk Script Generator: Attempt {attempt} of {max_retries}...")

            # Get current date and time for unique folder naming
            current_date_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_directory = f"{output_directory}\\{current_date_time}"

            # Initialize browser with headless options
            edge_options = EdgeOptions()
            edge_options.add_argument("--headless")  # Enable headless mode
            edge_options.add_argument("--disable-gpu")  # Disable GPU acceleration (useful for headless)
            edge_options.add_argument("--no-sandbox")  # Avoids issues on certain environments
            edge_options.add_argument("--disable-dev-shm-usage")  # Helps with low-memory systems

            # Initialize browser
            if headless == True:
                browser = webdriver.Edge(
                    service=EdgeService(EdgeChromiumDriverManager().install()),
                    options=edge_options  # Apply headless options
                )
            else:
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

            # Map checkbox IDs to their elements
            checkbox_elements = {
                "DmcsAndPackages": checkbox_dmcs,
                "ComponentConfiguration": checkbox_component_config,
                "Sources": checkbox_sources,
                "CustomSqlObjects": checkbox_custom_sql,
            }

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
            path_textbox.send_keys(output_directory)

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

            #input('Please press "Enter" to close program')

            return {"status": "success", "output_dir": output_directory}

        except Exception as e:
            print(f"Error! Script aborted because: {e}")
            return {"status": "error", "error": str(e)}

        finally:
            browser.quit()

if __name__ == '__main__':
    # For testing purposes will run in Cab_Ironman sandbox and only for "Sources" (much faster!)
    result = open_and_use_bulk_script_generator(output_directory = 'Z:\\Cab_Ironman\\BulkScriptGenerationDeploymentScriptsTest', 
                                        console_url = 'https://spn4cdw001.sp.local/Caboodle_DEV', #'https://spn4cdw001.sp.local/Cab_Ironman', 
                                        checkboxes_to_check = ['Sources'],
                                        headless = False,
                                        max_retries = 3, 
                                        retry_delay_secs = 3)
    print(result) 