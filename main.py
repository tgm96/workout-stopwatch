import time
import sys, os
from tkinter import *
from linked_list import LinkedList
import pygame

row = 0
running = False
cards = LinkedList()

pygame.mixer.init()
path = os.getcwd()

def play_countdown():
	pygame.mixer.music.load(path + "/countdown_beep.mp3")
	pygame.mixer.music.play(loops=0)

def play_start():
	pygame.mixer.music.load(path + "/start_beep.mp3")
	pygame.mixer.music.play(loops=0)

def start():
	global running

	if not running:
		for i in range(3):
			play_countdown()
			time.sleep(1)
		running = True
		play_start()
		run_card()

def run_card():
	global running
	global cards

	if running:
		if cards.size() == 0:
			time.sleep(3)
			sys.exit()
		data = cards.store_index(0)

		if data["time"] == 0:
			cards.remove_index(0)
			update_cards()
			display_cards()
			play_start()
			run_card()
		else:
			test_card = Label(frame, 
				text=str(data["name"]) + "\n \n" + str(data["time"]),
				width=50, 
				height=4,
				bg=data["bg"], 
				anchor="n",
				highlightthickness=2, 
				highlightbackground="black",
				relief=RAISED)

			test_card.grid(row=0, column=3, rowspan=2, padx=1)
			data["time"] -= 1
			cards.remove_index(0)
			cards.add(data)
			test_card.after(1000, run_card)

def update_cards():
	global cards

	for index in range(cards.size()):
		data = cards.store_index(index)
		data["row"] -= 2
		cards.remove_index(index)
		cards.insert(data, index)

def display_cards():
	global cards

	for widget in frame.winfo_children():
		widget.destroy()

	for index in range(cards.size()):
		data = cards.store_index(index)
		test_card = Label(frame, 
			text=str(data["name"]) + "\n \n" + str(data["time"]),
			width=50, 
			height=4,
			bg=data["bg"], 
			anchor="n",
			highlightthickness=2, 
			highlightbackground="black",
			relief=RAISED)

		test_card.grid(row=data["row"], column=3, rowspan=2, padx=1)

def add_card(name, time, row, bg):
    data = {"name": name, "time": time, "row": row, "bg": bg}
    cards.add_last(data)

def stop():
	global running

	if running:
		running = False

def get_action_params():
	global row
	global cards_time
	global cards

	time = action_entry_time.get() 
	name = action_entry_name.get()
	add_card(name, int(time), row, "dark orange")
	display_cards()
	row += 2

def get_break_time():
	global row
	global cards

	time = break_entry.get()
	add_card("Break", int(time), row, "light blue")
	display_cards()
	row += 2


def get_pause_time():
	global row
	global cards

	time = pause_entry.get()
	add_card("Pause", int(time), row, "red")
	display_cards()
	row += 2

def reset():
	global running
	global cards

	running = False

	for widget in frame.winfo_children():
		widget.destroy()

	cards.wipe_list()
	print(cards)


root = Tk()
root.title("WORKOUT ACTION PROGRAM")
root.minsize(900, 600)

action_entry_label = Label(root, text="Enter name of exercise: ", height=2)
action_entry_label.grid(row=0, column=1)
action_entry_name = Entry(root, width=25)
action_entry_name.grid(row=0, column=2)

action_entry_label2 = Label(root, text="Enter time of exercise: ", height=2)
action_entry_label2.grid(row=1, column=1)
action_entry_time = Entry(root, width=25)
action_entry_time.grid(row=1, column=2)

break_entry_label = Label(root, text="Enter time of break: ", height=4)
break_entry_label.grid(row=2, column=1)
break_entry = Entry(root, width=25)
break_entry.grid(row=2, column=2)

pause_entry_label = Label(root, text="Enter time of pause: ", height=4)
pause_entry_label.grid(row=4, column=1)
pause_entry = Entry(root, width=25)
pause_entry.grid(row=4, column=2)

action_button = Button(root, text="ACTION", bd=5, width=10, height=4, command=get_action_params)
action_button.grid(row=0, column=0, rowspan=2)

break_button = Button(root, text="BREAK", bd=5, width=10, height=4, command=get_break_time)
break_button.grid(row=2, column=0, rowspan=2)

pause_button = Button(root, text="PAUSE", bd=5, width=10, height=4, command=get_pause_time)
pause_button.grid(row=4, column=0, rowspan=2)

start_button = Button(root, text="START", bd=5, width=10, height=4, bg="green", command=start)
start_button.grid(row=6, column=0, rowspan=2)

stop_button = Button(root, text="STOP", bd=5, width=10, height=4, bg="red", command=stop)
stop_button.grid(row=8, column=0, rowspan=2)

reset_button = Button(root, text="RESET", bd=5, width=10, height=4, bg="blue", command=reset)
reset_button.grid(row=10, column=0, rowspan=2)

quit_button = Button(root, text="QUIT", bd=5, width=10, height=4, command=root.quit)
quit_button.grid(row=12, column=0, rowspan=2)

frame = Frame(root)
frame.grid(row=0, column=3, rowspan=20)

root.mainloop()
