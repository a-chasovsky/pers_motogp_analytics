## Методика оценки результатов MotoGP

### Краткое описание проекта
 
В данном проекте реализована методика для объективной оценки выступлений гонщиков чемпионата MotoGP. После обработки протокола гонки формируется датафрейм с оценками по трем метрикам, а также общим рейтингом. <br>
 
Методика полностью автоматизирована:

- данные автоматически скачиваются с сайта MotoGP в формате .pdf (при этом скачивание происходит не по прямым ссылкам, а с помощью навигации, выбора нужного раздела сайта и гран-при через меню);
- извлекаются из .pdf в виде списка, состоящего их большого числа строк ;
- переформатируются в датафреймы pandas;
- далее считаются итоговые метрики и строятся графики.

В рамках данного проекта реализованы все этапы типовой аналитической задачи (data engineering, data analysis):

- Постановка задачи;
- Выбор метода оценки и определение метрик;
- Определение источника данных;
- Автоматизированное извлечение данных из источника;
- Преобразование данных;
- Расчет метрик;
- Визуализация результатов.
 
**Исходные данные** (протокол результатов гран-при в формате .pdf, скачанный с сайта www.motogp.com)

<img src='images/scr1.png'>

**Выгруженные сырые данные**

<img src='images/scr2.png'>

**Преобразованные данные**

<img src='images/scr3.png'>

**Результаты** 

<img src='images/scr4.png'>

<br>

<img src='images/2022_qatar_franco_morbidelli.png'>

<img src='images/2022_qatar_pol_espargaro.png'>

В заголовке для каждого гонщика укаывается его место в итоговом рейтинге (R12). <br>
Далее приводятся точечные оценки по каждому из трёх показателей и место в рейтинге:

- Start - число отыгранных/потерянных мест на старте;
- Overtakes - число отыгранных/потерянных мест по ходу гонки относительно общего числа изменения позиций данного гонщика;
- Density - плотность времени прохождения каждого круга.

На левом графике показаны позиции гонщика: стартовая, финишная, динамика по ходу гонки. <br>
На правом графике показаны врмена прохождения каждого круга, время лучшего круга, а также линия "идеальных" времен для этого гонщика.
