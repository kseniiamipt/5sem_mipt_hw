1) Как можно описать отношения родительского и дочернего классов?
Дочерний класс наследуют все методы от родительского. Использование родительских и дочерних классов удобно, например, если у нас несколько классов, которые содержат несколько одинаковых методов. Тогда повторяющиеся методы можно выделать в общий родительский класс.
2) Каким образом работает обращение к методу через super()?
super().method(). Так их дочернего класса можем обратиться к родительскому. При сложной иеархии поиск нужного метода ведется обходом в ширину
3) Зачем нужна обработка исключений? В каких случаях ее использование некорректно?
Если пользователь совершается неправомерные действия, то оптимальным вариантом будет сказать ему, что он делает не так, а не упасть ошибкой параллельно с одновременным завершением работы программы. Некорректно обрабатывать слишком много ошибок, так как это будет занимать мноо ресурсов.
4) Что нужно сделать, чтобы реализовать свое собственное исключение?
try:
наша цель, эито мы хотим сделать

exept 'имя ошибки':
если поймаем ошибку, то делаем вот это

else:
делаем если ошибок не было

finally:
делаем в любом случае

Чтобы создать прям собственную ошибку, нужно создать соответствующий класс, а далее вызывать ее через raise

