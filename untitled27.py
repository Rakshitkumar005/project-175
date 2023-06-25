import matplotlib.pyplot as plt
import psutil as p

app_name_dict={}

count=0

for process in p.process_iter():
    count=count+1
    if count<=6:
        name=process.name()
        cpu_usage=p.cpu_percent()
        print("Name : ",name,"-- Cpu Usage ",cpu_usage)
        app_name_dict.update({name:cpu_usage})
        keymax=max(app_name_dict,key=app_name_dict.get)
        print(keymax)
        keymin=min(app_name_dict,key=app_name_dict.get)
        name_list=[keymax,keymin]
        print(name_list)
        app_name=app_name_dict.values()
        max_app=max(app_name)
        print(max_app)
        min_app=min(app_name)
        print(min_app)
        max_min_list=[max_app,min_app]
        print(max_min_list)
        
plt.figure(figsize=(15,7))
plt.xlabel("Applications")
plt.ylabel("Usage")   
plt.bar(name_list,max_min_list,width=0.5,color=("blue","orange")) 
plt.show()    