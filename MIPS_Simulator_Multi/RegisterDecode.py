# dictionary used to contain register numeric values
registers = {
    "$zero" : 0, "$at" : 1, "$v0" : 2, "$v1" : 3, "$a0" : 4, "$a1" : 5, "$a2" : 6, "$a3" : 7, 
    "$t0" : 8, "$t1" : 9, "$t2" : 10, "$t3" : 11, "$t4" : 12, "$t5" : 13, "$t6" : 14, "$t7" : 15,
    "$s0" : 16, "$s1" : 17, "$s2" : 18, "$s3" : 19, "$s4" : 20, "$s5" : 21, "$s6" : 22, "$s7" : 23,
    "$t8" : 24, "$t9" : 25, "$k0" : 26, "$k1" : 27, "$gp" : 28, "$sp" : 29, "$fp" : 30,"$ra" : 31,
    "$0" : 0, "$1" : 1, "$2" : 2, "$3" : 3, "$4" : 4, "$5" : 5, "$6" : 6, "$7" : 7, "$8" : 8,
    "$9" : 9, "$10" : 10, "$11" : 11, "$12" : 12, "$13" : 13, "$14" : 14, "$15" : 15, "$16" : 16,
    "$17" : 17, "$18" : 18, "$19" : 19, "$20" : 20, "$21" : 21, "$22" : 22, "$23" : 23, "$24" : 24,
    "$25" : 25, "$26" : 26, "$27" : 27, "$28" : 28, "$29" : 29, "$30" : 30, "$31" : 31
}

# Given the function type, reg_decode will output an array containing the
# numeric values of the registers and immediates in MIPS code.   
# param 'func_type' is the function type of the MIPS code
# param 'instr' is the instruction given in the MIPS code
# param 'regs' is an array containing the registers used in the MIPS code
# returns an array in the form [rs, rt, rd, shamt] for r-type functions
# returns an array in the form [rs, rt, immediate] for i-type functions
def reg_decode(func_type, instr, regs, error):
    
    #execution for r-type functions
    if func_type == "r": 
        
        #special case for MIPS shifts
        if (instr == "sll") or (instr == "srl"): 
            try:
                if int(regs[2]) > 0 and int(regs[2]) < 31:
                    #return[rs,     rt,                 rd,                   shamt]
                    return [0, registers[regs[1]], registers[regs[0]], int(regs[2])]
                else:
                    flag = 1
            except:
                if regs[0] not in registers:
                    error.append("Error: Destination operand " + regs[0] + " doesn't exist!")
                if regs[1] not in registers:
                    error.append("Error: Source operand " + regs[1] + " doesn't exist!")
                if regs[2][0].isdecimal() == False:
                    error.append("Error: Source operand " + regs[2] + " doesn't exist!")
                elif flag == 1:
                    error.append("Error: Shamt " + regs[2] + " is out of space!")
                    flag = 0
                return None             

        #special case for MIPS jr
        if (instr == "jr"): 
            try:
                if registers[regs[0]] != 31:
                    flag = 1
                else:
                    #return[        rs,        rt, rd,shamt]
                    return [registers[regs[0]], 0, 0, 0]
            except:
                if flag == 1:
                    error.append("Error: Source operand " + regs[0] + " is not $ra or $31!")
                    flag = 0
                return None                
            
        #standard r-type MIPS instructions              
        try:   
            #return[      rs,                 rt,               rd,          shamt]    
            return[registers[regs[1]], registers[regs[2]], registers[regs[0]], 0]
        except:
            #destination operand format error
            if regs[0][0].isdecimal():
                error.append("Error: Destination operand " + regs[0] + " doesn't exist!")
            elif regs[0] not in registers:
                error.append("Error: Destination operand " + regs[0] + " doesn't exist!")
            #source operand format error
            if regs[1][0].isdecimal():
                error.append("Error: Source operand " + regs[1] + " doesn't exist!")
            elif regs[1] not in registers:
                error.append("Error: Source operand " + regs[1] + " doesn't exist!")
            if regs[2][0].isdecimal():
                error.append("Error: Source operand " + regs[2] + " doesn't exist!")
            elif regs[2] not in registers:
                error.append("Error: Source operand " + regs[2] + " doesn't exist!")            
            return None


    #execution for i-type functions
    elif func_type == "i":                
        
        #special case for lw, sw
        if (instr == "lw") or (instr == "sw"):
            if len(regs[1]) > 0:
                regs[1] = regs[1].replace(")", "")
                regs[1] = regs[1].split("(")
                imm = int(regs[1][0])
                try:
                    if imm > 32767 and imm < -32768:
                        flag = 1
                    elif imm % 4 != 0:
                        flag = 2
                    else:
                        #return[       rs,                rt        ,  immediate  ]      
                        return[registers[regs[1][1]], registers[regs[0]], imm]
                except:
                    if regs[0] not in registers:
                        if instr == "lw":
                            error.append("Error: Destination operand " + regs[0] + " doesn't exist!")
                        if instr == "sw":
                            error.append("Error: Source operand " + regs[0] + " doesn't exist!")
                    if regs[1][1] not in registers:
                        error.append("Error: Source operand " + regs[1][1] + " doesn't exist!")
                    elif flag == 1:
                        error.append("Error: " + imm + " is out of the memory space!")
                        flag = 0
                    elif flag == 2:
                        error.append("Error: " + imm + " is not the multiple of 4!")
                        flag = 0
                    return None
                            
            
        #standard i-type MIPS instructions    
        try:
            if len(regs[2]) > 0 and (instr != "beq" or instr != "bne"):
                imm = int(regs[2])
                if imm > 32767 or imm < -32768:
                    flag = 1
                else:
                    #return[        rs                 rt        immediate ]
                    return [registers[regs[1]], registers[regs[0]], imm]
        except:
            if regs[0][0].isdecimal():
                error.append("Error: Destination operand " + regs[0] + " doesn't exist!")
            elif regs[0] not in registers:
                error.append("Error: Destination operand " + regs[0] + " doesn't exist!")
            #source operand format error
            if regs[1][0].isdecimal():
                error.append("Error: Source operand " + regs[1] + " doesn't exist!")
            elif regs[1] not in registers:
                error.append("Error: Source operand " + regs[1] + " doesn't exist!")
            if flag == 1:
                error.append("Error: " + regs[2] + " is out of the memory space!")
                flag = 0
            return None      