line = -1
special_opcodes = ["nop","in","out","console","time_0","time_1","time_2","time_3", "counter","keyboard"]
alu_opcodes = ["nand","or","and","nor","add","sub","xor","lsl","lsr","mul"]
special_alu_opcodes = ["mov","neg","not","push","pop","call","ret"]
jumps = ["je","jne","jl","jge","jle","jg","jb","jae","jbe","ja"] 
ram_opcodes = ["load_8","load_16","store_8","store_16","pload_8","pload_16","pstore_8","pstore_16"]
def register(reg):
    if reg == "zr":
        return bin(0)
    elif reg == "sp":
        return bin(14)
    elif reg == "flags":
        return bin(15)
    reg = reg[1:-1]
    elif reg<1 or 13<reg:
        raise ValueError(f"line {line} Register r{reg} is out of bounds")
    else:
        return bin(int(reg))

def opcode(opc):
    if opc in special_opcodes:
        return(0b000000+bin(special_opcodes.index(opc)))
    elif opc in alu_opcodes:
        return(0b010000+bin(alul_opcodes.index(opc)))
    elif opc in jumps:
        return(0b100000+bin(jumps.index(opc)))
    elif opc in ram_opcodes:
        return(0b110000+bin(ram_opcodes.index(opc)))
    elif opc in special_alu_opcodes:
        if opc == "mov":
            return(0b010100,zr)
        elif opc == "neg":
            return(0b010101,zr)
        elif opc == "not":
            return(0b010011,zr)
        elif opc == "push":

        
