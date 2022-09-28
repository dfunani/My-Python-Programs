import sys
import os
import calendar
from datetime import datetime
from pyinputplus import inputNum
from static import MONTHS, DAYS, DAYS2
from tkinter import *
from tkinter import messagebox
import shelve

def Main():
    Month = datetime.now().month
    Year = datetime.now().year
 
    if len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
        Year = int(sys.argv[1])
        Month = int(sys.argv[2])
    
    if len(sys.argv) != 3:
        Year = inputNum("Enter the year for the calendar:\n>")
        Month = inputNum(prompt="Enter the month for the calendar, 1-12:\n>", max=12, min=1)
    
    calendarList = calendar.monthcalendar(Year, Month)
    return calendarList, Year, Month

def CreateMonth(calendars, month, year):
    header = f'''{MONTHS[month - 1]} {year}'''.center(80)
    
    temp = calendars[0].count(0)
    for i, value in enumerate(range(calendars[0].count(0)), 1):
        tempY, tempM = (year - 1, 12) if month == 1 else (year, month)
        tempList = [*calendarList[-2],*[val for val in calendar.monthcalendar(tempY, tempM)[-1] if val != 0]]
        calendars[0][i-1] = tempList[-(temp + 1 - i)]
        
    temp = calendars[-1].count(0)
    for i, value in enumerate(range(calendars[-1].count(0)), 1):
        calendars[-1][-(temp + 1 - i)] = i
    
    body = []
    for day in range(7):
        if day % 2 == 0:
        	Days = [f'''{"." * round(((12-len(DAYS[day]))/2))}{DAYS[day].center(len(DAYS[day]))}{"." * round(((12-len(DAYS[day]))/2))}''',
        f'''+-----------+''']
        else:
            Days = [f'''{"." * round(((12-len(DAYS[day]))/2))}{DAYS[day].center(len(DAYS[day]))}{"." * round(((12-len(DAYS[day]))/2))}''',
        f'''-----------''']
        for week in range(len(calendars)):
            with shelve.open("events") as EVENTS:
                events = EVENTS.get(str(year), {}).get(str(month), {}).get(str(calendars[week][day]), {})
                Days = CreateDay(Days, day, calendars[week][day], events)
        body.append(Days)
    newBody = []
    for col in range(len(body[0])):
        temp = ''
        for row in range(len(body)):
            temp += body[row][col]
        newBody.append(temp)
    newBody = "\n".join(newBody)
    return f'''{header}
{newBody}'''

def CreateDay(days, i, day, events):
    a = str(len(events)).center(2) + " " if len(events) != 0 else '   '
    
    if i % 2 == 0:
    	return [*days, f'''|{str(day).ljust(2)}         |''',
f'''|           |''',
f'''|    {a}    |''',
f'''|           |''',
f'''+-----------+''']
    else:
        return [*days, f'''{str(day).ljust(2)}         ''',
f'''           ''',
f'''     {a}   ''',
f'''           ''',
f'''-----------''']

