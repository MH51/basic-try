name=str(input("enter name "))
date=str(input("enter date "))
letter='''dear <name>
		you r selectes <date>'''

letter=letter.replace("<name>",name)
letter=letter.replace("<date>",date)
print(letter)
