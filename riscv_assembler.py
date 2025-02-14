import opcodes.opcodes as op


def type_of_instruction(line: str) -> str|None:

    """
    opcode x1, ..., xn

    split() -> [opcode, x1, ..., xn] 

    agarra la instruccion -> la traduce al opcode -> devuelve el fmt
    
    """

    instruction_name = line.split()[0] 
 

    return op.instruction_to_fmt[instruction_name] if instruction_name in op.instruction_to_fmt else None


    
def r_parser(inst: str, args: list[str]) -> str:
    """
    Arma una instruccion de tipo r

    31        25 24    20 19    15 14     12 11    7 6       0
    | fuction7  | rs2    | rs1    |  funct3 | rd    | opcode |

    
    add rd,rs1,rs2

    opcode: add
    args: [rd, rs1, rs2]
    """

    #busco los binarios de todo
    opcode = op.intructions_to_opcode[inst]
    rd = op.registers[args[0]]
    rs1 = op.registers[args[1]]
    rs2 = op.registers[args[2]]

    funct3 = op.funct3[inst]
    funct7 = op.funct7[inst]

    #armo el binario

    print("opcode en binario", opcode)
    print("rd en binario", rd)
    print("rs1 en binario", rs1)
    print("rs2 en binario", rs2)
    print("funct3 en binario", funct3)
    print("funct7 en binario", funct7)

    # no hardcodeen? 
    return funct7 << 25 | rs2 << 20 | rs1 << 15 | funct3 << 12 | rd << 7 | opcode


def u_parser(opcode: str, rd: str, funct3: str, rs1: str, rs2:str, funct7) -> str:
    pass

def i_parser(opcode: str, rd: str, funct3: str, rs1: str, rs2:str, funct7) -> str:
    pass

def b_parser(opcode: str, rd: str, funct3: str, rs1: str, rs2:str, funct7) -> str:
    pass

def s_parser(opcode: str, rd: str, funct3: str, rs1: str, rs2:str, funct7) -> str:
    pass

def j_parser(opcode: str, rd: str, funct3: str, rs1: str, rs2:str, funct7) -> str:
    pass

def instruction_parser(line: str, instruction_type: str | None):
    
    if instruction_type == "R":
        print("entre a R")
        return r_parser(line)
    elif instruction_type == "U":
        return u_parser(line)
    elif instruction_type == "I":
        return i_parser(line)
    elif instruction_type == "B":
        return b_parser(line)
    elif instruction_type == "S":
        return s_parser(line)
    elif instruction_type == "J":
        return j_parser(line)
    else:
        return "Invalid instruction type"



