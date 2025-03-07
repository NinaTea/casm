# Hay cosas que dejo porque capaz me sirven a futuro
# de ultima, los borro

FMT = {
    "R": ["add", "sub", "xor", "or", "and", "sll", "srl", "slt", "sltu"],
    "I": ["addi", "xori", "ori", "andi", "slti", "sltiu", "slli", "srli"],
    "I_l": ["lb", "lh", "lw", "lbu", "lhu"],
    "I_j": ["jalr"],
    "I_e": ["ecall", "ebreak"],
    "S": ["sb", "sh", "sw"],
    "B": ["beq", "bne", "blt", "bge", "bltu", "bgeu"],
    "U": ["lui", "auipc"],
    "J": ["jal"],
    }

intructions_to_opcode = {
    "add": 0b0110011,
    "sub": 0b0110011,
    "xor": 0b0110011,
    "or": 0b0110011,
    "and": 0b0110011,
    "sll": 0b0110011,
    "srl": 0b0110011,
    "slt": 0b0110011,
    "sltu": 0b0110011,
    "addi": 0b0010011,
    "xori": 0b0010011,
    "ori": 0b0010011,
    "andi": 0b0010011,
    "slti": 0b0010011,
    "sltiu": 0b0010011,
    "slli": 0b0010011,
    "srli": 0b0010011,

    "lb": 0b0000011,
    "lh": 0b0000011,
    "lw": 0b0000011,
    "lbu": 0b0000011,
    "lhu": 0b0000011,

    "ecall": 0b1110011,
    "ebreak": 0b1110011,

    "sb": 0b0100011,
    "sh": 0b0100011,
    "sw": 0b0100011,

    "beq": 0b1100011,
    "bne": 0b1100011,
    "blt": 0b1100011,
    "bge": 0b1100011,
    "bltu": 0b1100011,
    "bgeu": 0b1100011,

    "lui": 0b0110111,
    "auipc": 0b0010111,

    "jalr": 0b1100111,

    "jal": 0b1101111,
}

instruction_to_fmt = {
    "add": "R",
    "sub": "R",
    "xor": "R",
    "or": "R",
    "and": "R",
    "sll": "R",
    "srl": "R",
    "slt": "R",
    "sltu": "R",

    "addi": "I",
    "xori": "I",
    "ori": "I",
    "andi": "I",
    "slti": "I",
    "sltiu": "I",
    "slli": "I",
    "srli": "I",
    "lb": "I",
    "lh": "I",
    "lw": "I",
    "lbu": "I",
    "lhu": "I",
    "jalr": "I",
    "ecall": "I",
    "ebreak": "I",

    "sb": "S",
    "sh": "S",
    "sw": "S",
    "beq": "B",
    "bne": "B",
    "blt": "B",
    "bge": "B",
    "bltu": "B",
    "bgeu": "B",

    "lui": "U",
    "auipc": "U",

    "jal": "J",

    "jalr": "I",
    "ecall": "I",
    "ebreak": "I",
}


# pseudo instruction breaked down in their
# respective instructions in order to be parsed
# TODO: usar regex
pesudo_instructions = {}

# en binario
opcodes = {
    "R": 0b0110011,
    "I": {  "other": 0b0010011, 
          
            "lb": 0b0000011,
            "lw": 0b0000011,
            "lbu": 0b0000011,
            "lh": 0b0000011,
            "lhu": 0b0000011,
            "jalr": 0b1100111,
            
            "ecall": 0b1110011,
            "ebreak": 0b1110011, 
        },
    "S": 0b100011,
    "B": 0b1100011,
    "U": {"lui": 0b0110111,
           "auipc": 0b010111},
    "J": 0b1101111,
    }

funct3 = {
    "add": 0b000,
    "sub": 0b000,
    "xor": 0b100,
    "or": 0b110,
    "and": 0b111,
    "sll": 0b001,
    "srl": 0b101,
    "sra": 0b101,
    "slt": 0b010,
    "sltu": 0b011,
    "addi": 0b000,
    "xori": 0b100,
    "ori": 0b110,
    "andi": 0b111,
    "slti": 0b010,
    "sltiu": 0b011,
    "slli": 0b001,
    "srli": 0b101,
    "lb": 0b000,
    "lh": 0b001,
    "lw": 0b010,
    "lbu": 0b100,
    "lhu": 0b101,
    "jalr": 0b000,
    "ecall": 0b000,
    "ebreak": 0b000,
    "sb": 0b000,
    "sh": 0b001,
    "sw": 0b010,
    "beq": 0b000,
    "bne": 0b001,
    "blt": 0b100,
    "bge": 0b101,
    "bltu": 0b110,
    "bgeu": 0b111,
    "lui": 0b000,
    "auipc": 0b000,
    "jal": 0b000,
}

funct7 = {
    "add":0b000_0000,
    "sub": 0b010_0000,
    "xor": 0b000_0000,
    "or": 0b000_0000,
    "and": 0b000_0000,
    "sll": 0b000_0000,
    "srl": 0b000_0000,
    "slt": 0b000_0000,
    "sra": 0b010_0000,
}



# Explicacion:
# https://youtu.be/kOHB85vDuow?si=cMTdogXHRaGKuIha 


# abi to binary
registers = {
    "zero": 0b00000,
    "ra": 0b00001,
    "sp": 0b00010,
    "gp": 0b00011,
    "tp": 0b00100,
    "t0": 0b00101,
    "t1": 0b00110,
    "t2": 0b00111,
    "s0": 0b01000,
    "s1": 0b01001,
    "a0": 0b01010,
    "a1": 0b01011,
    "a2": 0b01100,
    "a3": 0b01101,
    "a4": 0b01110,
    "a5": 0b01111,
    "a6": 0b10000,
    "a7": 0b10001,
    "s2": 0b10010,
    "s3": 0b10011,
    "s4": 0b10100,
    "s5": 0b10101,
    "s6": 0b10110,
    "s7": 0b10111,
    "s8": 0b11000,
    "s9": 0b11001,
    "s10": 0b11010,
    "s11": 0b11011,
    "t3": 0b11100,
    "t4": 0b11101,
    "t5": 0b11110,
    "t6": 0b11111,
}