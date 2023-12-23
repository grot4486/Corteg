def tpl_sort(tpl): # Эта функция сортирует кортеж
    for i in tpl:
        if type(i) !=int:
            return tpl
    result = (sorted(tpl))
    return result
    
def sliker(tpl, elem): # Эта функция возвращает подкортеж, начиная с первого вхождения элемента elem в кортеже tpl. Если элемент не найден в кортеже, функция возвращает пустой кортеж ().
        if elem not in tpl:
            return()
        start = tpl.index(elem)
        if tpl.cout(elem)==1:
            return tpl[start:]
        end=tpl.index(elem, start +1)
        return tpl[start:end+1]
        
def sieve(tpl): # Эта функция удаляет повторяющиеся элементы из кортежа и возвращает новый кортеж, отсортированный в обратном порядке.
    return tuple(set(tpl))[::-1]

def del_from_tuple(tpl, elem): # Эта функция удаляет все вхождения элемента elem из кортежа tpl и возвращает новый кортеж без этого элемента. Если элемент не найден в кортеже, функция возвращает исходный кортеж без изменений.
        if elem not in tpl:
            return tpl
    
        s = []
        for i in tpl:
            s.append(i)
        s.remove(elem)
        return tuple(s)

def good_students(students): # Эта функция вычисляет средний балл студентов и возвращает список имен студентов, чей балл выше среднего. Имена студентов возвращаются в виде строки, разделенной запятыми.
    a = 0
    for student in students:
        a += student[2]
    a /= len(students)

    names = []
    for student in students:
        if student[2] > a:
            names.append(student[0])

    shortNames = ''
    for name in names:
        end = name.index(' ')
        shortNames += f'{name[:end]}, '

    return f"Ученики {shortNames[:-2]} в этом семестре хорошо учатся!"

students = (("Крячко Марк Александрович", 19, 4.8, "Новосибирск"),
            ("Павлов Александр Витальевич", 20, 4.5, "Новосибирск"),
            ("Муллакаев Андрей Евгеньевич", 17, 4.2, "Новосибирск"),
            ("Левин Максим Максимович", 16, 5.0, "Новосибирск"),
            ("Новиков Дмитрий Дмитриевич", 17, 3.2, "Новосибирск"),
            ("Головин Гордей Романович", 17, 3.1, "Новосибирск"))
print(good_students(students))
