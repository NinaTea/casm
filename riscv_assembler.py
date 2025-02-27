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
    # print("opcode en binario", opcode)
    # print("rd en binario", rd)
    # print("rs1 en binario", rs1)
    # print("rs2 en binario", rs2)
    # print("funct3 en binario", funct3)
    # print("funct7 en binario", funct7)

    # no hardcodeen? 
    return funct7 << 25 | rs2 << 20 | rs1 << 15 | funct3 << 12 | rd << 7 | opcode

def u_parser(inst: str, args: list[str]) -> str:
    pass
    # return imm << 12 | rd << 7 | opcode  

def i_parser(inst: str, args: list[str]) -> str:
    
    """
    Arma una instruccion de tipo i

    31        20 19    15 14     12 11    7 6       0
    | imm[11:0] | rs1    |  funct3 | rd    | opcode |


    addi rd, rs1, imm

    inst: opcode
    args: [rd, rs1, imm]

    """

    #busco los binarios de todo
    opcode = op.intructions_to_opcode[inst]
    rd = op.registers[args[0]]
    rs1 = op.registers[args[1]]
    imm = int(args[2]) 
    funct3 = op.funct3[inst]

    # armo el binario
    # estoy flasheando?
    return imm << 20 | rs1 << 15 | funct3 << 12 | rd << 7 | opcode


def b_parser(inst: str, args: list[str]) -> str:
    pass  

def s_parser(inst: str, args: list[str]) -> str:
    
    """
    Arma una instruccion de tipo s

    31        25 24    20 19    15 14     12 11    7 6       0
    | imm[11:5] | rs2    | rs1    |  funct3 | imm[4:0] | opcode |

    sb rs2, imm(rs1)
    inst: opcode
    args: [rd, rs1, imm]

    """

    pass


def j_parser(inst: str, args: list[str]) -> str:
    pass

def instruction_parser(line: str, instruction_type: str | None):
    
    # Agarro la linea y la separo
    parts = line.replace(',', ' ').split()
    instruction = parts[0].lower()
    args = parts[1:]

    print("Instruction: ", instruction)
    print("Args: ", args)

    if instruction_type == "R":
        return r_parser(instruction, args)
    elif instruction_type == "U":
        return u_parser(instruction, args)
    elif instruction_type == "I":
        return i_parser(instruction, args)
    elif instruction_type == "B":
        return b_parser(instruction, args)
    elif instruction_type == "S":
        return s_parser(instruction, args)
    elif instruction_type == "J":
        return j_parser(instruction, args)
    else:
        return "Invalid instruction type"



