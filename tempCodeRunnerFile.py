import os
from ftplib import FTP

def upload_ftp_folder(ftp, folder_path, remote_path):
    try:
        ftp.cwd(remote_path)
    except Exception:
        ftp.mkd(remote_path)
        ftp.cwd(remote_path)

    for item in os.listdir(folder_path):
        local_path = os.path.join(folder_path, item)
        if os.path.isfile(local_path):
            with open(local_path, 'rb') as file:
                ftp.storbinary(f'STOR {item}', file)
            print(f'Uploaded file: {local_path} to {remote_path}/{item}')
        elif os.path.isdir(local_path):
            try:
                ftp.mkd(item)
            except Exception:
                pass
            upload_ftp_folder(ftp, local_path, f'{remote_path}/{item}')
            ftp.cwd('..')

def main():
    ftp_host = '82.25.125.141'  # or 'kitsw.site'
    ftp_user = 'u464826052'
    ftp_pass = 'QWERTY123456@a'
    ftp_port = 21  # default FTP port

    ftp = FTP()
    ftp.connect(ftp_host, ftp_port)
    ftp.login(ftp_user, ftp_pass)
    print(f'Connected to FTP server: {ftp_host}')

    local_folder = 'KITSW'  # local folder to upload
    remote_folder = '/public_html'  # remote folder path on FTP server

    upload_ftp_folder(ftp, local_folder, remote_folder)

    ftp.quit()
    print('FTP upload completed.')

if __name__ == '__main__':
    main()
