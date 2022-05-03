play_status=input("Do you want to play? ")
if play_status.upper() != "YES":
    quit()
while True:
  print("Welcome to the Capital Quiz!\n")
  print("Let's play!\nYou have maximum 2 chances to answer a question.")
  score=0
  number_of_chances=2
  data={"russia":"moscow","india":"delhi","china":"beijing","japan":"tokyo","canada":"ottawa"}
 
  for country in data:
    for i in range(0,number_of_chances):
      
      answer=input(f"What is the capital of {country.upper()}?").lower()
      if answer==data[country].lower():
        print("Correct!")
        score+=1
        break
      else:
        print("Oops! That is wrong .")
        if i==number_of_chances-1:
          break
        answer_again=int(input("Press 1 if you want to answer again and 0 for next question."))
        if answer_again==0:
          break

  print("\nYou completed the quiz.\n\nYou scored ",score,"out of ",len(data),"!")
  play_again=input("\nPress 1 if you want to play again and 0 to exit.")
  if play_again==str(1):
    continue
  else :
    print("Goodbye!")
    break

    