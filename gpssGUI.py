import tkinter as tk
from tkinter import ttk, filedialog
import gpss

GPSScode = ''

root = tk.Tk()
root.title("GPSS Simulation Tool")
root.geometry("1024x768")
root.resizable(False, False)
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


openFilebtn = ttk.Button(root, text='Open GPSS file', command=openFile)
openFilebtn.place(x=30, y=720, width=218)
saveToFilebtn = ttk.Button(root, text='Save to file', command=saveToFile)
saveToFilebtn.place(x=278, y=720, width=218)
startGPSSbtn = ttk.Button(root, text='Start GPSS Simulation', command=startGPSS)
startGPSSbtn.place(x=526, y=720, width=466)

GPSSmodelLabel = tk.Label(GPSStab, text="GPSS model editor")
GPSSmodelLabel.place(x=30, y=30, height=30, width=467)
resultsFromGPSSLabel = tk.Label(GPSStab, text="Simulation Results")
resultsFromGPSSLabel.place(x=527, y=30, height=30, width=467)
GPSSmodel = tk.Text(GPSStab)
GPSSmodel.place(x=30, y=90, height=600, width=467)
resultsFromGPSSTextbox = tk.Text(GPSStab)
resultsFromGPSSTextbox.place(x=527, y=90, height=600, width=467)

infoTextbox = tk.Text(helpTab)
infoTextbox.place(x=30, y=30, height=330, width=964)
infoTextbox.insert(tk.END, showHelp())
infoTextbox.config(state=tk.DISABLED)


root.mainloop()
