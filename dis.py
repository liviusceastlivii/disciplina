dict1={'disciplina':'L.rom', 'note':[9,8,9,9,8], 'Teza':9}
dict2={'disciplina':'Engleza', 'note':[10,10,10,4,4], 'Teza':6}
dict3={'disciplina':'Matematica', 'note':[6,5,4,7,7],'Teza':7}
a1=sum(dict1['note'])/5
a2=sum(dict2['note'])/5
a3=sum(dict3['note'])/5
c1=round((dict1['Teza']+a1)/2,2)
c2=round((dict2['Teza']+a1)/2,2)
c3=round((dict3['Teza']+a1)/2,2)
med=(c1+c2+c3)/3
print("Media este" , med)
if med>=9:
    print("Eminent")
if (med>8 and med<9):
    print("Proeminent")
if (med<8 and med>5):
    print("Codas")
if (dict1['Teza']<5 or dict2['Teza']<5 or dict3['Teza']<5):
    print('Restantier')


