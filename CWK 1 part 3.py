# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: UoW - w1867441, IIT - 20210324 
# Date: 2021/ 12/ 01
Pass = 0
defer = 0
fail = 0
total = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
list_1 = 0
list_2 = 0
list_3 = 0
list_4 = 0
list_1 = []
list_2 = []
list_3 = []
list_4 = []
total_count = 0
while True:
  outcome = str(input("""Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view result: """))
  outcome = outcome.lower()
  if (outcome == 'y'):
      try:
        Pass = int(input("Enter your total PASS credits:  "))
        if Pass >= 0 and Pass <= 120:
            if Pass % 20 != 0:
                print("Out of range displayed.")
                continue
            defer = int(input("Enter your total DEFER credits: "))
            if defer >= 0 and defer <= 120:
                if defer % 20 != 0:
                    print("Out of range displayed.")
                    continue
                fail = int(input("Enter your total FAIL credits:  "))
                if fail >= 0 and fail <= 120:
                    if fail % 20 != 0:
                       print("Out of range displayed.")
                       continue
                    total = Pass + defer + fail
                    if total == 120:
                            if(Pass == 120):
                                count_1 = count_1 + 1
                                progress = [Pass, defer , fail]
                                list_1.append(progress)
                                print("Progress.")
                                continue
                            elif(Pass == 100):
                                trailer = [Pass, defer , fail]
                                list_2.append(trailer)
                                print("Progress (module trailer)")
                                count_2 = count_2 + 1
                            elif(Pass == 40 and fail == 80) or (Pass == 20 and defer <= 20) or (Pass == 0 and defer <= 40):
                                exclude = [Pass, defer , fail]
                                list_4.append(exclude)
                                print("Exclude")
                                count_4 = count_4 + 1
                                
                            else:
                                retriever = [Pass, defer , fail]
                                list_3.append(retriever)
                                print("Module retriever")
                                count_3 = count_3 + 1
                                
                    else:
                        print("Total incorrect.")
            else:
                print("Out of the range.")
        else:
            print("Out of the range.")
      except ValueError:
        print("Integer required.")
        continue
  elif (outcome == 'q'):
      total_count = count_1 + count_2 + count_3 + count_4
      print("-------------------------------------------------")
      print("Horizontal Histogram")
      print("Progress  "+ str(count_1), " :",count_1 * '*')
      print("Trailer   "+ str(count_2) ," :",count_2 * '*')
      print("Retriever "+ str(count_3), " :",count_3 * '*')
      print("Excluded  "+ str(count_4), " :",count_4 * '*')
      print(total_count,"outcomes in total.")
      print("-------------------------------------------------")

      print("Vertical Histrogram")
      header =['   Progress   |', '   Trailer   |', '   Retriever   |', '   Exclude']
      print(''.join(header))
      for p in range(max(count_1, count_2, count_3, count_4)):
          print(" {0:>6} {1:>14} {2:>14} {3:>15}".format(
              '*' if p < count_1 else'',
              '*' if p < count_2 else'',
              '*' if p < count_3 else'',
              '*' if p < count_4 else'',
              ))
      print("-------------------------------------------------")
      for p in list_1:
              print("Progress  :",p)
      for q in list_2:
              print("Trailer   :",q)
      for r in list_3:
              print("Retriever :",r)
      for s in list_4:
              print("Exclude   :",s)
      break
  else:
        print("This string not valid! try again")
        continue
#reference
#lecture notes
