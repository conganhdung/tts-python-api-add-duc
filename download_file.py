import requests

class Download_File:

    def download_file_from_google_drive(id, destination):
        URL = "https://docs.google.com/uc?export=download"
        session = requests.Session()
    
        response = session.get(URL, params = { 'id': id }, stream = True)
        token = Download_File.get_confirm_token(response)
        if token:
            params = { 'id': id , 'confirm': token }
            response = session.get(URL, params = params, stream = True)
        Download_File.save_response_content(response, destination)
            

    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None


    def save_response_content(response, destination):
        CHUNK_SIZE = 32768
        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                  

# if __name__ == "__main__":
#     file_id = Upload_File.Get_Id_file("1.jpg")
#     destination = '/home/cong/Downloads/%s' % (Upload_File.Get_Name_file("1.jpg"))
#     Download_File.download_file_from_google_drive(file_id, destination)