if __name__ == '__main__':
	calendarList, Year, Month = Main()
	print(CreateMonth(calendarList, Month, Year))
	calendarList = calendar.monthcalendar(Year, Month)
	while True:
		window = Tk()
		window.wm_title("My Calendar")
		window.geometry("1920x1080+0+0")
		def YearSetter(options):
			global calendarList
			global Month
			global Year
			options = varListY.get()
			Year = int(options)
			calendarList = calendar.monthcalendar(Year, Month)
			window.destroy()

		def MonthSetter(options):
			global calendarList
			global Month
			global Year
			options = varListM.get()
			Month = options
			Month = MONTHS.index(Month) + 1
			calendarList = calendar.monthcalendar(Year, Month)
			window.destroy()
   
		def restart_program():
			"""Restarts the current program.
			Note: this function does not return. Any cleanup action (like
			saving data) must be done before calling this function."""
			python = sys.executable
			os.execl(python, python, * sys.argv)
   
		def AddEvent():
			global monthEntry
			global yearEntry 
			global dayEntry
			global keyEntry
			global eventEntry

			y = yearEntry.get()
			m = monthEntry.get()
			d = dayEntry.get()
			k = keyEntry.get()
			e = eventEntry.get()

			with shelve.open('events', flag='w', writeback=True) as EVENTS:
				EVENTS.setdefault(str(y), {str(m): {str(d): {}}})
				EVENTS[str(y)].setdefault(str(m), {str(d): {}})
				EVENTS[str(y)][str(m)].setdefault(str(d), {})
				temp = EVENTS[str(y)][str(m)][str(d)]
				temp.update({k: e})
				EVENTS[str(y)][str(m)][str(d)] = temp
				 
		frame = Frame(window)
		frame.pack()
		
		button = Button(frame, text='Refresh', command=restart_program, border=0, anchor='w', width=20)
		button.config( font=("Comic Sans MS", 15, "bold"))
		button.pack(side=LEFT, expand=1, fill=X)
		
		varListM = StringVar(frame)
		varListM.set(MONTHS[Month - 1])
		menu = OptionMenu(frame, varListM, *MONTHS, command=MonthSetter)
		menu.config(font=("Comic Sans MS", 15, "bold"), border=0)
		menu.pack(side=LEFT, expand=1, fill=X)
  
		varListY = StringVar(frame)
		varListY.set(Year)
		
		menu = OptionMenu(frame, varListY, *range(datetime.now().year + 50, 1970, -1), command=YearSetter)
		menu.config(font=("Comic Sans MS", 15, "bold"), border=0)
		menu.pack(side=LEFT, expand=1, fill=X)
  
		label = Label(frame, text="                Year")
		label.config(font=("Comic Sans MS", 15, "bold"), border=0)
		label.pack(side=LEFT, expand=1, fill=X)
		varInt = IntVar(frame)
		varInt.set(Year)
		yearEntry = Entry(frame, width=10, textvariable=varInt)
		yearEntry.focus_set()
		yearEntry.pack(side=LEFT, expand=1, fill=X)
  
		label = Label(frame, text=" Month")
		label.config(font=("Comic Sans MS", 15, "bold"), border=0)
		label.pack(side=LEFT, expand=1, fill=X)
		varInt = IntVar(frame)
		varInt.set(Month)
		monthEntry = Entry(frame, width=10, textvariable=varInt)
		monthEntry.focus_set()
		monthEntry.pack(side=LEFT, expand=1, fill=X)

		label = Label(frame, text=" Day")
		label.config(font=("Comic Sans MS", 15, "bold"), border=0)
		label.pack(side=LEFT, expand=1, fill=X)
		varInt = IntVar(frame)
		varInt.set(1)
		dayEntry = Entry(frame, width=10, textvariable=varInt)
		dayEntry.focus_set()
		dayEntry.pack(side=LEFT, expand=1, fill=X)
  
		label = Label(frame, text=" Key")
		label.config(font=("Comic Sans MS", 15, "bold"), border=0)
		label.pack(side=LEFT, expand=1, fill=X)
		varInt = IntVar(frame)
		varInt.set("Example_No_Spaces")
		keyEntry = Entry(frame, width=10, textvariable=varInt)
		keyEntry.focus_set()
		keyEntry.pack(side=LEFT, expand=1, fill=X)
  
		label = Label(frame, text=" Event")
		label.config(font=("Comic Sans MS", 15, "bold"), border=0)
		label.pack(side=LEFT, expand=1, fill=X)
		varInt = IntVar(frame)
		varInt.set("Description...")
		eventEntry = Entry(frame, width=10, textvariable=varInt)
		eventEntry.focus_set()
		eventEntry.pack(side=LEFT, expand=1, fill=X)

		button = Button(frame, text='Add Event', command=AddEvent)
		button.config(width=10)
		button.pack(side=LEFT, expand=1, fill=X)
		frame = Frame(window)
		frame.pack(fill=BOTH)
		for day in range(7):
			var = Text(frame, width=15, height=1)
			var.tag_configure("center", justify='center')
			var.config(bg='black', fg='white', font=("Comic Sans MS", 15, "bold"))
			var.pack(side=LEFT, expand=1, fill=X)
			var.insert(END,DAYS2[day])
   
		temp = calendarList[0].count(0)
		tempY, tempM = (Year - 1, 12) if Month == 1 else (Year, Month-1)	
		for i, value in enumerate(range(calendarList[0].count(0)), 1):
			tempList = [*calendarList[-2], *[val for val in calendar.monthcalendar(tempY, tempM)[-1] if val != 0]]
			calendarList[0][i-1] = str(tempList[-(temp + 1 - i)]) + str(MONTHS[tempM-1][0])
		temp = calendarList[-1].count(0)
		tempY, tempM = (Year + 1, 1) if Month == 12 else (Year, Month+1)
		for i, value in enumerate(range(calendarList[-1].count(0)), 1):
			calendarList[-1][-(temp + 1 - i)] = str(i) + str(MONTHS[tempM-1][0])
   
		for week in calendarList:
			frame = Frame(window)
			frame.pack(expand=1, fill=BOTH)
			for day in week:
				var = Text(frame, width=15, height=3)
				
				with shelve.open('events') as EVENTS:
					eventsList = EVENTS.get(str(Year), {}).get(str(Month), {}).get(str(day), {}).items()
					if eventsList:
						var.config(bg='gray', fg='red', font=("Comic Sans MS", 15, "bold"))
						var.pack(side=LEFT, expand=1, fill=BOTH)
						var.insert(END, str(day) +'\n'+ "\n".join([f"{key.upper()}: {value}" for key, value in eventsList]))
					else:
						var.config(bg='gray', fg='black', font=("Comic Sans MS", 15, "bold"))
						var.pack(side=LEFT, expand=1, fill=BOTH)
						var.insert(END, str(day) +'\n'+ "\n".join([f"{key.upper()}: {value}" for key, value in eventsList]))
		def on_closing():
			if messagebox.askokcancel("Quit", "Do you want to quit?"):
				window.destroy()
				sys.exit()

		
		window.protocol("WM_DELETE_WINDOW", on_closing)
		window.mainloop()
     