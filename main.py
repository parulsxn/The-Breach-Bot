#Breach Bot Starter Code
breachYear = 2017

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("\nNice to meet you " + userName + "\n")

#Recounts start of dreach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("\nWow! That means it has been " + str(timePassed) + " years since the National Health Services data breach in " + str(breachYear)+"!\n")

#Introduces breach
print("Would you like to learn about the National Health Services Breach in 2017?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    #breach deets
    print("\nHackers utilized the public access to EternalBlue by Microsoft and the ransomware WannaDecryptor to break into hospital systems in the UK. 16 hospitals were affected and patients were forced to pay $300 bitcoin in order to access their information again.\n")
  
  elif topic.lower() == "b":
    #organization's response
    print("\nThe National Health Society said that they dealt with the problem as fast as they could and that no patient data was compromised. The FBI informally recommended paying the $300 ransom in order to decrypt the files, an ethically controversial suggestion.\n")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("\nWhat would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad, (b) my reaction, (c) my advice or (d) none")
  topic = input()

  if topic.lower() == "a":
    #breach deets
    print("\nThis relates to confidentiality since the hackers had open source access to Microsoft’s EternalBlue security system. Due to this they were able to crack down its security and hack people’s medical data.\n")

  elif topic.lower() == "b":
    #organization's response
    print("\nI disagree with the organization’s response since they responded to it promptly saying that their clients’ data is not compromised. Additionally, they do not provide any closure as to how these hospitals would be dealing with the issue after the fact.\n")

  elif topic.lower() == "c":
    print("\nI would convince victims to take action by telling them to keep a copy of their medical records with themselves so that if a medical system goes down they will still have their own data.My advice would be to store these medical files on a secure cloud storage so that in the case that their personal devices get hacked they still have access to their records.\n")

  elif topic.lower() == "d":
    break

  else:
    print("\nSorry, I didn't catch that. Choose one of the options listed.")

  input("Press enter to continue\n")

#Chatbot ends conversation
print("\nThanks for chatting with me, and I hope you learned something new!")