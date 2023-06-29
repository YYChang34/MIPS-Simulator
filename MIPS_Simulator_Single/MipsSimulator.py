# Converts MIPS instructions into binary and hex
import tkinter as tk
from bleach import clean
from InstructionDecode import instr_decode # converts the instruction part of a line of MIPS code
from RegisterDecode import reg_decode # converts the register and immediate parts of the MIPS code

#clean the screen
def clean():
    text.delete(1.0, "end")

# the main conversion function
def convert():
    code = entry.get()
    code = code.replace("(", " ")
    code = code.replace(")", "")
    code = code.replace(",", " ")
    code = code.replace("  ", " ")
    args = code.split(" ")
    instruction = args[0]
        
    codes = instr_decode(instruction)
    func_type = codes[0]   
    reg_values = reg_decode(func_type, instruction, args[1:]) #get the numeric values of the registers
    
    #the following if statement below prints an error if needed
    if reg_values == None:
        text.insert(tk.INSERT,"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        text.insert(tk.INSERT,"Not a valid MIPS statement\n")
        text.pack()
        return
     
    #execution for r-type functions
    if func_type == "r":            
        opcode = '{0:06b}'.format(codes[1])
        rs = '{0:05b}'.format(reg_values[0])
        rt = '{0:05b}'.format(reg_values[1])
        rd = '{0:05b}'.format(reg_values[2])
        shamt = '{0:05b}'.format(reg_values[3])
        funct = '{0:06b}'.format(codes[2])
        binary = "0b"+opcode+rs+rt+rd+shamt+funct
        hex_string = '{0:08x}'.format(int(binary, base=2))
        #UI
        text.insert(tk.INSERT,"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        text.insert(tk.INSERT,"Function type: R-Type\n")
        text.insert(tk.INSERT,"Instruction form: opcode/  rs /  rt /  rd /shamt/ funct\n")
        text.insert(tk.INSERT,"Formatted binary: "+opcode+"/"+rs+"/"+rt+"/"+rd+"/"+shamt+"/"+funct+"\n")
        text.insert(tk.INSERT,"Binary:           "+binary+"\n")
        text.insert(tk.INSERT,"Hex:              0x"+hex_string+"\n")
        text.pack()
        return
    
    #execution for i-type functions    
    elif func_type == "i":
        opcode = '{0:06b}'.format(codes[1])
        rs = '{0:05b}'.format(reg_values[0])
        rt = '{0:05b}'.format(reg_values[1])
        imm = '{0:016b}'.format(reg_values[2])
        binary = "0b"+opcode+rs+rt+imm
        hex_string = '{0:08x}'.format(int(binary, base=2))
        #UI
        text.insert(tk.INSERT,"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        text.insert(tk.INSERT,"Function type: I-Type\n")
        text.insert(tk.INSERT,"Instruction form: opcode/  rs /  rt /   immediate      \n")
        text.insert(tk.INSERT,"Formatted binary: "+opcode+"/"+rs+"/"+rt+"/"+imm+"\n")
        text.insert(tk.INSERT,"Binary:           "+binary+"\n")
        text.insert(tk.INSERT,"Hex:              0x"+hex_string+"\n")
        text.pack()
        return
    
    #execution for j-type functions    
    elif func_type == "j":
        opcode = '{0:06b}'.format(codes[1])
        imm = '{0:026b}'.format(reg_values[0])
        binary = "0b"+opcode+imm
        hex_string = '{0:08x}'.format(int(binary, base=2))
        #UI
        text.insert(tk.INSERT,"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        text.insert(tk.INSERT,"Function type: I-Type\n")
        text.insert(tk.INSERT,"Instruction form: opcode/          immediate           \n")
        text.insert(tk.INSERT,"Formatted binary: "+opcode+"/"+imm+"\n")
        text.insert(tk.INSERT,"Binary:           "+binary+"\n")
        text.insert(tk.INSERT,"Hex:              0x"+hex_string+"\n")
        text.pack()         
    else:
        text.insert(tk.INSERT,"-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        text.insert(tk.INSERT,"Not a valid MIPS statement\n")
        text.pack()
        return
        
    return

#UI
win = tk.Tk()
win['bg'] = 'light yellow'
win.title('MIPS Simulator for eaxh instruction') 
win.geometry('800x600')

title = tk.Label(win,text = 'Please enter MIPS struction:', bg = 'pink', font = ('Arial', 10))
title.pack()

entry = tk.Entry(win, width = 20, font = ('Arial', 15))
entry.pack()

text = tk.Text(win)

button_normal = tk.Button(win,text = 'Enter',command = convert, bg = 'red', width = 10, height = 2, font = ('Arial', 10))
button_clean = tk.Button(win,text = 'Clean',command = clean, bg = 'light green', width = 10, height = 2, font = ('Arial', 10))
button_normal.pack(anchor = tk.N, pady = 10)
button_clean.pack(anchor = tk.N)
win.mainloop()