#with open('output.txt', 'r', encoding='utf-8') as f:
with open('output.txt', 'r',encoding = 'utf-8') as f:
    result = {}
    for line in f.readlines():
        line = line.strip()
        if not len(line):
            continue
        result[line.split(':')[0]] = line.split(':')[1]
    #print(result)

KC_dic = result

while True:
  #print('Enter a JP word or enter q to quit')
  print('請輸入一個日文字。或按q退出並查看檔案"output.txt"確認')
  JP_word = input()
  if JP_word == 'q':
    print('中日對照檔輸出至output.txt的檔案')
    break

  if JP_word in KC_dic:
     for key,value in KC_dic.items():
         print(key + '的中文為' + value)
  else:
    print(JP_word+' 這個字還沒有相對的中文字，請輸入適當的中文')
    CH_word = input()
    KC_dic[JP_word] = CH_word
    KC_dic.update({JP_word:CH_word})
    print('中文已被更新')

  print('==========================')
  print('目前中日對照的資料有: ')
  print(KC_dic)
  print('==========================')


with open('output.txt','w', encoding='utf-8') as fout:
    for k, v in KC_dic.items():
        dic = k +':'+ v + '\n'
            #print(dic)
        fout.write(dic)
    print(fout)
