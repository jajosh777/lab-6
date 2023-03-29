import os
import hashlib
import subprocess
import requests

def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
    link = ' http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    resp_msg = requests.get(link)

    if resp_msg==requests.codes:
        data=resp_msg
        print(data)
    return resp_msg

def download_installer():
    installer_link = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(installer_link)
    if resp_msg==requests.codes:
     return resp_msg

def installer_ok(installer_data, expected_sha256):
    hash_img=hashlib.sha256(installer_data).hexadigest()
    if hash_img== expected_sha256:
     return True

def save_installer(installer_data):
    name= 'file.exe'
    location= os.path.join(name)
    with open(location):
       file.write(installer_data)
    return name 

def run_installer(installer_path):
    subprocess.run([installer_path, '/L=1033', '/S'])
    return
    
def delete_installer(installer_path):
    os.remove(installer_path)
    return

if __name__ == '__main__':
    main()