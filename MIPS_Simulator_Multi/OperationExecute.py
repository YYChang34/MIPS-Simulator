from RegisterFile import reg_file # load and save value from register

def operation_execute(func_type, instr, regv, pc, data_memory, buffer):

    if func_type == "r":

        if instr == "jr":
            pc = reg_file(True, regv[0], buffer, 0) # pc == R[rs]
            return pc

        if instr == "sll":
            rd = reg_file(True, regv[0], buffer, 0)
            rt = reg_file(True, regv[1], buffer, 0)
            rd = rt << regv[2]
            reg_file(False, regv[0], buffer, rd)
            pc = pc + 4
            return [pc, rd]
        
        elif instr == "srl":
            rd = reg_file(True, regv[0], buffer, 0)
            rt = reg_file(True, regv[1], buffer, 0)
            rd = rt >> regv[2]
            reg_file(False, regv[0], buffer, rd)
            pc = pc + 4
            return [pc, rd]
        
        rd = reg_file(True, regv[0], buffer, 0)
        rs = reg_file(True, regv[1], buffer, 0)
        rt = reg_file(True, regv[2], buffer, 0)

        if instr == "add":
            rd = rs + rt

        elif instr == "addu":
            rd = rs + rt

        elif instr == "and":
            rd = rs & rt

        elif instr == "nor":
            rd = not (rs or rt)
            
        elif instr == "or":
            rd = rs or rt

        elif instr == "slt":
            if rs < rt:
                rd = 1
            else:
                rd = 0

        elif instr == "sltu":
            if rs < rt:
                rd = 1
            else:
                rd = 0
            
        elif instr == "sub":
            rd = rs - rt
        
        pc = pc + 4
        reg_file(False, regv[0], buffer, rd)

        return [pc, rd]

    elif func_type == "i":
        rs = reg_file(True, regv[1], buffer, 0)
        rt = reg_file(True, regv[0], buffer, 0)
        imm = int(regv[2])
        
        if instr == "addi":
            rt = rs + imm

        elif instr == "addiu":
            rt = rs + imm

        elif instr == "beq":
            if rs == rt:
                pc = pc + imm * 4

        elif instr == "bne":
            if rs != rt:
                pc = pc + imm * 4

        elif instr == "lw":
            regv[1] = regv[1].replace(")", "")
            regv[1] = regv[1].split("(")
            imm = int(regv[1][0])
            rs = reg_file(True, regv[1][1], buffer, 0)
            addr = rs + imm
            rt = data_memory[addr] + data_memory[addr+1] + data_memory[addr+2] + data_memory[addr+3]
            
            rt = int(str(rt), 2)
            reg_file(False, regv[0], buffer, rt)
            pc = pc + 4
            return [pc, rt]
            
        elif instr == "sw":
            regv[1] = regv[1].replace(")", "")
            regv[1] = regv[1].split("(")
            imm = int(regv[1][0])
            rs = reg_file(True, regv[1][1], buffer, 0) 
            value = '{0:032b}'.format(rt)
            addr = rs + imm
            data_memory[addr].append(value[0:8])
            data_memory[addr + 1].append(value[8:16])
            data_memory[addr + 2].append(value[16:24])
            data_memory[addr + 3].append(value[24:32])
            pc = pc + 4
            return [pc, rt]

        elif instr == "slti":
            if rs < imm:
                rt = 1
            else:
                rt = 0
        
        pc = pc + 4
        reg_file(False, regv[0], buffer, rt)

        return [pc, rt]

    elif func_type == "j":

        if instr == "j" or "jal":
            pc_value = '{0:032b}'.format(pc)
            pc_start_four_bits = pc_value[0:4]
            position = '{0:028b}'.format(int(regv[0]) * 4)
            position = position[-28:] # only need 28-bit
            addr = pc_start_four_bits + position
            pc = int(addr, 2) # change back to decimal

            return [pc]    