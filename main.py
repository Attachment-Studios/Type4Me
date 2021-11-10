# Type4Me

# Prototype Version 2021.11

# libraries
import tkinter
import pyautogui
import time

# globals
global status

# options
default = {
	"wait_time" : 3,
	"type_interval" : 0.05,
	"text" : ""
}
config = {
	"wait_time" : 3,
	"type_interval" : 0.05,
	"text" : ""
}
status = {
	"active" : False,
	"stop" : False,
	"pause" : False
}

# trigger autotype
def trigger():
	config["text"] = text_box.get("1.0", tkinter.END)
	try:
		config["wait_time"] = float(option1.get())
	except:
		config["wait_time"] = default["wait_time"]
	try:
		config["type_interval"] = float(option2.get())
	except:
		config["type_interval"] = default["type_interval"]
	if config["text"] == "":
		return
	else:
		pyautogui.alert("Click OK To Start Countdown For Auto-Typing.", title="Type4Me")
		autotype()

# write
def autotype():
	try:
		conf = config
		time.sleep(conf["wait_time"])
		for character in conf["text"]:
			pyautogui.keyDown(character)
			pyautogui.keyUp(character)
			time.sleep(conf["type_interval"])
		status = {
			"active" : False,
			"stop" : False,
			"pause" : False
		}
		pyautogui.alert("Typing Complete.", title="Type4Me")
	except Exception as error:
		print(f"Error - {error}")

# window
window = tkinter.Tk()
window.title("Type4Me")
window.configure(padx=10, pady=10)
window.resizable(0,0)

main_frame = tkinter.Frame()
main_frame.pack()

labelH = tkinter.Label(main_frame, text="Type4Me - AutoTyper")
labelH.pack()

text_frame = tkinter.Frame(main_frame, padx=10)
text_frame.pack()
conf_frame = tkinter.Frame(main_frame)
conf_frame.pack()
run_frame = tkinter.Frame(main_frame)
run_frame.pack()

label1 = tkinter.Label(text_frame, text="\nText")
text_box = tkinter.Text(text_frame, height=5, width=50)
label2 = tkinter.Label(conf_frame, text="\nOptions")
label2_1 = tkinter.Label(conf_frame, text="Countdown(Seconds)")
option1 = tkinter.Entry(conf_frame)
label2_2 = tkinter.Label(conf_frame, text="Type Interval(Seconds)")
option2 = tkinter.Entry(conf_frame)
label3 = tkinter.Label(run_frame, text="\nRun Program")
run_button = tkinter.Button(run_frame, text="Run", command=trigger)

widgets = [
	label1,
	text_box,
	label2,
	label2_1,
	option1,
	label2_2,
	option2,
	label3,
	run_button
]

for widget in widgets:
	widget.pack()

option1.insert(0, str(config["wait_time"]))
option2.insert(0, str(config["type_interval"]))

window.mainloop()
