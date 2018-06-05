import pydasm
import binascii

#Open, and read 200 bytes out of the file,
#While converting buffer to hex string
with open('c:\\Windows\\notepad.exe','r') as f:
    buffer = binascii.hexlify(f.read(200))


#Iterate through the buffer and disassemble 
offset = 0
while offset < len(buffer):
    i = pydasm.get_instruction(buffer[offset:], pydasm.MODE_32)
  
    print pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, 0)
    
    if not i:
        break
    offset += i.length
