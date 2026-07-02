Electoral_Party = ["BJP" , "Congress" , "TMC" , "SAPA" , "DMK" , "AAP"]
voter_name = input("Enter Your Name : ")
voter_age = int(input("Enter Your Age : "))
voter_gender = input("Enter Your Gender : ")
if voter_age >= 18 :
    print("You are Eligible for Voting. You can Vote : ")
    for i in range(len(Electoral_Party)):
        print(f"Press {i+1} for Vote {Electoral_Party[i]}")
    while True :
        vote = int(input("Enter Your Vote : "))
        if vote == 1 :
            print(f"{Electoral_Party[0]} Won the Election")
            break
        elif vote == 2 :
            print(f"{Electoral_Party[1]} Won the Election")
            break
        elif vote == 3 :
            print(f"{Electoral_Party[2]} Won the Election")
            break
        elif vote == 4 :
            print(f"{Electoral_Party[3]} Won the Election")
            break
        elif vote == 5 :
            print(f"{Electoral_Party[4]} Won the Election")
            break
        elif vote == 6 :
            print(f"{Electoral_Party[5]} Won the Election")
            break
        else :
            print("Your Input is Wrong...Please Try Again !!!")
else :
    print("You are not Eligible for voting")
    


