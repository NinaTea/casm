import riscv_assembler as rasm


if __name__ == "__main__":

    with open("input/r_types.asm", "r") as f:
        assembly_lines = f.readlines()
        
        for line in assembly_lines:
            instruction_type = rasm.type_of_instruction(line)

            # dada la linea y el tipo, 
            # tengo que generar esa linea en binario
            # linea -> tipo -> tipo del parser que tengo que usar para esa instruccion? -> codigo en binario
            # -> lo outputeo en un archivo
            machine_code = rasm.instruction_parser(line, instruction_type) 

            print(f"machine code: {bin(machine_code)} # assembly line: {line}")
            print()