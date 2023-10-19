import tkinter as tk
from tkinter import ttk, filedialog
import gpss

GPSScode = ''

root = tk.Tk()
root.title("GPSS Simulation Tool")
root.geometry("800x600")
tabControl = ttk.Notebook(root)

GPSStab = ttk.Frame(tabControl)
helpTab = ttk.Frame(tabControl)

tabControl.add(GPSStab, text='GPSS model and results')
tabControl.add(helpTab, text='Help')
tabControl.pack(expand=1, fill="both")


def openFile():
    GPSSmodel.delete('1.0', tk.END)
    file = filedialog.askopenfile(mode='r', filetypes=[('GPSS Files', '*.gps')])
    if file:
        content = file.read()
        file.close()
    GPSSmodel.insert(tk.END, content)


def saveToFile():
    global GPSScode
    GPSScode = GPSSmodel.get('1.0', tk.END)
    outputFile = open('model.gps', 'w')
    outputFile.writelines(GPSScode)
    outputFile.close()


def startGPSS():
    resultsFromGPSSTextbox.delete('1.0', tk.END)
    saveToFile()
    try:
        gpss.run("model.gps")
        result = gpss.createReport()
        resultsFromGPSSTextbox.insert(tk.END, result)
    except:
        resultsFromGPSSTextbox.insert(tk.END, "Parser Error!")


def showHelp():
    infoText = ''
    inputFile = open('help.txt', 'r')
    Lines = inputFile.readlines()
    count = 0
    for line in Lines:
        count += 1
        currentLine = line.strip()
        infoText = infoText + currentLine + '\n'
    return infoText


GPSStab.rowconfigure(0, weight=1, minsize=30)
GPSStab.rowconfigure(1, weight=1, minsize=50)
GPSStab.rowconfigure(2, weight=2, minsize=50)
GPSStab.columnconfigure(0, weight=1, minsize=50)
GPSStab.columnconfigure(1, weight=1, minsize=50)

GPSSmodelLabel = tk.Label(GPSStab, text="GPSS model editor", height=5, width=100)
GPSSmodelLabel.grid(row=0, column=0, padx=5, pady=5)
resultsFromGPSSLabel = tk.Label(GPSStab, text="Simulation Results", height=5, width=100)
resultsFromGPSSLabel.grid(row=0, column=1, padx=5, pady=5)
GPSSmodel = tk.Text(GPSStab, height=95, width=100)
GPSSmodel.grid(row=1, column=0, padx=5, pady=5)
resultsFromGPSSTextbox = tk.Text(GPSStab, height=95, width=100)
resultsFromGPSSTextbox.grid(row=1, column=1, padx=5, pady=5)

openFilebtn = ttk.Button(GPSStab, text='Open GPSS file', command=openFile, width=30)
openFilebtn.grid(row=2, column=0, padx=5, pady=5, sticky='w')
saveToFilebtn = ttk.Button(GPSStab, text='Save to file', command=saveToFile, width=30)
saveToFilebtn.grid(row=2, column=0, padx=5, pady=5, sticky='e')
startGPSSbtn = ttk.Button(GPSStab, text='Start GPSS Simulation', command=startGPSS, width=100)
startGPSSbtn.grid(row=2, column=1, padx=5, pady=5)

helpTab.rowconfigure(0, weight=1, minsize=50)
helpTab.columnconfigure(0, weight=1, minsize=50)
infoTextbox = tk.Text(helpTab, height=100, width=100)
infoTextbox.grid(row=0, column=0, padx=5, pady=5, sticky='nw')
infoTextbox.insert(tk.END, showHelp())
infoTextbox.config(state=tk.DISABLED)

root.mainloop()
