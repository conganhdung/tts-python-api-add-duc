from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler
import os
import re
import cgi
import json
from sendingmail import send_single_email
from uploadfile import Upload_File
from download_file import Download_File
from querymysql import Query_Mysql


def read_html_template(path):

    """function to read HTML file"""
    try:
        with open(path) as f:
            file = f.read()
    except Exception as e:
        file = e
    return file

class Server(BaseHTTPRequestHandler):
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        
    def do_GET(self):

        if self.path == '/':
            self.path = '/index.html'
            try:
                split_path = os.path.splitext(self.path)
                request_extension = split_path[1]
                if request_extension != ".py":
                    f = open(self.path[1:]).read()
                    f += '<div class="hidden">'
                    for i in Query_Mysql.show_all_data_from_information():
                        f += '<div class="data-student" attr-id="1">'
                        f += f'<div id=number>{i[0]}</div>'
                        f += f'<div id=name>{i[1]}</div>'
                        f += f'<div id=age>{i[2]}</div>'
                        f += f'<div id=sex>{i[3]}</div>'
                        f += f'<div id=salary>{i[4]}</div>'

                    f += '</div>'
                #    print(f)
                    self.send_response(200)
                    self.send_header('value', 1)
                    self.end_headers()
                    self.wfile.write(bytes(f, 'utf-8'))
                else:
                    print(1)
                    f = "File not found"
                    self.send_error(404,f)
            except Exception as e:
                print(str(e))
                f = "File not found"
                self.send_error(404,f)
                
        elif self.path.find('/api/editModelName') != -1:
            # filehtml = '/index.html'
            m = ''.join(re.findall(r'\d', self.path))
            result =  Query_Mysql.select_from_information_by_id(m)
            result1=result[0]
            result_final = json.dumps(result1)
            self.send_response(200)
            self.send_header('value', 1)
            self.end_headers()
            self.wfile.write(result_final.encode(encoding='utf_8'))
            
        # elif self.path.find('/api/viewModelName') != -1 :
        #     ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
        #     # print(pdict)
        #     # print(ctype)
        #     # pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
        #     if ctype == 'application2/json':
        #         # print(1)
        #     # fields = cgi.parse_multipart(self.rfile, pdict)
        #         content_len = int(self.headers.get('Content-length', 0))
        #         print(1)
                
        #         post_body = self.rfile.read(content_len)
        #         string_format = str(post_body)
        #         string_format_1 = string_format.strip("b")
        #         string_format_final = string_format_1.strip("'")
        #         json_data = json.loads(string_format_final)
        #         id = json_data.get('id')
        #         print(json_data)
        #         Name = json_data.get('Name')
        #         Age = json_data.get('Age')
        #         Sex = json_data.get('Sex')
        #         Class = json_data.get('Class')
        #         # Query_Mysql.update_data(id, Name, Age , Sex , Class)
        #         html = f"<html><head></head><body><h1>Form data successfully recorded!!!</h1></body></html>"
        #         self.send_response(200, "OK")
        #         self.end_headers()
        #         self.wfile.write(bytes(html, "utf-8"))
        
            
    def do_POST(self):
        
        # "delete data by the id that be sent from html "
        if self.path.find('/api/deleteModelName') != -1:
            m = ''.join(re.findall(r'\d', self.path))
            Query_Mysql.delete_from_information_by_id(m)
            self.send_response(200)
            self.end_headers()
        # todo 
        "add the data that be sent from form when add data from button Add"
        #print(self.path.find('/api/add'))
        if self.path.find('/api/add') != -1 :

            ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
            # print(pdict)
            # print(ctype)
            # pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
            if ctype == 'application/json':
                # fields = cgi.parse_multipart(self.rfile, pdict)
                content_len = int(self.headers.get('Content-length', 0))
                post_body = self.rfile.read(content_len)
                string_format = str(post_body)
                string_format_1 = string_format.strip("b")
                string_format_final = string_format_1.strip("'")
                print(string_format_final)
                json_data = json.loads(string_format_final)
                id = json_data.get('id')
                Name = json_data.get('Name')
                Age = json_data.get('Age')
                Sex = json_data.get('Sex')
                Class = json_data.get('Class')
                Query_Mysql.insert_data(id, Name, Age , Sex , Class)
                html = f"<html><head></head><body><h1>Form data successfully recorded!!!</h1></body></html>"
                self.send_response(200, "OK")
                self.end_headers()
                self.wfile.write(bytes(html, "utf-8"))

        "update the data that be sent from form when add data from button Edit"
        if self.path.find('/api/edit') != -1 :
            ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
            # print(pdict)
            # print(ctype)
            # pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
            if ctype == 'application2/json':
                # fields = cgi.parse_multipart(self.rfile, pdict)
                content_len = int(self.headers.get('Content-length', 0))
                post_body = self.rfile.read(content_len)
                string_format = str(post_body)
                string_format_1 = string_format.strip("b")
                string_format_final = string_format_1.strip("'")
                json_data = json.loads(string_format_final)
                id = json_data.get('id')
                print(json_data)
                Name = json_data.get('Name')
                Age = json_data.get('Age')
                Sex = json_data.get('Sex')
                Class = json_data.get('Class')
                Query_Mysql.update_data(id, Name, Age, Sex, Class)
                html = f"<html><head></head><body><h1>Form data successfully recorded!!!</h1></body></html>"
                self.send_response(200, "OK")
                self.end_headers()
                self.wfile.write(bytes(html, "utf-8"))
                
        print(self.path)

        if self.path.find('/api/viewModelName') != -1 :
            ctype= cgi.parse_header(self.headers.get('Content-type'))
            # ctype = self.headers.get_header('content-type')
            # print(pdict)
            # print(ctype)
            # pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
            if ctype == 'application3/json':
                print(1)
                fields = cgi.parse_multipart(self.rfile, pdict)
                content_len = int(self.headers.get('Content-length', 0))                
                post_body = self.rfile.read(content_len)
                string_format = str(post_body)
                string_format_1 = string_format.strip("b")
                string_format_final = string_format_1.strip("'")
                json_data = json.loads(string_format_final)
                id = json_data.get('id')
                print(json_data)
                Name = json_data.get('Name')
                Age = json_data.get('Age')
                Sex = json_data.get('Sex')
                Class = json_data.get('Class')
                # Query_Mysql.update_data(id, Name, Age , Sex , Class)
                html = f"<html><head></head><body><h1>Form data successfully recorded!!!</h1></body></html>"
                self.send_response(200, "OK")
                self.end_headers()
                self.wfile.write(bytes(html, "utf-8"))
            


        if self.path.find('/api/send_email') != -1 :
            ctype = cgi.parse_header(self.headers.get('Content-type'))
            # print(pdict)
            # print(ctype)
            # pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
            #if ctype == 'application3/json':
                # fields = cgi.parse_multipart(self.rfile, pdict)
            content_len = int(self.headers.get('Content-length', 0))
            post_body = self.rfile.read(content_len)
            string_format = str(post_body)
            string_format_1 = string_format.strip("b")
            string_format_final = string_format_1.strip("'")
            json_data = json.loads(string_format_final)
            receiver_email = json_data.get('receiver_email')
            sender_email = json_data.get('sender_email')
            message = json_data.get('message')
            password = json_data.get('password')
            send_single_email.send_mail(receiver_email, sender_email, message, password)
            self.send_response(200, "OK")
            self.end_headers()

        if self.path.find('/api/upload') != -1:
            
            # ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
            ctype = cgi.parse_header(self.headers.get('Content-type'))
            # print(pdict)
            # print(ctype)
            # pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
            #if ctype == 'application3/json':
                # fields = cgi.parse_multipart(self.rfile, pdict)
            content_len = int(self.headers.get('Content-length', 0))

            post_body = self.rfile.read(content_len)


            string_format = str(post_body)
            string_format_1 = string_format.strip("b")
            string_format_final = string_format_1.strip("'")
            json_data = json.loads(string_format_final)
            id = json_data.get('id')
            filename = json_data.get('filename')
            id_drive = Upload_File.Get_Id_file(filename)
            address = 'https://drive.google.com/file/d/'+ id_drive + '/view?usp=sharing'
            Query_Mysql.insert_data_file_upload(id ,filename , address , id_drive)
            self.send_response(200, "OK")
            self.end_headers()

        if self.path.find('/api/download') != -1:
            
            # ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
            ctype = cgi.parse_header(self.headers.get('Content-type')) 
            content_len = int(self.headers.get('Content-length', 0))
            post_body = self.rfile.read(content_len)
            string_format = str(post_body)
            string_format_1 = string_format.strip("b")
            string_format_final = string_format_1.strip("'")
            json_data = json.loads(string_format_final)
            id = json_data.get('id')
            list_id = Query_Mysql.get_drive_id_from_fileupload(id)
            for i in list_id:
                destination = Query_Mysql.get_filename_from_fileupload(id)
                idofdrive = Query_Mysql.get_drive_id_from_fileupload(id)
                Download_File.download_file_from_google_drive(idofdrive,destination)


            
