from tkinter import Tk, simpledialog, messagebox

def readFile():
    with open('countries.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            theWorld[country] = city
            
def writeFile(country, city):
    with open('countries.txt', 'a') as file:
        file.write('\n' + country + '/' + city)
            
            
#main code
root = Tk()
root.withdraw()
while True:
    theWorld = {}
    readFile()

    guess = simpledialog.askstring('ELY', 'Maa:')
    guess = guess.capitalize()

    if guess in theWorld:
        result = theWorld[guess]
        messagebox.showinfo('Vastaus',
                            'maan ' + guess + ' pääkaupunki on ' + result + '!')
    else:
        newcity = simpledialog.askstring('Opeta minua',
                                         'en tiedä ' +
                                         'pääkaupunkia maassa ' + guess + '?')
        theWorld[guess] = newcity
        writeFile(guess, newcity)



