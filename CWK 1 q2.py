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
                                print("Progress.")
                                count_1 = count_1 + 1
                            elif(Pass == 100):
                                print("Progress (module trailer)")
                                count_2 = count_2 + 1
                            elif(Pass == 40 and fail == 80) or (Pass == 20 and defer <= 20) or (Pass == 0 and defer <= 40):
                                print("Exclude")
                                count_4 = count_4 + 1
                                
                            else:
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
      break
  else:
        print("This string not valid! try again")
        continue
#reference
# lecture notes
