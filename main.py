import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.drive import GoogleDriveFileList

def authentication():
    auth = GoogleAuth()
    auth.LocalWebserverAuth()

    return GoogleDrive(auth)

"""def dup_checker():
    
    if """

# //Duplication checker and more

drive = authentication()

drive_path = ''        # YOUR GOOGLE DRIVE PATH URL
folder = r""           # DIRECTORY OF THE RESPECTIVE FOLDER YOU WANT TO UPLOAD TO GOOGLE DRIVE

for file in os.listdir(folder):

    filepath = os.path.join(folder, file)
    filesize = os.path.getsize(filepath) >> 20
    print('Uploading ' + file + ' Size: ' + str(filesize) + ' MB')

    upload_file = drive.CreateFile({'parents': [{'id': drive_path}], 'title': file})
    upload_file.SetContentFile(filepath)
    upload_file.Upload()

exit()
