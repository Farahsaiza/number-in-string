import re 


def chiffre(para):
     x=re.findall('[0-9]',para)
     list=[]
     if x !=[]:
          return True
     else:
          return False
     

para=str(input("write te a paragraph: "))
if chiffre(para)== True:
     print("it  exist digits in  this paragraph ")
else:
     print("it dosn't exist digits in  this paragraph ")
     
