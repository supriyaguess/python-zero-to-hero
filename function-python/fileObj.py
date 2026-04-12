# File Objects 
# with open('demo.txt','r') as f:  # dont need to close it close itslef
#     size_to_read = 10
#     f_contests = f.read(size_to_read)

#     print(f.tell())
#     f.seek(0)

    
#     while len(f_contests) > 0:
#         print(f_contests, end='*')
#         f_contests = f.read(size_to_read)
#    # pass
    #f_contests = f.readlines() #read line s
#     f_contests = f.read(100) 
#     print(f_contests, end='')
#     # print(f.readline)

#     for line in f:
#         print(line,end='')

# #f = open('demo.txt','r')  # read

  #  print(f.name)
 #   print(f.mode) #read
#f.close() # need to clod=se manually
#print(f.closed)   #true

#print(f.read)

#write
with open('test.txt','w') as test:
    test.write('Test')
    test.seek(0)
    test.write('R')
    with open('test_copy.txt','w') as wf:
        for line in test:
            wf.write(line)