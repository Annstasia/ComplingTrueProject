Планировалось называть файлы нормально, не сложилось
<ol>
  <li>Папка bil1 - тут хранятся тексты былин<li>
  <li>Файл namesFile.py - тут я выделяю части слова по которым можно определить имя, сохраняю в файл fileJson2.json</li>
  <li>Файл fileJson2.json - хранит словарь из предыдущего пункта
  <li>Файл third.py - тут вытаскиваются имена, характеристики. Все сохраняет в fileJson1.json</li>
  <li>Файл fileJson1.json - см. предыдущий пункт</li>
  <li>Файл second.py - просмотр данных из fileJson1.json Для получения данных не требуется. Нужен, чтобы не потеряться в fileJson1.json</li>
  <li>Файл generateGraph.py - генерирует строки для файла graph1.gexf</li>
  <li>Файл сountWordInAll.py - строит частотник по былинам, сохраняет в countAllWords.txt</li>
  <li>Файл count_parts_of_speech.py строит частотник по ВиМ и былинам, сохраняет в warAndPeace_wihout_punctuation1.txt и text_wihout_punctuation.txt соответственно</li>
  <li>Файл findAdj.py находит прилагательные соседние с именами, сохраняет в newNewData1.json.json</li>
  <li>Файл countAdj.py строит частотник по newNewData1.json.json</li>
</ol>
Остальные программные файл либо помогали мне в чем-то, но не важны, либо делают то, что я не успела проанализировать/придумать как присобачить (tfIdf)
