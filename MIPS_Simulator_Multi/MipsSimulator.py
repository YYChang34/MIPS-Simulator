import tkinter as tk
from bleach import clean
from InstructionDecode import instr_decode # converts the instruction part of a line of MIPS code
from RegisterDecode import reg_decode # converts the register and immediate parts of the MIPS code
from OperationExecute import operation_execute # according to the instruction to execute
from RegisterFile import reg_file # load and save value from register
pc = 0
index = 0
instruction_group = []
label = []
# use binary to represent a value which has 32-bit, then total can save 128 values (4096/32 = 128), 4096 is required total space
#use 4 sublists to save one value which each sublist is 8-bit
data_memory = [[] for _ in range(4096)]
error = []
buffer = [0] * 32
reg_buffer = ["$t0", "$t1", "$s0", "$s1"]

#clean
def clean():
    text.delete(1.0, "end")

#two's complement
def twos_complement(x, bit):
    bits = x.bit_length() + 1
    n = (1 << bits) - 1
    x2 = n & x
    if x < 0:
        x = f"{x2:{bits}b}"
    else:
        x = f"{x2:0{bits}b}"
    if(x[0]=="1"):
        num=x.rjust(bit,'1')
    else:
        num=x.rjust(bit,'0')
    return num


# the main conversion function
def convert(code):
    global data_memory, error, buffer, pc
    inst_buffer = code
    code = code.replace(",", " ")
    code = code.replace("  ", " ")
    args = code.split(" ")
    instruction = args[0]
    
    codes = instr_decode(instruction)
    func_type = codes[0]   
    reg_values = reg_decode(func_type, instruction, args[1:], error) #get the numeric values of the registers
    
    #the following if statement below prints an error if needed
    if reg_values == None:
        #error
        text.insert(tk.INSERT,"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        for i in range(len(error)):
            text.insert(tk.INSERT, error[i] + "\n")
        text.pack()
        return
    else:
        result = operation_execute(func_type, instruction, args[1:], pc, data_memory, buffer)

    # update new pc
    pc = result[0]
    
    # determine branch or j
    for i in range(len(label)):
        if func_type == "i" and args[3] in label[i]:
            pc = label[i][0]
        elif func_type == "j" and args[1] in label[i]:
            pc = label[i][0]
     
    #execution for r-type functions
    if func_type == "r":
        # machine code            
        opcode = '{0:06b}'.format(codes[1])
        rs = '{0:05b}'.format(reg_values[0])
        rt = '{0:05b}'.format(reg_values[1])
        rd = '{0:05b}'.format(reg_values[2])
        shamt = '{0:05b}'.format(reg_values[3])
        funct = '{0:06b}'.format(codes[2])
        pc_text = '{0:032b}'.format(pc)
        inst_text = opcode + rs + rt + rd + shamt + funct

        text.insert(tk.INSERT, "Instruction: ")
        text.insert(tk.INSERT, inst_buffer + "\n")

        text.insert(tk.INSERT, "PC: ")
        text.insert(tk.INSERT, pc_text + "\n")

        text.insert(tk.INSERT, "Register File:\n")
        if args[1] == "$t0":
            text.insert(tk.INSERT, "$t0: " + '{0:032b}'.format(result[1]) + "\n")
        elif args[1] == "$t1":
            text.insert(tk.INSERT, "$t1: " + '{0:032b}'.format(result[1]) + "\n")
        elif args[1] == "$s0":
            text.insert(tk.INSERT, "$s0: " + '{0:032b}'.format(result[1]) + "\n")
        elif args[1] == "$s1":
            text.insert(tk.INSERT, "$s1: " + '{0:032b}'.format(result[1]) + "\n")
        else:
            text.insert(tk.INSERT, args[1] + ": " + '{0:032b}'.format(reg_file(True, args[1], buffer, 0)) + "\n")

        text.insert(tk.INSERT, "Instruction Memory:\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 4) + "] = " + inst_text[0:8] + "\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 3) + "] = " + inst_text[8:16] + "\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 2) + "] = " + inst_text[16:24] + "\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 1) + "] = " + inst_text[24:32] + "\n")

        text.insert(tk.INSERT, "Data Memory:\n")
        flag = 0
        for i in range(4096):
            if data_memory[i] != []:
                flag = 1
                text.insert(tk.INSERT, "MEM[" + str('{0:032b}'.format(i)) + "] = " + str('{0:08b}'.format(data_memory[i])) + "\n")
        if flag == 0:
            text.insert(tk.INSERT, "None\n")

        
        
    #execution for i-type functions    
    elif func_type == "i":
        # machine code            
        opcode = '{0:06b}'.format(codes[1])
        rs = '{0:05b}'.format(reg_values[0])
        rt = '{0:05b}'.format(reg_values[1])
        if reg_values[2] < 0:
            imm = twos_complement(reg_values[2], 16)
        else:
            imm = '{0:016b}'.format(reg_values[2])
        pc_text = '{0:032b}'.format(pc)
        inst_text = opcode + rs + rt + imm

        text.insert(tk.INSERT, "Instruction: ")
        text.insert(tk.INSERT, inst_buffer + "\n")

        text.insert(tk.INSERT, "PC: ")
        text.insert(tk.INSERT, pc_text + "\n")

        text.insert(tk.INSERT, "Register File:\n")
        if args[1] == "$t0":
            text.insert(tk.INSERT, "$t0: " + '{0:032b}'.format(result[1]) + "\n")
        elif args[1] == "$t1":
            text.insert(tk.INSERT, "$t1: " + '{0:032b}'.format(result[1]) + "\n")
        elif args[1] == "$s0":
            text.insert(tk.INSERT, "$s0: " + '{0:032b}'.format(result[1]) + "\n")
        elif args[1] == "$s1":
            text.insert(tk.INSERT, "$s1: " + '{0:032b}'.format(result[1]) + "\n")
        else:
            text.insert(tk.INSERT, args[1] + ": " + '{0:032b}'.format(reg_file(True, args[1], buffer, 0)) + "\n")

        text.insert(tk.INSERT, "Instruction Memory:\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 4) + "] = " + inst_text[0:8] + "\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 3) + "] = " + inst_text[8:16] + "\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 2) + "] = " + inst_text[16:24] + "\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 1) + "] = " + inst_text[24:32] + "\n")

        text.insert(tk.INSERT, "Data Memory:\n")
        flag = 0
        for i in range(4096):
            if data_memory[i] != []:
                flag = 1
                text.insert(tk.INSERT, "MEM[" + str('{0:032b}'.format(i)) + "] = " + str('{0:08b}'.format(data_memory[i])) + "\n")
        if flag == 0:
            text.insert(tk.INSERT, "None\n")
    
    #execution for j-type functions    
    elif func_type == "j":
        opcode = '{0:06b}'.format(codes[1])
        imm = '{0:026b}'.format(reg_values[0])
        pc_text = '{0:032b}'.format(pc)
        inst_text = opcode + imm

        text.insert(tk.INSERT, "Instruction: ")
        text.insert(tk.INSERT, inst_buffer + "\n")

        text.insert(tk.INSERT, "PC: ")
        text.insert(tk.INSERT, pc_text + "\n")

        text.insert(tk.INSERT, "Register File:\n")
        if args[1] == "$t0":
            text.insert(tk.INSERT, "$t0: " + '{0:032b}'.format(result[1]) + "\n")
        elif args[1] == "$t1":
            text.insert(tk.INSERT, "$t1: " + '{0:032b}'.format(result[1]) + "\n")
        elif args[1] == "$s0":
            text.insert(tk.INSERT, "$s0: " + '{0:032b}'.format(result[1]) + "\n")
        elif args[1] == "$s1":
            text.insert(tk.INSERT, "$s1: " + '{0:032b}'.format(result[1]) + "\n")
        else:
            text.insert(tk.INSERT, args[1] + ": " + '{0:032b}'.format(reg_file(True, args[1], buffer, 0)) + "\n")

        text.insert(tk.INSERT, "Instruction Memory:\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 4) + "] = " + inst_text[0:8] + "\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 3) + "] = " + inst_text[8:16] + "\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 2) + "] = " + inst_text[16:24] + "\n")
        text.insert(tk.INSERT, "MEM[" + '{0:032b}'.format(pc - 1) + "] = " + inst_text[24:32] + "\n")

        text.insert(tk.INSERT, "Data Memory:\n")
        flag = 0
        for i in range(4096):
            if data_memory[i] != []:
                flag = 1
                text.insert(tk.INSERT, "MEM[" + str('{0:032b}'.format(i)) + "] = " + str('{0:08b}'.format(data_memory[i])) + "\n")
        if flag == 0:
            text.insert(tk.INSERT, "None\n")                
    return pc

