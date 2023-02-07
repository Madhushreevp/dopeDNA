letter = '''Dear <|NAME|>,\n
you are selected,\n
Date is <|DATE|>,\n
'''
name=input("enter ur name\n")
date=input("enter ur date\n" )
letter=letter.replace("<|NAME|>",name )
letter=letter.replace("<|DATE|>",date )
print( letter )
