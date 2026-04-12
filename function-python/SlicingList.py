my_list = [0 ,1 ,2 ,3 ,4 ,5, 6,7 ,8 ,9]
    #      0 ,1 ,2 ,3 ,4 ,5, 6 ,7 ,8 ,9
    #.   -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

    #list[start:end:step]
print(my_list[5:7:2])

print(my_list[-4])
print(my_list[-7:-2])
print(my_list[8:6])
print(my_list[2:8])
print(my_list[:])
print(my_list[-2:1:- 2])
print(my_list[::-1])

sample_url = 'http://supriyasanoj.com'
print(sample_url)


#reverse the url
print(sample_url[::-1])

#get top-level domain(TDL)
print(sample_url.split('.')[-1])
print(sample_url[-4:])

#remove  http://
print(sample_url.replace('http://',''))
print(sample_url[7:])

#print the url without the http:// or the top level domaim
print(sample_url[7:-4])