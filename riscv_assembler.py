import opcodes.opcodes as op


def type_of_instruction(line: str) -> str:

    """
    opcode x1, ..., xn

    split() -> [opcode, x1, ..., xn] 

    agarra la instruccion -> la traduce al opcode -> devuelve el fmt
    
    """

    instruction_name = line.split()[0] 
 

    return op.instruction_to_fmt[instruction_name]

    
   


def r_parser(line: str) -> str:
    pass

def u_parser(line: str) -> str:
    pass

def i_parser(line: str) -> str:
    pass

def b_parser(line: str) -> str:
    pass

def s_parser(line: str) -> str:
    pass

def j_parser(line: str) -> str:
    pass

def instruction_parser(line: str, instruction_type: str | None):
    """
    Given the line to read and the instruction type, 
    this function will return the object that parses that 
    kind of instruction.
    """
    pass