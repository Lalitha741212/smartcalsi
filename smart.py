import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(StringValue):
    engine.say(StringValue)
    engine.runAndWait()
def takeCommand():
    print("hello welcom to smart calculator")
    speak("hello welcome to smart calculator")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listeing.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognize...")
            query = r.recognize_google(audio, language= 'en-in')
            print(f"your command :{query}\n")
        #speak(query)
        except Exception as e:
            print("say that agin ple...")
            speak("say that again ple...")
            return "None"
    
    return query
def getCommandValue(StringValue):
    listofcommands = []
    listofvalues = []
    for item in StringValue.split(" "):
        if item.isnumeric():
            listofvalues.append(int(item))
        else:
            listofcommands.append(item)
    return listofcommands , listofvalues
addition = ["sum","add","adding","summation","+","addition","and"]
substraction = ["sub","substraction","-","minus"]
multiplication = ["multiply","multiplication","*","into"]
divison = ["/","divide","devided","div","by"]

def Addition(listofvalues):
    sum1=0
    for i in listofvalues:
        sum1+= i
    return sum1
def Substraction(listofvalues):
    sub1 = 0
    for i in listofvalues:
        sub1-= i
    return sub1
def Multiplication(listofvalues):
    mul1 = 1
    for i in listofvalues:
        mul1 = mul1*i
    return mul1
def Division(listofvalues):
    return listofvalues[0]/listofvalues[1]
op = 'yes'
while op == 'yes':
    Query = takeCommand()
    listofcommand,listofvalues = getCommandValue(Query)
    for command in listofcommand:
        if command.lower() in addition:
            sum1 = Addition(listofvalues)
            print(f"Addition of {listofvalues} is {sum1}")
            speak(f"Addition of {listofvalues} is {sum1}")
            break
        elif command.lower() in substraction:
            sub1 = Substraction(listofvalues)
            print(f"substraction of {listofvalues} is {sub1}")
            speak(f"substraction of {listofvalues} is {sub1}")
            break
        elif command.lower() in multiplication:
            mul1 = Multiplication(listofvalues)
            print(f"multiplication of {listofvalues} is {mul1}")
            speak(f"multiplication of {listofvalues} is {mul1}")
            break
        elif command.lower() in divison:
            div1 = Division(listofvalues)
            print(f"division of {listofvalues} is {div1}")
            speak(f"division of {listofvalues} is {div1}")
            break
        else:
            pass
    else:
        print("we cant find any command")
        speak("we cant find any command ")

    speak("do want continue : yes or no")
    print("do want continue:yes or no")
    op = takeCommand().lower()

print("thanks")
print("do you want continue")
#op = takecommand().lower()

    
    

    
    
