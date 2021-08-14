import time,pymongo,smtplib,logging
import validation
from collections import deque
logging.basicConfig(filename='bloodbank.log',level=logging.DEBUG)


client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = client['donorDb']
collection_name = mydatabase['donors']

bgroupList= []
List = []
donorList = deque(List)
class Donor:
    def addDonor(self,name,addr,bgroup,pincode,mobno,email,last_donated_date,place):
        current_local_time=time.strftime("%H:%M:%S",time.localtime())
        dict = {"name":name,"address":addr,"bgroup":bgroup,"pincode":pincode,"mobno":mobno,"email":email,"last_donated_date":last_donated_date,"place":place,"addedon":current_local_time,"flag":0}
        donorList.append(dict)
        collection_name.insert_many(donorList)

d1 = Donor()
try:
    while(1):
        print("-------BLOOD BANK MANAGEMENT SYSTEM--------")

        print("1. Add Donors ")
        print("2. Search donors based on blood group ")
        print("3. Search donors based on blood group and place ")
        print("4. Update all donor details using their mobile number")
        print("5. Delete the donor details using mobile number")
        print("6. Display total number of donors on each blood group")
        print("7. Immediate notification to all via email")
        print("8. Exit")
        choice= int(input("Enter your choice: "))

        if choice == 1:
            while(1):
                name = input("Enter your name: ")
                addr= input("Enter your address: ")
                bgroup = input("Enter your blood group: ")
                pincode=input("Enter the pincode: ")
                mobno = input("Enter your mobile number: ")
                email = input("Enter Email-id:")
                last_donated_date = input("Enter last blood donated date: ")
                place = input("Enter your place: ")
                if validation(name,bgroup,pincode,mobno,email,last_donated_date):
                    d1.addDonor(name,addr,bgroup,pincode,mobno,email,last_donated_date,place)   
                else:
                    print("Please try again by entering valid data")
                    continue
                break 
        if choice == 2:
            search=input("Enter blood group to search: ")
            res = collection_name.find({"$and":[{"bgroup":search}]})
            for i in res:
                print(i) 

        if choice == 3:
            bg = input("Enter blood group to search: ")
            pl = input("Enter the place name:")
            res1 =collection_name.find({"$and":[{"bgroup":bg},{"place":pl}]})
            for i in res1:
                print(i)
        if choice == 4:

            print("Enter your mobile number whose data has to be updated :")
            mob=input("Enter your mobile number:")
            print("Enter the latest data:")
            name = input("Enter your name: ")
            add= input("Enter your address: ")   
            pin=input("Enter the pincode: ")
            M= input("Enter your mobile number: ")
            last_date = input("Enter last blood donated date: ")
            Place = input("Enter your place: ")
            res=collection_name.update_one({"$and":[{"mobno":mob}]},{"$set":{"name":name,"address":add,"pincode":pin,"mobno":M,"last_donated_date":last_date,"place":Place}})

        if choice == 5:
            Mo = input("Enter the mobile number:")
            res2 = collection_name.update_one({"$and":[{"mobno":Mo}]},{"$set":{"flag":1}})
            print(res2)
            print("Deleted Successfully")

        
        if choice == 7:
            msg = input("Enter the message to send notification email to donors:") 
            message=str(f'Hello everyone,{msg}')
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("sureshbannur6@gmail.com","aks.1513")
            connection.sendmail("sureshbannur6@gmail.com",email,message)

            print("Email successfully sent to donors")
            logging.info("Transaction Successful")
            
            connection.quit()
            break  
        if choice == 8:
            break   
except:
    print("Something went wrong, Please try again")
    logging.error("Something went wrong. Please try again") 
finally:
    print("Thank You")            

         


        

 