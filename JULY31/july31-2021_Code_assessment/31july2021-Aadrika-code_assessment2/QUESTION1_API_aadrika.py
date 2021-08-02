import json
import requests
try:
    data=requests.get("https://jsonplaceholder.typicode.com/todos")
    ExtractD=data.json()
    True_L=[]
    List_Of_True=[i for i in ExtractD if i["completed"]==True]
    True_L.append(List_Of_True)
    print(True_L)

except:
    print("Please check the link if it is not correct") #handling exception

else:
    print("We got details for True information") #else will run if except block dont

finally:
    print("Good job, task completed ") #finally will run 