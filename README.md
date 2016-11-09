## **FireBox**

Pyhon библиотека для взаимодействия с устройствами по последовательному порту. 
``` python
import firebox as fb

serPort = fb.findDevice('stimulator')
if(serPort):
    data = []
    data.append("<fire,200,5>")
    fb.sendMessage(serPort,data)
```


#### Особенности:
* Определение порта устройства по имени
* Возможность передачи передачи передача команд.

#### <i class="icon-anchor"> Импорт библиотеки
``` python
import firebox as fb
```
#### <i class="icon-search"> Поиск устройства

``` python
serPort = fb.findDevice('stimulator')
```
###### Необязательные аргументы: 
> Если для Вас критично время ответа, то выполняйте данный код в начале вашего скрипта.

#### <i class="icon-male"> Тело запроса

``` python
data = []
data.append("<fire,200,5>")
```
Запрос заключен в стоп символы **< ... >**, принимает 3 аргумента, первый из которых является строковым типом, остальные целочисленными.

#### <i class="icon-flash"> Команда

``` python
fb.sendMessage(serPort,data)
```
В случае успешной передачи данных в консоли появится
```
=========== 
Sent from PC -- LOOP NUM 0 TEST STR <fire,200,5>
Reply Received: fired
Timing: 0.213000059128
===========
```

#### <i class="icon-book">  Реализованные методы.

#####  Список портов
``` python
serialPorts()
```
#####  Открытие порта
``` python
openSerial(serPort, baudRate)
# serPort - порт назначения
# baudRate - скорость порта
```
#####  Отправка данных на устройство
``` python
sendToArduino(sendStr)
# sendStr- произвольная строка
```
##### Получение данных с устройства
``` python
recvFromArduino()
```
##### Ожидание ответа устройства
``` python
waitForArduino()
```
##### Отправка сообщения
``` python
sendMessage(serPort,td, baudRate=19200)
# serPort - порт назначения
# td - массив команд
# baudRate - скорость порта
```
##### Поиск устройства
``` python
findDevice(devName,baudRate=19200,numDev=0)
# devName- имя устройства
# baudRate - скорость порта
# numDev - уникальный идентификатор устройства (в случае использования нескольких однотипных устройств)
```

