# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

workers_lastname = []
workers_counter = 0
salary_summ = 0
with open("task_file.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line)
        worker_salary = line.split(' ')
        if float(worker_salary[1]) < 20000.00:
            workers_lastname.append(worker_salary[0])
        salary_summ += float(worker_salary[1])
        workers_counter += 1
print(f'Средняя величина дохода сотрудников - {salary_summ / workers_counter:.2f} р.')
print('Сотрудники с доходом выше 20 000 р.:')
for ind, el in enumerate(workers_lastname, 1):
    print(ind, el)