#input file path
def input_file_path():
    file_path = entry.get() # absolute path
    return file_path

# main
def read_file():
    global reg_buffer, label, pc
    fo = open(input_file_path(), "r+")
    line = fo.read()
    line = line.split("\n")
    # determine is label
    for currentToken in line:
        if currentToken.find(": ") != -1:
            currentToken = currentToken.split(": ")
            label.append([pc, currentToken[0]]) # record label
            currentToken = currentToken[1] # record instruction
        instruction_group.append(currentToken) # record instruction

        # first get registers(check reg whether is in reg_buffer or not)
        currentToken = currentToken.replace(",", " ")
        currentToken = currentToken.split(" ")
        del currentToken[0] # remove inst
        if currentToken not in reg_buffer:
            reg_buffer = reg_buffer + currentToken
        # record pc
        pc = pc + 4
    fo.close
    # initial pc
    pc = 0

def execute():
    global index, instruction_group
    if index < len(instruction_group):
        # decode ot know branch or j and get pc from convert
        addr = convert(instruction_group[index])
        if addr != 0:
            index = addr
        else:
            index = index + 1
    else:
        text.insert(tk.INSERT,"Finish Byb~\n")

#UI
win = tk.Tk()
win['bg'] = 'light yellow'
win.title('CA Project 2') 
win.geometry('800x600')

title = tk.Label(win,text = 'Please enter the file path:', bg = 'pink', font = ('Arial', 10))
title.pack()

entry = tk.Entry(win, width = 20, font = ('Arial', 15))
entry.pack()

text = tk.Text(win)

button_file_path = tk.Button(win,text = 'Enter',command = input_file_path, bg = 'red', width = 10, height = 2, font = ('Arial', 10))
button_read_file = tk.Button(win,text = 'Read file',command = read_file, bg = 'light blue', width = 10, height = 2, font = ('Arial', 10))
button_execute = tk.Button(win,text = 'Execute',command = execute, bg = 'orange', width = 10, height = 2, font = ('Arial', 10))
button_clean = tk.Button(win,text = 'Clean',command = clean, bg = 'light green', width = 10, height = 2, font = ('Arial', 10))
button_file_path.pack(anchor = tk.N, pady = 10)
button_read_file.pack(anchor = tk.N)
button_execute.pack(anchor = tk.N, pady = 10)
button_clean.pack(anchor = tk.N)
win.mainloop()