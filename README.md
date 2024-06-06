# goit-algo-hw-05

GoIT_Algo_hw05

Результати вимірювання часу 
Article 1 - Existing Substring 
Boyer-Moore: 0.002 seconds 
KMP: 0.003 seconds 
Rabin-Karp: 0.004 seconds 

Article 1 - Non-Existing Substring 
Boyer-Moore: 0.003 seconds 
KMP: 0.004 seconds 
Rabin-Karp: 0.005 seconds 

Article 2 - Existing Substring 
Boyer-Moore: 0.0015 seconds 
KMP: 0.002 seconds 
Rabin-Karp: 0.003 seconds 

Article 2 - Non-Existing Substring
Boyer-Moore: 0.002 seconds 
KMP: 0.0025 seconds 
Rabin-Karp: 0.0035 seconds

Висновоки:

Алгоритм Боєра-Мура:
Найшвидший як для існуючих, так і для неіснуючих підрядків у обох текстах.
Перевага алгоритму в тому, що він виконує менше перевірок завдяки використанню
поганої таблиці символів, що дозволяє швидше переміщувати вікно пошуку. 

Алгоритм Кнута-Морріса-Пратта (КМП):
Зазвичай трохи повільніший за Боєра-Мура, але все ж швидший за Рабіна-Карпа.
Ефективний у пошуку шаблонів, але потребує побудови додаткового масиву для
обробки зразка. 

Алгоритм Рабіна-Карпа:
Найповільніший серед трьох алгоритмів. Перевага в простоті реалізації та
використанні хешування, але швидкість може страждати через колізії хешів.

Найшвидший алгоритм: 
Для Article 1 та Article 2, як для існуючих, так і для неіснуючих підрядків, 
найшвидшим алгоритмом є Боєр-Мур. Ці висновки показують, що алгоритм Боєра-Мура в 
більшості випадків є ефективнішим для пошуку підрядків у великих текстових файлах.
