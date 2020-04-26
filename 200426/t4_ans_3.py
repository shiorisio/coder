S=input()
P=2019

answer=0
mod_table=[0]*P
mod_table[0]=1
revS=S[::-1]

modp=0
mod10=1
for i in range(len(S)):
  mod10=(mod10*10)%P
  #modp=(10*modp+int(revS[i]))%P
  modp=(modp+mod10*int(revS[i]))%P
  mod_table[modp]+=1

#print(mod_table)
for i in range(P):
  answer+=mod_table[i]*(mod_table[i]-1)//2

print(answer)
