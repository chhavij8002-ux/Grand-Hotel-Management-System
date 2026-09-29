print("WELCOME TO THE GRAND HOTEL")

name=input("PLEASE ENTER YOUR USER NAME: ")
phone=input("PLEASE ENTER YOUR PHONE NUMBER: ")

while len(phone)!=10 or not phone.isdigit():
  print("INVALID PHONE NUMBER! PLEASE ENTER A 10-DIGIT NUMBER.")
  phone=input("PLEASE ENTER YOUR PHONE NUMBER: ")

print("\nCHOOSE YOUR ROOM: ")
print("1. STANDARD ROOM")
print("2. DELUXE ROOM")
print("3. SUITE ROOM")

room=input("ENTER YOUR CHOICE: ")

while room=="" or not room.isdigit() or int(room)<1 or int(room)>3:
  print("INVALID CHOICE! PLEASE CHOOSE 1,2 OR 3.")
  room=input("ENTER YOUR CHOICE: ")

room=int(room)

if room==1:
  room_price=2000
  print("STANDARD ROOM SELECTED.")
elif room==2:
  room_price=3500
  print("DELUXE ROOM SELECTED.")
else:
  room_price=5000
  print("SUITE ROOM SELECTED.")


print("\nCHOOSE BED SIZE: ")
print("1. SINGLE BED")
print("2. DOUBLE BED")
print("3. KING SIZE BED")

bed=input("ENTER YOUR CHOICE: ")

while bed=="" or not bed.isdigit() or int(bed)<1 or int(bed)>3:
  print("INVALID CHOICE! PLEASE CHOOSE 1,2 OR 3.")
  bed=input("ENTER YOUR CHOICE: ")

bed=int(bed)

if bed==1:
  bed_price=100
  print("SINGLE BED SELECTED.")
elif bed==2:
  bed_price=500
  print("DOUBLE BED SELECTED.")
else:
  bed_price=1000
  print("KING SIZE BED SELECTED.")


nights=input("\nENTER NUMBER OF NIGHTS: ")

while nights=="" or not nights.isdigit() or int(nights)<=0:
  print("INVALID NUMBER OF NIGHTS!")
  nights=input("ENTER NUMBER OF NIGHTS: ")

nights=int(nights)

room_total=(room_price+bed_price)*nights


print("\nCHOOSE FOOD: ")
print("1. BREAKFAST - Rs. 300")
print("2. LUNCH - Rs. 500")
print("3. DINNER - Rs. 500")
print("4. ALL MEALS - Rs. 1100")
print("5. NO FOOD")

food=input("ENTER YOUR CHOICE: ")

while food=="" or not food.isdigit() or int(food)<1 or int(food)>5:
  print("INVALID CHOICE! PLEASE CHOOSE 1,2,3,4 OR 5.")
  food=input("ENTER YOUR CHOICE: ")

food=int(food)

if food==1:
  food_price=300
elif food==2:
  food_price=500
elif food==3:
  food_price=500
elif food==4:
  food_price=1100
else:
  food_price=0

food_total=food_price*nights


print("\nCHOOSE SPA SERVICE: ")
print("1. HEAD MASSAGE - Rs. 500")
print("2. BODY SPA - Rs. 1000")
print("3. FULL SPA - Rs. 1500")
print("4. NO SPA")

spa=input("ENTER YOUR CHOICE: ")

while spa=="" or not spa.isdigit() or int(spa)<1 or int(spa)>4:
  print("INVALID CHOICE! PLEASE CHOOSE 1,2,3 OR 4.")
  spa=input("ENTER YOUR CHOICE: ")

spa=int(spa)

if spa==1:
  spa_price=500
elif spa==2:
  spa_price=1000
elif spa==3:
  spa_price=1500
else:
  spa_price=0

spa_total=spa_price


subtotal=room_total+food_total+spa_total
gst=subtotal*18/100
total=subtotal+gst


print("\nHOTEL BILL")
print("GRAND HOTEL")
print("\nCUSTOMER NAME: ",name)
print("PHONE NUMBER: ",phone)
print("ROOM CHARGES: Rs",room_total)
print("FOOD CHARGES: Rs",food_total)
print("SPA CHARGES: Rs",spa_total)
print("SUBTOTAL: Rs.",subtotal)
print("GST(18%): Rs",gst)

print("\nTOTAL PAYMENT: Rs",total)

print("\nTHANK YOU FOR VISITING GRAND HOTEL!")
print("HAVE A NICE DAY!")
