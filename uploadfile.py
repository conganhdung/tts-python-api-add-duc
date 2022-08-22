
from email.mime import image
import json
import string
from unicodedata import name
import requests

class Upload_File:

    def Upfile(name):
        name_of_file = str(name)
        # print(name_of_file)
        headers = {"Authorization": "Bearer ya29.A0AVA9y1skUpb9x2FheykK4sYXYk0I_lz_98_4O6N05HTKLVwfO_0LYMy6HyKUy6um2QGT9SIYguenCNy0UuA2FkmdFZa61AEfA_OZID4eQ9UyNwopNmkugFoW_-46N4q2gKtnsUwKPmW1uAW4Njyn7Bhnu2OSaCgYKATASATASFQE65dr8mYcpEq08Q0yF9Ncm_X6g1Q0163"}
        
        para = {
            "name": f"{name_of_file}",
            "parents": ["1fl06GLFKjN4NVNCYnwXLFjIoX03M0eyR"]
        }
        # print(para)
        files = {
            'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
            'file': open((f"./{name_of_file}"), "rb")
        }
        # print(files)
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files
        )
        return(r.text)
    def Get_Id_file(name):
        # print(type(Upload_File.Upfile(name)))
        # json_object = json.loads(employee_string)
        jsonObject = json.loads(Upload_File.Upfile(name))
        # print(jsonObject)
        # id = 'https://drive.google.com/file/d/'+ jsonObject['id'] + '/view?usp=sharing'
        id =  jsonObject['id']

        return(id)
        
# def main():
#     k = 'https://drive.google.com/file/d/'+ Upload_File.Get_Id_file("image.png") + '/view?usp=sharing'
#     print(k)
# if __name__ == "__main__":
#     main()

