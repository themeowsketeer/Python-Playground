import speech_recognition
import pyttsx3

ear=speech_recognition.Recognizer()
mouth=pyttsx3.init()
while True:
	with speech_recognition.Microphone() as Microphone:
		print("I'm listening")
		ear.adjust_for_ambient_noise(Microphone, duration=1)
		ear.pause_threshold = 0.5
		audio=ear.listen(Microphone)
	try:
		you = ear.recognize_google(audio)
	except:
		you=""
	if "hello" in you:
		brain="hello Duy Handsome"
	elif you=="":
		brain="I can't hear you"
	elif"bye" in you:
		brain="bye"
		mouth.say(bye)
		mouth.runAndWait()
		print(brain)
		break
	elif"You're gay" in you:
		brain="fuck you"
		mouth.say(brain)
	else:
		brain="How are you today ?"
	mouth.say(brain)
	mouth.runAndWait()
	print("You:",you)
	print(brain)