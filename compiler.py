line_count = 0
labels = []
special_opcodes = ["nop","in","out","console","time_0","time_1","time_2","time_3", "counter","keyboard"]
alu_opcodes = ["nand","or","and","nor","add","sub","xor","lsl","lsr","mul"]
special_alu_opcodes = ["mov","neg","not","push","pop","call","ret"] #these need to be handled on a case-by-case basis
jumps = ["je","jne","jl","jge","jle","jg","jb","jae","jbe","ja"] 
ram_opcodes = ["load_8","load_16","store_8","store_16","pload_8","pload_16","pstore_8","pstore_16"]
output = ""

def register(reg):
    try:
        reg = int(reg)
        if reg <-32768 or reg > 65535:
            raise ValueError
        else:
            return(bin(reg))
    except:
        if reg == "zr":
            return bin(0)
        elif reg == "sp":
            return bin(14)
        elif reg == "flags":
            return bin(15)
        reg = reg[1:-1]
        if reg<1 or 13<reg:
            raise ValueError(f"line {line_count} Register r{reg} is out of bounds")
        else:
            return bin(int(reg))

def opcode(opc,reg1,regdest):
    if opc in special_opcodes:
        return(0b000000+bin(special_opcodes.index(opc)))
    elif opc in alu_opcodes:
        return(0b010000+bin(alu_opcodes.index(opc)))
    elif opc in jumps:
        return(0b100000+bin(jumps.index(opc)))
    elif opc in ram_opcodes:
        return(0b110000+bin(ram_opcodes.index(opc)))
    elif opc in special_alu_opcodes:
        if opc == "mov":
            return(f"add {regdest},zr,{reg1}")
        elif opc == "neg":
            return(f"sub {regdest},zr,{reg1}")
        elif opc == "not":
            return(f"nor {regdest},zr,{reg1}")
        elif opc == "push":
            return([f"store_16 [sp] {regdest}","sub sp sp 2"])
        elif opc == "pop":
            return([f"load_16 {regdest} [sp]","add sp sp 2"])
        elif opc == "call":
            return(["counter flags","add flags flags 16","push flags",f"jmp {reg1}"])
        elif opc == "ret":
            return("pop flags","jmp flags")
        else:
            raise KeyError(f"line {line_count}: invalid opcode: {opc}")


def main_(line):

    line_count += 1
    if ":" in line:
        line_count -= 1
        labels.append(line[0:-2])
    else:
        temp = line.find(" ") #temporaries just for splitting the string into opcodes and registers
        temp2 = line[0:temp]
        temp3 = line[temp+1:-1]
        regcount = 0
        reg1 = ""
        reg2 = ""
        regdest = ""
        temp4 = ""
        for char in temp3:
            if char == ",":
                 if regcount == 0:
                     regdest = temp4
                 elif regcount == 1:
                     reg1 = temp4
                 else:
                     reg2 = temp4
                 regcount += 1
                 temp4 = ""
            else:
                temp4 += char
        opc = opcode(temp2,reg1,regdest)
        output *= 64
        output.append(register(reg1))
        output *= 16
        output.append(register(reg2))
        output *= 16
        output.append(register(regdest))
        
        try:
            opc = int(opc)
            output.append(opc)
        except:
            for line in opc:
                main_(line)




