
import struct,os
filename,count_one,couont_zero='example.txt',0,0
for current_byte in list(open(filename,'rb').read()):
      count_one+=bin(struct.pack("B",current_byte)[0]).count('1')
      count_zero=os.path.getsize(filename)*8-count_one
print("one:"+str(count_one))
print("zero:"+str(count_zero))
print("one/zero:"+str(count_one/count_zero))
