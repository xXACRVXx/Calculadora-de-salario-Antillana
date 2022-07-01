# "D:Abrahan SGESTMAN\Nueva carpeta\python\bin\python.exe" C:\d\cal.py

# Codigo extendido artificialmente para que mi jefe crea que estoy haciendo algo :) 

import os
import time

version = "v1.03"

os.system("cls")
print(f"--------------------------------------------©-Abrahan-2022--{version}------")
print("CALCULADORA DE SALARIO:                                           ")
print("-----------------------------------------------------------------------\n")


# Aqui se llevan a cabo los calculos
def calculadora(diast, sal_dias):    
    if sal_dias > 1000:
        sal_dias = sal_dias / 190.6
        sal_dias = sal_dias * 8
    
    sal_mes = diast * sal_dias
    impuestos1 = 5 * sal_mes / 100
    
    if sal_mes >= 3260:
    
        resto = sal_mes - 3260   
    
        impuestos2 = 3 * resto / 100
    
        sal_real = sal_mes - impuestos1 - impuestos2
    
        r =sal_real
        
        return r

    else:
        sal_real = sal_mes - impuestos1

        r =sal_real
        
        return r
  
  
if __name__ == "__main__":
    
    # Menu de opciones XD
    print("---------------------------------------------------------")
    config = str(input("Para calcular el salario precione           |Enter/Intro|\n---------------------------------------------------------\nPara calcular salario + vacasiones esriba   |     1     |\n---------------------------------------------------------\nPara configurar el idioma/lenguaje presione |     2     |\n---------------------------------------------------------\nPara cerrar la app escriba                  |    exit   |\n---------------------------------------------------------\nEscriba aqui: "))
    
    # Bucle principal
    while True:
        
        # Calculo de salario + vacasiones
        if config == "1":
            os.system("cls")
        
            print(f"--------------------------------------------©-Abrahan-2022--{version}------")
            print("CALCULADORA DE SALARIO:                                           ")
            print("-----------------------------------------------------------------------\n")
        
            diast = (input("\nDias trabajados: "))
            
            if str(diast).__contains__("exit"):
                os.system("cls")
                exit()
        
            sal_dias = (input("\nSalario diario o mensual: "))
        
            if str(sal_dias).__contains__("exit"):
                os.system("cls")
                exit()
        
            if str(sal_dias).__contains__(","):
                sal_dias=sal_dias.replace(",",".")
            
            vacasiones = (input("\nvacasiones: (proximamente) "))
            
            if str(vacasiones).__contains__("exit"):
                os.system("cls")
                exit()
        
            os.system("cls")
        
            print(f"--------------------------------------------©-Abrahan-2022--{version}------")
            print("CALCULADORA DE SALARIO:                                           ")
            print("-----------------------------------------------------------------------\n")
        
            try:            
                diast = int(diast)
                sal_dias = float(sal_dias)
                
                # 
                result = calculadora(diast, sal_dias)
            
                print("-------------------------------------")
                print('\nSalario a cobrar = ' , result , '\n')
                print("-------------------------------------")
        
            except:
                print("ERROR: NO SE ADMITEN LETRAS, SOLO NUMEROS")
                input

        
        
        
        if str(config).__contains__("exit"):
                os.system("cls")
                exit()

        if config == "2":
            os.system("cls")
        
            print(f"--------------------------------------------©-Abrahan-2022--{version}------")
            print("CALCULADORA DE SALARIO:                                           ")
            print("-----------------------------------------------------------------------\n")
            input("proximamente")
            exit()
            
        
        else:
        
            os.system("cls")
        
            print(f"--------------------------------------------©-Abrahan-2022--{version}------")
            print("CALCULADORA DE SALARIO:                                           ")
            print("-----------------------------------------------------------------------\n")
            
            diast = (input("\nDias trabajados: "))
            if str(diast).__contains__("exit"):
                os.system("cls")
                exit()
        
            sal_dias = (input("\nSalario diario o mensual: "))
        
            if str(sal_dias).__contains__("exit"):
                os.system("cls")
                exit()
        
            if str(sal_dias).__contains__(","):
                sal_dias=sal_dias.replace(",",".")
            
            os.system("cls")
        
            print(f"--------------------------------------------©-Abrahan-2022--{version}------")
            print("CALCULADORA DE SALARIO:                                           ")
            print("-----------------------------------------------------------------------\n")
        
            try:            
                diast = int(diast)
                sal_dias = float(sal_dias)
                result = calculadora(diast, sal_dias)
            
                print("-------------------------------------")
                print('\nSalario a cobrar = ' , result , '\n')
                print("-------------------------------------")
                input()
        
            except:
                print("ERROR: NO SE ADMITEN LETRAS, SOLO NUMEROS")
                input()

        
