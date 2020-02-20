class contraseña:
    def __init__(self,contraseña):
        self.contraseña=contraseña
    def pregunta(self):
        #real=int(input("Ingrese contraseña:"))
        contraseña=1703
        real=0
        error=0
        while(contraseña!=real | error<4):
            real=int(input("Ingrese contraseña:"))
            if(real==contraseña):
                print("\nEl sistema ha sido desbloqueado")            
            else:
                print("\nContraseña incorrecta")
                error = error + 1
                if(error==4):
                    print("\nEl sistema ha sido bloqueado por límite de intentos")
            

contraseña.pregunta(1703)
        

