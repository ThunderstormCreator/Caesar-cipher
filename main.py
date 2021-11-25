
text = input ("What message would you like to encript? ")
buff =""

key = input ("Type the secret key: ") 
for l in text:
  o= ord(l)
  if o in range (97, 123):
    o=o-32
  if o in range (65, 91):
    o=o+int(key)
    if o > 90:
      o=o-26
  
  l = chr (o)
  buff = buff + l
print (buff)


resp = input ("If you would like to decode it, print D ")
buff2=""
if resp == "D":
  for i in buff:
    a = ord (i)
    a= a - int (key)
    if a < 65:
      a = a+26
    k = chr (a)
    buff2 = buff2+k
  print (buff2)
else:
  print ("Keep it secret))")

#needs some polishing (with spaces in text)
