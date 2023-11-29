import speech_recognition as sr
import smtplib
import pyttsx3

engine = pyttsx3.init()
	
recognizer=sr.Recognizer()

with sr.Microphone() as source:
    print('Clearing background bnoise..')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    engine.say("waiting for Your message")
    engine.runAndWait()
    print("waiting for Your message...")
    recordedaudio=recognizer.listen(source)
    print('Done recording..!')
    engine.say("Done recording")
    engine.runAndWait()
try:
    print('Printing the message')
    text=recognizer.recognize_google(recordedaudio,language='en-in')
    print('Your message:{}'.format(text))
    engine.say(text)
    engine.runAndWait()

except Exception as ex:
    print(ex)


s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("balajiraghu159002@gmail.com", "orwihmtuzhutnina")

# message to be sent
message = text

# sending the mail
s.sendmail("balajiraghu159002@gmail.com", "balaji159002@gmail.com", message)
print("Sent successfully")

# terminating the session
s.quit()
