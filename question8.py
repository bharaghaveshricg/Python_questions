 You are using Python
num=int(input())
month=input()
if(month=="March" and (num>21 and num<=31)) or (month=="April" and (num>=1 and num<=19)):
    print("Your zodiac sign is Aries")
elif(month=="April" and (num>20 and num<=30)) or (month=="May" and (num>=1 and num<=20)):
    print("Your zodiac sign is Taurus")
elif(month=="May" and (num>21 and num<=31)) or (month=="June" and (num>=1 and num<=20)):
    print("Your zodiac sign is Gemini")
elif(month=="June" and (num>=21 and num<=30)) or (month=="July" and (num>=1 and num<=22)):
    print("Your zodiac sign is Cancer")
elif(month=="July" and (num>=23 and num<=31)) or (month=="August" and (num>=1 and num<=22)):
    print("Your zodiac sign is Leo")
else:
    print("Your zodiac sign is Other")
