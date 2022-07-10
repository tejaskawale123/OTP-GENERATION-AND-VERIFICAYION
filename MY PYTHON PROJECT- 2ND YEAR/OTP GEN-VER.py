fromcProfileimportlabel

fromtkinterimportLabel
importtwilio
importrandom

OTP=random.randint(100000,999999)

fromtwilio.restimportClient
account_sid ='AC531eaceaa24fa8fc634bfbfa9b15ab78'
auth_token ='61bf9dfb181a0d59941232977f595855'
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="Your OTP is ::"+str(OTP),
                     from_='+12312416250',
                     to='+917385326237'
                )
print("------------------------")
print("------------------------")
print("Successfully sent")
print("------------------------")
print("------------------------")
a=input("Enter your OTP ")
print("------------------------")
print("------------------------")
ifa==str(OTP):
    print("verified")
    print("------------------------")
    print("------------------------")
else:
    print("Please enter Valid OTP")
    print("------------------------")
    print("------------------------")

