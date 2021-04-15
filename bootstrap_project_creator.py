import os
import urllib.request as rq
import webbrowser as wb

repeat = 'y'
project_lst = list()

print("\n")
print('####   ######  ######  ######  ######  ######  ####      ##    ####  ')
print('#   #  #    #  #    #    ##    #         ##    #    #   #  #   #    #')
print('####   #    #  #    #    ##    ######    ##    ####    ######  ####  ')
print('#   #  #    #  #    #    ##         #    ##    #  #    #    #  #     ')
print('####   ######  ######    ##    ######    ##    #    #  #    #  #     ')

while(repeat == 'y' or repeat == 'Y'):    

    def create_project_dir(file_name):
        if(os.path.isdir(file_name)):
            print('\nThe '+file_name+" Project has already been created")
            os.chdir(file_name)
        else:
            os.mkdir(file_name)
            print('\nThe '+file_name+" Project created")
            os.chdir(file_name)

    def create_project_sub_dir(files):
        for file in files:
            if(os.path.isdir(file)):
                print('\nThe '+file+" Directory has already been created")
            else:
                os.mkdir(file)
                print('\nThe '+file+" Directory created")

    def css_write_files(urls,file,files_name):
        for url in urls[file]:                
            request_data = rq.urlopen(url)
            for fn in files_name:
                f = open(fn,"wt")
                for line in request_data:
                    f.write(line.decode("utf-8"))
                files_name.remove(fn)            
                break

    def js_write_files(urls,file,files_name):
        for url in urls[file]:
            #print(url)
            request_data = rq.urlopen(url)
            for fn in files_name:
                f = open(fn,"wt")
                for line in request_data:
                    f.write(line.decode("utf-8"))
                files_name.remove(fn)
                #print(files_name)
                break

    def create_project_sub_dir_file(urls,files,files_name):    
        for file in files:
            cur_dir = os.getcwd()
            if(file == "css"):
                os.chdir(file)            
                css_write_files(urls,file,files_name)

            else:
                os.chdir(os.path.dirname(cur_dir))
                os.chdir(file)                               
                js_write_files(urls,file,files_name)  

    def create_index_file(data):
        os.chdir("../")
        #print(os.getcwd())
        f = open('index.html','wt')
        f.write(data)
        print('\nThe index.html File created')

    print("\n----------------------Bootstrap Project Creater----------------------")    

    project_name = input("\nEnter the name of your project\n")

    while(project_name == ''):
        print("\n----------------------Bootstrap Project Creater----------------------")
        project_name = input("\nEnter the name of your project\n")
        if(project_name != ''):
            break

    select_bootstrap_version = None
    files = ['css','js']
    files_name = ['bootstrap.min.css','bootstrap.min.js','popper.min.js','jquery.min.js','fontawesome.css','fontawesome.js']
    urls_v4_6 = {"css":["https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css"],
            "js":["https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.min.js",
            "https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js",
            "https://code.jquery.com/jquery-3.5.1.slim.min.js"]};

    urls_v5_0 = {"css":["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"],
            "js":["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.min.js",
            "https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js",
            "https://code.jquery.com/jquery-3.6.0.slim.min.js"]};

    while(True):
        select_bootstrap_version = str(input("\nSelect the Bootstrap Version:\n \t\t     (1) v5.0 \n \t\t     (2) v4.6 \n"))
        if(select_bootstrap_version == '1' or select_bootstrap_version == '2'):
            break        

    create_project_dir(project_name)
    create_project_sub_dir(files)

    if(select_bootstrap_version == '1'):
        create_project_sub_dir_file(urls_v5_0,files,files_name)
    else:
        create_project_sub_dir_file(urls_v4_6,files,files_name)
    
    index_file_data = """<!DOCTYPE html><html><head><meta charset='utf-8'><meta http-equiv='X-UA-Compatible' content='IE=edge'>
                         <title>"""+ project_name +"""</title><meta name='viewport' content='width=device-width, initial-scale=1'><link rel='stylesheet' type='text/css' media='screen' href='css/bootstrap.min.css'>
                         <link rel='stylesheet' type='text/css' media='screen' href='css/fontawesome.css'><script src='js/bootstrap.min.js'></script><script src='js/fontawesome.js'></script>
                         <script src='js/jquery.min.js'></script><script src='js/popper.min.js'></script></head><body><h1>"""+project_name+"""</h1></body></html>"""
    create_index_file(index_file_data)
    
    project_lst.append(project_name)

    while(True):
        fontawesome = input("\nDo you want to add Fontawesome? (y/Y/n/N)")
        if(fontawesome == 'y' or fontawesome == 'Y' or fontawesome == 'n' or fontawesome == 'N'):
            break            

    if(fontawesome == 'Y' or fontawesome == 'y'):
        font = {'css':['https://use.fontawesome.com/releases/v5.15.3/css/all.css'],'js':['https://use.fontawesome.com/releases/v5.15.3/js/all.js']}
        create_project_sub_dir_file(font,files,files_name)
        os.chdir("../../")
        #print(os.getcwd())
    else:
        os.chdir("../")
        #print(os.getcwd())

    while(True):
        repeat = input("\nDo you want to create another Project? (y/Y/n/N)")
        if(repeat == 'y' or repeat == 'Y' or repeat == 'n' or repeat == 'N'):
            break 
        
    if(repeat == 'N' or repeat == 'n'):        
        for project in project_lst:
            #print(project)
            os.chdir(project)
            url = os.getcwd()+"\index.html"
            wb.open_new_tab(url)
            os.chdir("../")            
            # print(url)
        break