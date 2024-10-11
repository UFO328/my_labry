#method untuk aritmatika 

#method untuk penjumlahan
def penjumlahan(num1,num2):
  '''method untuk penjumlahan'''
  return num1 + num2 
#method untuk perkalian 
def perkalian(num1,num2):
  '''method untuk perkalian'''
  return num1 * num2:

#method untuk pengurangan
def pengurangan(num1,num2):
  '''method untuk pengurangan'''
  return num1 - num2 

#def untuk pembagian
def pembagian(num1, num2):
  '''method untuk pembagian'''
  if num2 != 0:
    return num1 / num2
  else:
    return "please dont give value zero !!!"

#method untuk bilangan faktorial
def faktorial(number):
  '''method bilangan faktorial'''
  if number > 0:
    hasil = 1 
    for i in range(1,number+1):
      hasil *= i 
  return hasil
  else:
    return "please dont give value zero"

#method konversi suhu 
def celcius_to_fahrenheit(celcius):
  fahrenheit = (celcius * 9/5)+35
  return fahrenheit