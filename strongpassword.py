d={'digit':'0','special':'0','upper':'0','lower':'0'}
def validatepassword(passw):
    if(len(passw)>=12 ):
        for ch in passw:
            if(ch.isupper()):
                d['upper']='1'
                
            
            elif(ch.islower()):
                d['lower']='1'
                
            elif(ch.isdigit()):
                d['digit']='1'
                
            else:
                d['special']='1'
                
                
            
        for ch in d.keys():
            if(d[ch]=='0'):
                return 0
        
                  
        return 1
    else:
        return 0

print("Enter th password ")
passw=input()

a=validatepassword(passw)
if(a):
    print("valid")
else:
    print('not valid')