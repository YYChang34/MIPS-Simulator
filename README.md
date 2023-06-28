# MIPS-Simulator
The project aims to provide an efficient and simple approach to simulate a MIPS CPU to execute the series of instructions  step-by-step.
MIPSDecode
====================
Hi!<br>
**MIPSDecode** is a python based script that converts lines of MIPS code into hex and binary.

It works with all of the instructions in the "Core Instruction Set" from the MIPS reference sheet
which can be found here: http://inst.eecs.berkeley.edu/~cs61c/resources/MIPS_Green_Sheet.pdf


Instructions:
--------------------------------------------------------------------------------

To run the script, simply cd into the folder containing the files and run:
>python3 -i MIPSdecoder.py

Then type whatever line of MIPS code you wish to decode.

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
