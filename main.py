# Type4Me

# Prototype Version 2021.11

# libraries
import tkinter
import pyautogui
import time
import threading

# globals
global status
global global_trigger

# pre-defined
global_trigger = ""

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
	global status
	config["text"] = text_box.get("1.0", tkinter.END)[:-1]
	try:
		config["wait_time"] = int(float(option3.get()))
	except:
		config["wait_time"] = default["wait_time"]
	try:
		config["type_interval"] = float(option2.get())
	except:
		config["type_interval"] = default["type_interval"]
		option2.delete(0, tkinter.END)
		option2.insert(0, str(config["type_interval"]))
	if config["text"] in "":
		return
	else:
		if status["active"] == False:
			status = {
				"active" : True,
				"stop" : False,
				"pause" : False
			}
			global run_button
			type_thread = threading.Thread(target=autotype)
			type_thread.start()
			type_thread.join()
		else:
			pass

# write
def autotype():
	try:
		conf = config
		pyautogui.typewrite(conf["text"], interval=conf["type_interval"])
		global status
		status = {
			"active" : False,
			"stop" : False,
			"pause" : False
		}
		pyautogui.alert("Typing Complete.", title="Type4Me")
	except Exception as error:
		print(f"Error - {error}")

# Insert From File
def insert_file():
	from tkinter import ttk, filedialog
	from tkinter.filedialog import askopenfile
	file = tkinter.filedialog.askopenfile(mode="r")
	if file == None:
		pass
	else:
		text_box.insert(tkinter.END, file.read())
		file.close()

# start auto typing
def start_autotype():
	global global_trigger
	global_trigger = "start_autotype"

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
label2_1 = tkinter.Label(conf_frame, text="Insert From File")
browse_button = tkinter.Button(conf_frame, text="Browse File", command=insert_file)
label2_2 = tkinter.Label(conf_frame, text="Type Interval(Seconds)")
option2 = tkinter.Entry(conf_frame)
label2_3 = tkinter.Label(conf_frame, text="Countdown(Seconds)")
option3 = tkinter.Entry(conf_frame)
label3 = tkinter.Label(run_frame, text="\nRun Program")
run_button = tkinter.Button(run_frame, text="Run", command=start_autotype)

widgets = [
	label1,
	text_box,
	label2,
	label2_1,
	browse_button,
	label2_2,
	option2,
	label2_3,
	option3,
	label3,
	run_button
]

for widget in widgets:
	widget.pack()

option2.insert(0, str(config["type_interval"]))
option3.insert(0, str(config["wait_time"]))

def window_close():
	global global_trigger
	global_trigger = "exit"
	
	global window
	window.destroy()

window.protocol("WM_DELETE_WINDOW", window_close)

# event listener
def event_listener():
	while True:
		global global_trigger
		if global_trigger == "":
			pass
		elif global_trigger == "start_autotype":
			global status
			global config
			try:
				config["wait_time"] = int(f'{float(option3.get())}'.split('.')[0])
			except:
				config["wait_time"] = default["wait_time"]
				option3.delete(0, tkinter.END)
				option3.insert(0, str(config["wait_time"]))
			config["text"] = text_box.get("1.0", tkinter.END)[:-1]
			if config["text"] == "":
				pass
			else:
				# pyautogui.alert("Select Where To Type. Once Ready, Click OK To Start Auto-Typing.\n(Minimize Main Window)", title="Type4Me")
				count = config["wait_time"]
				for _ in range(count):
					run_button["text"] = f"{count - _}"
					time.sleep(1)
				run_button["text"] = "Running"
				trigger()
				run_button["text"] = "Run"
			global_trigger = ""
		elif global_trigger == "exit":
			return

event_thread = threading.Thread(target=event_listener)
event_thread.start()

window.mainloop()

