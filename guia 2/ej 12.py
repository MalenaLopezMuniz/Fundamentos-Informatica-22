dic = {}
cantidad = int(input("cantidad de alumnos: "))
for x in range(0,cantidad):
    alumno = input("nombre de alumno: ")
    lst=[]
    i=int(input("notas: "))


    while i>=0:
        lst.append(i)
        i=int(input("notas: "))

    dic[alumno]=lst

for alumnos in dic.keys():
    print(alumnos," ",sum(dic[alumnos])/len(dic[alumnos]))