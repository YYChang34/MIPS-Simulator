# MIPS-Simulator
The project aims to provide an efficient and simple approach to simulate a MIPS CPU to execute the series of instructions step-by-step.


Instructions:
--------------------------------------------------------------------------------
To get the example instructions, first download the folder **Test**. 

To run the script, simply cd into the folder containing the files and run:
>python3 -i MipsSimulator.py

Then, type the path of the download files or you can rewrite a new file with MIPS instructions.

**(The filename extention should be ".txt")**

It works with all of the instructions in the "Core Instruction Set" from the MIPS reference sheet
which can be found here: http://inst.eecs.berkeley.edu/~cs61c/resources/MIPS_Green_Sheet.pdf


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
