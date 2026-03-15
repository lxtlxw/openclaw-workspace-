import requests
import os
import sys
import io
import zipfile
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Download agent-browser skill from github
url = "https://github.com/openclaw/skill-agent-browser/archive/refs/heads/master.zip"
save_path = "agent-browser.zip"
extract_path = r"C:\Users\Administrator\.openclaw\workspace\skills\agent-browser"

try:
    print(f"Downloading {url}...")
    # Use proxy if available
    proxies = {
        'http': 'http://127.0.0.1:7890',
        'https': 'http://127.0.0.1:7890',
    }
    response = requests.get(url, proxies=proxies, stream=True, timeout=30)
    response.raise_for_status()
    
    with open(save_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Download completed: {save_path}")
    
    # Extract zip
    if os.path.exists(extract_path):
        import shutil
        shutil.rmtree(extract_path)
    
    with zipfile.ZipFile(save_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.dirname(extract_path))
    
    # Rename folder (github adds -master suffix)
    extracted_folder = os.path.join(os.path.dirname(extract_path), "skill-agent-browser-master")
    if os.path.exists(extracted_folder):
        os.rename(extracted_folder, extract_path)
        print(f"Extracted to: {extract_path}")
    
    os.remove(save_path)
    print("Done!")
    
except Exception as e:
    print(f"Error with proxy: {e}")
    print("Trying without proxy...")
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Download completed: {save_path}")
        
        if os.path.exists(extract_path):
            import shutil
            shutil.rmtree(extract_path)
        
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(extract_path))
        
        extracted_folder = os.path.join(os.path.dirname(extract_path), "skill-agent-browser-master")
        if os.path.exists(extracted_folder):
            os.rename(extracted_folder, extract_path)
            print(f"Extracted to: {extract_path}")
        
        os.remove(save_path)
        print("Done!")
    except Exception as e2:
        print(f"Final error: {e2}")
