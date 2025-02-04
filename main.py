import riscv_assembler as rasm


if __name__ == "__main__":

    assembly_lines = [
        "sub x3, x1, x2",
        "add x3, x1, x2",
        "xor x3, x1, x2",
        "addi x1, x2, 8",
        "sb x2, 3(x7)",
        "beq  x3, x4, 0x535",
        "bne  x1, x2, 0x458",
        "auipc x2, 0x8000",
        "jal x2, 0x454",
        "lui x1, 0x42",
    ]

    for line in assembly_lines:
        #aca consigo el fmt "R, U, B, etc"
        instruction_type = rasm.type_of_instruction(line)
        
        #aca consigo el codigo que va a leer la maquina
        machine_code = rasm.instruction_parser(line, instruction_type)
        
        print(f"machine code: {instruction_type} # assembly line: {line}")

