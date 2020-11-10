def calc(term):
    
    numeric = ''   #число, встретившееся в строке term
    znak = {} #знаки,встретившиеся в term, внутри скобок
    colsk = 0 #количество скобок
    znak[colsk]=[]
    mistake=''
    summary = [] #итоговое выражение    

    if term[0] == '-':
        term='0'+term
        
        
    for i in range(len(term)):
        if term[i] not in ['+','-','*','/', ')', ' ', '(', '.', ','] and term[i].isdigit()==False:
            for j in range(i,len(term)):
                if term[j] not in ['+','-','*','/', ')', ' ', '(', '.', ','] and term[j].isdigit()==False:
                    mistake+=term[j]
            return ('некорректный ввод, строка содержит недопустимое значение ', mistake)
        
        if term[i] == ' ':
            continue
        
        if term[i] in ['.',',']:
            numeric+='.'
             
            if term[i+1].isdigit() == False:
                return ('Неверная запись выражения')
            
        
        #если i элемент является цифрой, то добавим его в конец временной строки numeric
        if term[i].isdigit():
            numeric+=term[i]
            
            #если i+1 элемент не цифра и не конец строки, то довавим число из numeric в  итоговую строку summary
            #и обнулим numeric для следующих чисел

            
            if i+1 == len(term) or term[i+1] in ['+','-','*','/', ')', ' ']:
                summary.append(numeric)
                numeric = ''                 
                
        # если i элемент + или - , то проверяем словарь znak,  в котором записаны знаки внутри скобок под номером colsk
        # и добавляем все элементы оттуда в обратном порядке в summary, удаляя их из словаря znak внутри colsk 
        # затем добавляем этот встретившийся + или - в словарь znak в colsk
        if term[i] in ['+', '-']:

            if len(znak[colsk])>0:
                for zn in range(len(znak[colsk])):
                    summary.append(znak[colsk].pop())
            znak[colsk].append(term[i])
                                                   
        # если i это последний элемент, то добавояем все знаки из словаря znak[colsk] в обратном порядке в summary
        if i+1 == len(term):
            if len(znak[colsk])>0:
                for zn in range(len(znak[colsk])):
                    summary.append(znak[colsk].pop()) 
                            
        # если i элемент это * или /, то добавим его в znak[colsk]
        if term[i] in ['*', '/']:
            znak[colsk].append(term[i])
            
        # если i элемент это ')', то то добавояем все знаки из словаря znak[colsk] в обратном порядке в summary
        # и вычтем из colsk единицу
        if term[i] == ')':
            if len(znak[colsk])>0:
                for zn in range(len(znak[colsk])):
                    summary.append(znak[colsk].pop()) 
            colsk-=1
            
        
        if term[i] == '(':
            colsk += 1
            znak[colsk]=[]
            
    if len(znak[0])>0:
        for zn in range(len(znak[0])):
            summary.append(znak[0].pop()) 
             
 
    k = summary
    
    for i in range(len(k)):
        
       
        if k[i].isdigit() == False:

            if k[i] == '*':
                k[i] = str(float(k[i-1]) * float(k[i-2]))
                k.pop(i-1)
                k.pop(i-2)

                k.insert(0, 'N')
                k.insert(0, 'N')
            if k[i] == '-':
                k[i] = str(float(k[i-2]) - float(k[i-1]))
                k.pop(i-1)
                k.pop(i-2)
                k.insert(0, 'N')
                k.insert(0, 'N')
            if k[i] == '+':
                k[i] = str(float(k[i-1]) + float(k[i-2]))
                k.pop(i-1)
                k.pop(i-2)
                k.insert(0, 'N')
                k.insert(0, 'N')
            if k[i] == '/':
                k[i] = str(float(k[i-2]) / float(k[i-1]))
                k.pop(i-1)
                k.pop(i-2)
                k.insert(0, 'N')
                k.insert(0, 'N')
        
    
    return (print( 'результат "'+str(round(float(k.pop()), 2))+'"'))


print('Введите выражение')
term = input()

calc(term)

