from Lab3 import MyQueue

def EnDe(mode,code,text):
        FinalText = MyQueue()
        if (mode == 'E' or mode == 'e'):
                for i in text:
                        if(i != ' '):
                                num = ord(i) + code.deQueue()
                                if num > ord('z') and ord(i) >= 97 and ord(i) <= 122: # small
                                        temp = int(num - ord('z'))
                                        num = 96 + temp
                                if num > ord('Z') and ord(i) >= 65 and ord(i) <= 90:#big
                                        temp = int(num - ord('Z'))
                                        num = 64 + temp
                                FinalText.enQueue(chr(num))
                        else:
                                FinalText.enQueue(' ')
        elif(mode == 'D' or mode == 'd'):
                for i in text:
                        if(i != ' '):
                                num = ord(i) - code.deQueue()
                                if num < ord('A') and ord(i) >= 65 and ord(i) <= 90: #big
                                        temp = int(ord('A') - num)
                                        num = 91 - temp
                                if num < ord('a')and ord(i) >= 97 and ord(i) <= 122:#small
                                        temp = int(ord('a') - num)
                                        num = 123 - temp
                                FinalText.enQueue(chr(num))
                        else:
                                FinalText.enQueue(' ')

        return FinalText.items




text_input = input('Enter text : ')
code_input = input('Enter code : ')
mode_input = input('Encode(E) or Decode(D) : ')
j=0
n=0
code = MyQueue()
for i in text_input:
        if(i != ' '):
                j+=1
   

for i in range(j):
        code.enQueue(ord(code_input[n])-48)
        n+=1
        if (n == len(code_input)):
                n = 0

print(EnDe(mode_input,code,text_input))

#256183
#decode
 
