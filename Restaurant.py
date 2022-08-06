import random
print("Welcome to star restaurant")
name = input("Enter your name:")
while True:
      try:
           numb = int(input("Enter your phone number:"))
      except ValueError:
          print("please enter a valid choice from 0 to 3 ")
          continue

      if numb<6000000000 :
         print("please enter a valid choice")
      elif numb>9999999999:
         print("please enter a valid choice")
         continue
      else:
         break
print(" ")
choice = 1
toto = 0
toti = 0
totu = 0 
toty = 0 
tott = 0
totq = 0
final = 0
while choice>0:
  print("Press 1 for ordering starters:")
  print("Press 2 for ordering Main coarse:")
  print("Press 3 for ordering Deserts and Drinks:")
  print("Press 0 If Finished ordering:")
  print(" ")
  while True:
      try:
           choice = int(input("Enter your choice:"))
      except ValueError:
          print("please enter a valid choice from 0 to 3 ")
          continue

      if choice<0 :
         print("please enter a valid choice")
      elif choice>3:
         print("please enter a valid choice")
         continue
      else:
         break
  if choice==1:
    print("Press 1 for veg starters ")
    print("Press 2 for non veg starters ")
    print("Press 0 to go back:")
    print(" ")
    c1 = 1
    while c1>0:
     while True:
       try:
           c1 = int(input("Enter your choice:"))
       except ValueError:
           print("please enter a valid choice from 0 to 3 ")
           continue 

       if c1<0 :
         print("please enter a valid choice")
       elif c1>2:
         print("please enter a valid choice")
         continue
       else:
         break
     if c1==1:
       print("Item:                              price:")
       print("1)Paneer tikka                     ₹110")
       print("2)Veg kebab                        ₹110")
       print("3)Paneer kebab                     ₹110")
       print("4)Spring roll                      ₹130")
       print("5)Gobi Manchurian                  ₹130")
       print("6)Smoked mushroom                  ₹130")
       print("7)Veg momos                        ₹130") 
       print("8)Corn Chana Chat                  ₹150")
       print("9)Mixed Vegetable cutlet           ₹150")
       print("10)Veg lollipop                    ₹150")
       print("0 to go back to main menu")
       print(" ")
       oc = 0
       vs = 1
       amt = 0
       t1 = 0
       while vs>0:
         while True:
           try:
               vs = int(input("Enter your choice by entering the number:"))
           except ValueError:
               print("please enter a valid choice from 0 to 10 ")
               continue
           if vs<0 :
             print("please enter a valid choice")
           elif vs>10:
             print("please enter a valid choice")
             continue
           else:
             break
         if vs>=1 and vs<=3:
           oc = 110
         elif vs>=4 and vs<=7:
          oc = 130
         elif vs>7 and vs<=10:
          oc = 150
         elif vs==0:
          break

         while True:
           try:
               qty = int(input("Enter the quantity :"))
               print(" ")
           except ValueError:
               print("please enter a valid choice ")
               continue
           if qty<0 :
              print("please enter a valid choice")
              continue
           else:
             break
         amt = oc*qty
         t1 = t1+amt
       print(" ")
       f = t1
       toto = f+toto
       if vs==0:
         break
     elif c1==2:
       print("Item:                              price:")
       print("1)Chicken tikka                    ₹160")
       print("2)Chicken chilli kebab             ₹160")
       print("3)Mutton kebab                     ₹160")
       print("4)Drums of Heaven                  ₹180")
       print("5)Garlic Chicken                   ₹180")
       print("6)Smoked Chicken                   ₹180")
       print("7)Chicken fried momos              ₹180") 
       print("8)Garlic Prawns                    ₹200")
       print("9)Mughlai Mutton                   ₹200")
       print("10)Apollo Fish                     ₹200")
       print("0 to go back to main menu")
       print(" ")
       oc2 = 0
       nvs = 1
       amt2 = 0
       t2 = 0
       while nvs>0:
         while True:
           try:
               nvs = int(input("Enter your choice by entering the number:"))
           except ValueError:
               print("please enter a valid choice from 0 to 10 ")
               continue
           if nvs<0 :
              print("please enter a valid choice")
           elif nvs>10:
             print("please enter a valid choice")
             continue
           else:
             break
         if nvs>=1 and nvs<=3:
           oc2 = 160
         elif nvs>=4 and nvs<=7:
          oc2 = 180
         elif nvs>7 and nvs<=10:
          oc2 = 200
         elif nvs==0:
          break

         while True:
           try:
               qty2 = int(input("Enter the quantity :"))
               print(" ")
           except ValueError:
               print("please enter a valid choice ")
               continue
           if qty2<0 :
              print("please enter a valid choice")
              continue
           else:
             break
         amt2 = oc2*qty2
         t2 = t2+amt2
       print(" ")
       f2 = t2
       toti = f2+toti
       if nvs==0:
         break
     elif c1==0:
       break
  elif choice==2:
     print("Press 1 for veg main course ")
     print("Press 2 for non veg main course ")
     print("Press 0 to go back:")
     print(" ")
     c2 = 1
     while True:
       try:
           c2 = int(input("Enter your choice:"))
       except ValueError:
           print("please enter a valid choice from 0 to 3 ")
           continue

       if c2<0 :
         print("please enter a valid choice")
       elif c2>2:
         print("please enter a valid choice")
         continue
       else:
         break
     while c2>0:
      if c2==1:
        print("Item:                              price:")
        print("1)Paneer fried rice                ₹150")
        print("2)Veg biryani                      ₹150")
        print("3)Paneer noodles                   ₹150")
        print("4)Veg fried rice                   ₹170")
        print("5)Mushroom noodles                 ₹170")
        print("6)mushroom fried rice              ₹170")
        print("7)Veg hakka noodles                ₹190") 
        print("8)Kashmiri veg biryani             ₹190")
        print("9)Vegetable schezwan noodles       ₹190")
        print("10)Curd rice                       ₹100")
        print("0 to go back to main menu")
        print(" ")
        oc3 = 0
        vm = 1
        amt3 = 0
        t3 = 0
        while vm>0:
          while True:
            try:
                vm = int(input("Enter your choice by entering the number:"))
            except ValueError:
                print("please enter a valid choice from 0 to 10 ")
                continue
            if vm<0 :
              print("please enter a valid choice")
            elif vm>10:
              print("please enter a valid choice")
              continue
            else:
              break
          if vm>=1 and vm<=3:
            oc3 = 150
          elif vm>=4 and vm<=7:
           oc3 = 170
          elif vm>7 and vm<10:
           oc3 = 190
          elif vm==10:
           oc3 = 100
          elif vm==0:
           break

          while True:
            try:
                qty3 = int(input("Enter the quantity :"))
                print(" ")
            except ValueError:
                print("please enter a valid choice ")
                continue
            if qty3<0 :
               print("please enter a valid choice")
               continue
            else:
              break
          amt3 = oc3*qty3
          t3 = t3+amt3
        print(" ")
        f3 = t3
        totu = f3+totu
        if vm==0:
          break
      elif c2==2:
        print("Item:                              price:")
        print("1)Chicken Noodles                  ₹180")
        print("2)Egg Noodles                      ₹180")
        print("3)Egg fried rice                   ₹180")
        print("4)Chicken Biryani                  ₹210")
        print("5)Chicken lollipop Biryani         ₹210")
        print("6)Special Chicken Biryani          ₹220")
        print("7)Fish Biryani                     ₹240")
        print("8)Prawn Biryani                    ₹240") 
        print("9)Mutton Biryani                   ₹260")
        print("10)Kheema Biryani                  ₹280")
        print("0 to go back to main menu")
        print(" ")
        oc4 = 0
        nvm = 1
        amt4 = 0
        t4 = 0
        while nvm>0:
          while True:
            try:
                nvm = int(input("Enter your choice by entering the number:"))
            except ValueError:
                print("please enter a valid choice from 0 to 10 ")
                continue
            if nvm<0 :
              print("please enter a valid choice")
            elif nvm>10:
              print("please enter a valid choice")
              continue
            else:
              break
          if nvm>=1 and nvm<=3:
            oc4 = 180
          elif nvm>=4 and nvm<=5:
           oc4 = 210
          elif nvm==6:
           oc4 = 220
          elif nvm>=7 and nvm<=8:
            oc4 = 240
          elif nvm==9:
            oc4 = 260
          elif nvm==10:
            oc4 = 280
          elif nvm==0:
           break

          while True:
            try:
                qty4 = int(input("Enter the quantity :"))
                print(" ")
            except ValueError:
                print("please enter a valid choice ")
                continue
            if qty4<0 :
               print("please enter a valid choice")
               continue
            else:
              break
          amt4 = oc4*qty4
          t4 = t4+amt4
        print(" ")
        f4 = t4
        toty = f4+toty
        if nvm==0:
          break
  elif choice==3:
    print("Press 1 for deserts ")
    print("Press 2 for drinks ")
    print("Press 0 to go back:")
    print(" ")
    c3 = 1
    while True:
       try:
           c3 = int(input("Enter your choice:"))
       except ValueError:
           print("please enter a valid choice from 0 to 3 ")
           continue

       if c3<0 :
         print("please enter a valid choice")
       elif c3>2:
         print("please enter a valid choice")
         continue
       else:
         break
    while c3>0:
      if c3==1:
       print("Item:                              price:")
       print("1)Vanilla ice cream                ₹70")
       print("2)Double choclate ice cream        ₹70")
       print("3)Special Mango Ice cream          ₹90")
       print("4)Red velvet cake                  ₹100")
       print("5)Choco lava cake                  ₹100")
       print("6)Special ice cream                ₹120")
       print("7)Mughal kheer                     ₹120")
       print("8)Apple pie                        ₹120") 
       print("9)Toffee pudding                   ₹140")
       print("10)Choclate fudge sandae           ₹140") 
       print("0 to go back to main menu")
       print(" ")
       oc5 = 0
       d1 = 1
       amt5 = 0
       t5 = 0
       while d1>0:
         while True:
           try:
               d1 = int(input("Enter your choice by entering the number:"))
           except ValueError:
               print("please enter a valid choice from 0 to 10 ")
               continue
           if d1<0 :
             print("please enter a valid choice")
           elif d1>10:
             print("please enter a valid choice")
             continue
           else:
             break
         if d1==1 or d1==2:
           oc5 = 70
         elif d1==3:
          oc5 = 90
         elif d1==4 or d1==5:
          oc5 = 100
         elif d1>=6 and d1<=8:
          oc5 = 120
         elif d1==9 or d1==10:
           oc5 = 140
         elif d1==0:
          break

         while True:
           try:
               qty5 = int(input("Enter the quantity :"))
               print(" ")
           except ValueError:
               print("please enter a valid choice ")
               continue
           if qty5<0 :
              print("please enter a valid choice")
              continue
           else:
             break
         amt5 = oc5*qty5
         t5 = t5+amt5
       print(" ")
       f5 = t5
       tott = f5+tott
       if d1==0:
         break
      elif c3==2:
        print("Item:                              price:")
        print("1)sprite                           ₹40")
        print("2)fanta                            ₹40")
        print("3)coke                             ₹40")
        print("4)sweet lime soda                  ₹40")
        print("5)vanilla milkshake                ₹60")
        print("6)chocolate milkshake              ₹60")
        print("7)strawberry milkshake             ₹60")
        print("8)Butterscotch milkshake           ₹60") 
        print("9)coffee                           ₹20")
        print("10)tea                             ₹20") 
        print("0 to go back to main menu")
        print(" ")
        oc6 = 0
        d2 = 1
        amt6 = 0
        t6 = 0
        while d2>0:
          while True:
            try:
                d2 = int(input("Enter your choice by entering the number:"))
            except ValueError:
                print("please enter a valid choice from 0 to 10 ")
                continue
            if d2<0 :
              print("please enter a valid choice")
            elif d2>10:
              print("please enter a valid choice")
              continue
            else:
              break
          if d2>=1 and d2<=4:
            oc6 = 40
          elif d2>=5 and d2<=8:
           oc6 = 60
          elif d2==9 or d2==10:
           oc6 = 20
          elif d2==0:
           break

          while True:
            try:
                qty6 = int(input("Enter the quantity :"))
                print(" ")
            except ValueError:
                print("please enter a valid choice ")
                continue
            if qty6<0 :
               print("please enter a valid choice")
               continue
            else:
              break
          amt6 = oc6*qty6
          t6 = t6+amt6
        print(" ")
        f6 = t6
        totq = f6+totq
        if d2==0:
          break
  if choice==0:
    final = toto+toti+totu+toty+tott+totq
    print("Name:",name)
    print("Phone Number:",numb)
    print(" ")
    print("Amount:",final)
    print('GST= ',18/100*final)
    print('Service Tax=',6/100*final)
    print('VAT=',14/100*final)
    print('Total=',(18/100*final)+(6/100*final)+(14/100*final)+final)
    print("")
    print("Your token for food:",random.randrange(1,100))
    print("Do not forget to collect the bill")
    print("Visit Us Again")
    print("Feel free to send us your reviews at star.restaraunt@gmail.com")
    print("Thank you")
