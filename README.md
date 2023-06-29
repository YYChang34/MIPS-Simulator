# MIPS-Simulator
The project aims to provide an efficient and simple approach to simulate a MIPS CPU to execute the series of instructions step-by-step. Simultaneously, it can also observe that each block of CPU how to work and its overall executed process.

Modes:
--------------------------------------------------------------------------------
(1) Single Instruction mode:

You can type whatever line of MIPS code you wish to decode and it will help you to have a better understanding of MIPS ISA and the executed result.

(2) Mutiple Instruction mode:

You can put the series of instructions into the program and it will execute the instructions step-by-step. Then you can apparently observe that the overall executed process of MIPS CPU and each block of CPU how to work, and also can understand how to transform MIPS instructions into machine code.

Instructions:
--------------------------------------------------------------------------------
To get the example instructions, first of all download the folder **Example**.

It works with all of the instructions in the "Core Instruction Set" from the MIPS reference sheet
which can be found here: http://inst.eecs.berkeley.edu/~cs61c/resources/MIPS_Green_Sheet.pdf

To run the script, simply cd into the folder containing the files and run:
>python3 -i MipsSimulator.py

In Single Instruction mode, type whatever line of MIPS code you wish to decode.

In Multiple Instruction mode, type the datapath of the download files or you can rewrite a new file with MIPS instructions.
**(Be careful to the filename extention should be ".txt")**

Example Output:
--------------------------------------------------------------------------------
<blockquote>
<p>Type MIPS code here: add $t0 $t0 $t0</p>

<p>Function type: R-Type<br>
Instruction form:  opcode  /  rs / rt / rd / shamt / funct<br>
Formatted binary: 000000 /  01000 / 01000 / 01000 / 00000 / 100000<br>
Binary:           0b00000001000010000100000000100000<br>
Hex:              0x01084020</p>
</blockquote>
--------------------------------------------------------------------------------
<blockquote>
<p>Type MIPS code here: addi $t0 $t0 1</p>

<p>Function type: I-Type<br>
Instruction form:  opcode / rs / rt / immediate  <br>    
Formatted binary: 001000 / 01000 / 01000 / 0000000000000001<br>
Binary:           0b00100001000010000000000000000001<br>
Hex:              0x21080001</p>
</blockquote>
--------------------------------------------------------------------------------
<blockquote>
<p>Type MIPS code here: j 0x4</p>

<p>Function type: I-Type<br>
Instruction form: opcode /         immediate       <br>    
Formatted binary: 000010 / 00000000000000000000000100<br>
Binary:           0b00001000000000000000000000000100<br>
Hex:              0x08000004<p>
</blockquote>
--------------------------------------------------------------------------------
<blockquote>
<p>Type MIPS code here: asdf</p>

</p>Not a valid MIPS statement</p>
</blockquote>
