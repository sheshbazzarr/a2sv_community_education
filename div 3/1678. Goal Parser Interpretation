class Solution:
    def interpret(self, command: str) -> str:
        string=""
        i=0
        while i<len(command):
            if command[i]=='G':
                string+='G'
                i+=1
            elif command[i]=="(" and command[i+1]==")":
                string+='o'
                i+=2
            elif command[i]=='(' and command[i+1]=='a':
                string+='al'
                i+=4
        return string
