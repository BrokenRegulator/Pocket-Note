stor = {}

def start():
  NewNote = input("Enter a number\n1 - New\n2 - Search\n3 - Delete All\n4 - Delete\n5 - Print\nEnter Choice: ")
  if (NewNote not in ['1','2','3','4','5','99','please']):
    print("Na-ua-a, you didn't say the magic word")
    start()
  name = ""
  if (NewNote == "1"):
    name = input ("What is the name of the note: ")
    if (name == "" or str.strip(name) == ""):
      print("Note must have a name")
      start()
    else:
      createNote(name)
  if (NewNote == '2'):
    search()
  if (NewNote == '3'):
    delete()
  if (NewNote == '4'):
    delSetup()
  if (NewNote == '5'):
    printNotes()
  if (NewNote == '99'):
    print('Insert disk 22, 47, and 114')
  if (NewNote == 'please'):
    print('Unkown Command')
def delSetup():
  delNam = input('What is the name of the note that you want to delete? ')
  if (delNam in stor.keys()):
    deleteSpec(delNam)
  else:
    print('error: Note not found, or can not be deleted')
    start()
  


def createNote(name):
  note = input("Note: ")
  stor[name] = note
  save()
  start()
  


def search():
  name = input ("What note are you looking for? (Enter the name of a note): " )
  if (name in stor.keys()):
    print(stor[name])
  else:
    print("error: Note not found.")
  start()


def save():
  txt_w = open("Txt.txt", "w")
  for key, value in stor.items():
    txt_w.write(key)
    txt_w.write(' ~ ')
    txt_w.write(value + '\n')
  txt_w.close()

def upload():
  txt_u = open("Txt.txt", "r")
  for line in txt_u:
    item = line
    item = item[:-1]
    center = item.find(" ~ ")
    key = item[:center]
    value = item[center+3:]
    stor[key] = value

def delete():
      of = open('Txt.txt', 'w')
      of.close()
      print('Notes deleted')
      start()

def deleteSpec(name):
  del stor[name]
  delete()
  save()
  print('Note deleted')
  start()

def printNotes():
  for key in stor.keys():
    print(key)
  start()
#start of program.
upload()
start()
