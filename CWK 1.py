# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: UoW - w1867441, IIT - 20210324 
# Date: 2021/ 12/ 01
Pass = 0
defer = 0
fail = 0
total = 0
while True:
  
    try:
        Pass = int(input("Please enter your credit at pass: "))
        if Pass >= 0 and Pass <= 120:
            if Pass % 20 != 0:
                print("Out of range displayed.")
                continue
            defer = int(input("Please enter your credit at defer: "))
            if defer >= 0 and defer <= 120:
                if defer % 20 != 0:
                    print("Out of range displayed.")
                    continue
                fail = int(input("Please enter your credit at fail: "))
                if fail >= 0 and fail <= 120:
                    if fail % 20 != 0:
                       print("Out of range displayed.")
                       continue
                    total = Pass + defer + fail
                    if total == 120:
                            if(Pass == 120):
                                print("Progress.")
                                break
                            elif(Pass == 100):
                                print("Progress (module trailer)")
                                break
                            elif(Pass == 40 and fail == 80) or (Pass == 20 and defer <= 20) or (Pass == 0 and defer <= 40):
                                print("Exclude")
                                break
                            else:
                                print("Do not progress – module retriever")
                                break
                    else:
                        print("Total incorrect.")
            else:
                print("Out of the range.")
        else:
            print("Out of the range.")
    except ValueError:
        print("Integer required.")
#reference
# lecture notes
