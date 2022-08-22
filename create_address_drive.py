
from uploadfile import Upload_File
from google2 import CreateService

CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = CreateService.create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Update Sharing Setting
file_id = f'<{Upload_File.main()}>'

request_body = {
    'role': 'reader',
    'type': 'anyone'
}

response_permission = service.permissions().create(
    fileId=file_id,
    body=request_body
).execute()

print(response_permission)


# Print Sharing URL
response_share_link = service.files().get(
    fileId=file_id,
    fields='webViewLink'
).execute()

print(response_share_link)

# Remove Sharing Permission
service.permissions().delete(
    fileId=file_id,
    permissionId='anyoneWithLink'
).execute()