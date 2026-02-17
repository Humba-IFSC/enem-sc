import undetected_chromedriver as uc
import time
import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def upload_file(notebook_id, file_path, profile_dir):
    options = uc.ChromeOptions()
    options.add_argument(f"--user-data-dir={profile_dir}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new") # Use new headless mode for stability
    
    print(f"Starting browser with profile: {profile_dir}", flush=True)
    driver = uc.Chrome(options=options)
    
    try:
        url = f"https://notebooklm.google.com/notebook/{notebook_id}"
        print(f"Navigating to {url}", flush=True)
        driver.get(url)
        
        # Wait for the page or login redirection
        wait = WebDriverWait(driver, 30)
        
        # Check if we are on the login page
        if "accounts.google.com" in driver.current_url:
            print("Error: Profile is not authenticated. Manual login required.", flush=True)
            return False
            
        print("Page loaded. Looking for 'Add Source' button...", flush=True)
        # Try to find the Add Source button. Usually contains a plus or "Add source" text.
        add_source_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add source') or contains(@aria-label, 'Add source')]")))
        add_source_btn.click()
        print("Clicked 'Add source'. Waiting for modal...", flush=True)
        
        # Look for "Upload from computer" or similar. Usually a tab or a button.
        upload_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(., 'Upload')] | //button[contains(., 'Local')]")))
        upload_tab.click()
        print("Selected Upload tab.", flush=True)
        
        # Find the file input (often hidden)
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        print(f"Found file input. Uploading: {file_path}", flush=True)
        file_input.send_keys(file_path)
        
        # Wait for upload to complete
        print("Waiting for upload to finish...", flush=True)
        time.sleep(20) # Conservative wait
        
        print("Upload sequence completed.", flush=True)
        return True
    except Exception as e:
        print(f"An error occurred: {e}", flush=True)
        return False
    finally:
        driver.quit()

if __name__ == "__main__":
    notebook_id = "54edf03f-279f-41ca-8f4a-fd23d8fc9d87"
    file_path = "/home/humba/Documentos/Meus_Projetos/Correlacao_ENEM/0_Referencias_Originais/ENEM_DNA_O_Mapa_da_Coerência_Cognitiva.pdf"
    profile_dir = "/home/humba/.local/share/notebooklm-mcp/chrome_profile_notebooklm"
    
    success = upload_file(notebook_id, file_path, profile_dir)
    if success:
        print("SUCCESS")
        sys.exit(0)
    else:
        print("FAILURE")
        sys.exit(1)
