# Criado por : Lucas gabriel
# github : https://github.com/Lucas836-hub/
# instagram : @lucas_git

# Calculadora de degraus v0.3
import os
import math
import turtle
class main():
    def __init__(self):

        self.titulo("CALCULADORA DE DEGRAIS")
        print("Olá, seja bem vindo\nvamos ajuda-lo a saber sobre seus degrais\n")
        print("Digite o comprimendo da escada")
        c=self.valor()
        print("\nDigite a altura da escada")
        a=self.valor()
        ang=(a/c)
        #print(ang)
        tabela_final=self.calc_ang(ang,3)

        print("\nO que você quer descobrir ?")
        print("\nDigite 1 - Para a altura\n       2 - Para o comprimento ")
        r=self.imput(2)
        self.limpar()
        q_degrau=0
        comprimento_degrau=0
        altura_degrau=0
        if r == 0:
            print("Digite o tamanho do degrau (em cm)")
            tam=self.valor()
            comprimento_degrau=tam
            tam=tam/100

            self.limpar()
            self.titulo("RESULTADO FINAL")
            print("A escada vai ter :")
            q_degrau=int(c//tam)
            hj = tabela_final[3] * tam
            altura_degrau = hj * 100
            print(f"{q_degrau} degrais")
            print(f"\nCom sobra de comprimento de {self.numb_valor((c /tam)-(c // tam))} cm")
            print(f"Com sobra de altura de {self.numb_valor((a / hj) - (a // hj))} cm")

            print(f"\nCom comprimento {self.numb_valor(tam*100)} cm")
            print(f"Degrais com altura de {self.numb_valor(altura_degrau)}cm")

            print(f"\nA rampa vai ter um comprimento de {self.numb_valor(math.sqrt((c**2+a**2)))} m")
            print(f"O ângulo de inclinação da rampa é de {self.numb_valor(tabela_final[0])}º graus")
            pcl=((a-2)/hj)*tam

            print(f"\nA distancia para ter uma altura livre de 2 m do teto a escada á : {self.numb_valor(pcl)}m")
            pcl = ((a - 1.8) / hj) * tam
            print(f"A distancia para ter uma altura livre de 1,80 m do teto a escada á : {self.numb_valor(pcl)}m")

        else:
            print("Digite a altura do degrau (em cm)")
            tam = self.valor()
            altura_degrau=tam
            tam = tam / 100

            self.limpar()
            self.titulo("RESULTADO FINAL")
            print("A escada vai ter :")
            q_degrau=int(a // tam)
            hj = tam/tabela_final[3]
            comprimento_degrau=hj*100
            print(f"{q_degrau} degrais")
            print(f"\nCom sobra de altura de {self.numb_valor((a / tam) - (a // tam))} cm")
            print(f"Com sobra de comprimento de {self.numb_valor((c / hj) - (c // hj))} cm")

            print(f"\nCom altura {self.numb_valor(tam * 100)} cm")
            print(f"Degrais com comprimento de {self.numb_valor(hj*100)}cm")

            print(f"\nA rampa vai ter um comprimento de {self.numb_valor(math.sqrt((c ** 2 + a ** 2)))} m")
            print(f"O ângulo de inclinação da rampa é de {tabela_final[0]}º graus")

            pcl = ((a - 2) / tam) * hj
            print(f"\nA distancia para ter uma altura livre de 2 m do teto a escada á : {self.numb_valor(pcl)}m")
            pcl = ((a - 1.8) / tam) * hj
            print(f"A distancia para ter uma altura livre de 1,80 m do teto a escada á : {self.numb_valor(pcl)}m")

        print(f"\nMedidas da Escada= {c}m x {a}m")
        print(f"Medidas do Degrau= {self.numb_valor(comprimento_degrau)}cm x {self.numb_valor(altura_degrau)}cm\n")
        self.titulo("FINISH")

        print(f"Você quer ver o desenho da escada ?")
        print("\nDigite 1 - Para a Sim\n       2 - Para Não ")
        r = self.imput(2)
        if r==0:
            l1 = []
            # Fazendo os degrais
            comprimento_matriz = -310 + comprimento_degrau
            altura_matriz = 0 - altura_degrau
            #print(f"c+a {comprimento_degrau} + {altura_degrau}  = {comprimento_matriz} + {altura_matriz}")
            # Fazendo o triangulo
            #altura
            l1.append([-310,0])
            #l1.append([-300,-(q_degrau)*altura_degrau])
            l1.append([-310, -a*100])
            #comprimento
            #l1.append([-300+(comprimento_degrau*(q_degrau)),-(q_degrau)*altura_degrau])
            l1.append([-310 + c*100, -a*100])
            l1.append([-310,0])

            # montando a escada
            comprimento_matriz -= comprimento_degrau
            altura_matriz += altura_degrau
            for gh in range(0,q_degrau):
                comprimento_matriz+=comprimento_degrau
                l1.append([comprimento_matriz, altura_matriz])
                altura_matriz-=altura_degrau
                l1.append([comprimento_matriz,altura_matriz])

            self.drawseg(l1)
            turtle.mainloop()

    def drawseg(self,l):
        turtle.pu()
        turtle.goto(l[0][0], l[0][1])
        turtle.pd()
        for a, b in l[1:]:
            turtle.goto(a, b)

    def calc_ang(self,g,sct):
        # g = grau de inclinação / sct = seno cosseno tangente 1 2 3 respctivamente
        valor_ang=[[1 ,0.0175 , 0.9998 , 0.0175],
[2, 0.0349, 0.9994, 0.0349],
[3, 0.0523, 0.9986, 0.0524],
[4, 0.0698,	0.9976,	0.0699],
[5, 0.0872,	0.9962,	0.0875],
[6, 0.1045,	0.9945, 0.1051],
[7, 0.1219 ,0.9925,	0.1228],
[8, 0.1392, 0.9903, 0.1405],
[9,	0.1564,	0.9877,	0.1584],
[10, 0.1736, 0.9848, 0.1763],
[11, 0.1908, 0.9816, 0.1944],
[12, 0.2079, 0.9781, 0.2126],
[13, 0.2250, 0.9744, 0.2309],
[14, 0.2419, 0.9703, 0.2493],
[15, 0.2588, 0.9659, 0.2679],
[16, 0.2756, 0.9613, 0.2867],
[17, 0.2924, 0.9563, 0.3057],
[18, 0.3090, 0.9511, 0.3249],
[19, 0.3256, 0.9455, 0.3443],
[20, 0.3420, 0.9397, 0.3640],
[21, 0.3584, 0.9336, 0.3839],
[22, 0.3746, 0.9272, 0.4040],
[23, 0.3907, 0.9205, 0.4245],
[24, 0.4067, 0.9135, 0.4452],
[25, 0.4226, 0.9063, 0.4663],
[26, 0.4384, 0.8988, 0.4877],
[27, 0.4540, 0.8910, 0.5095],
[28, 0.4695, 0.8829, 0.5317],
[29, 0.4848, 0.8746, 0.5543],
[30, 0.5000, 0.8660, 0.5774],
[31, 0.5150, 0.8572, 0.6009],
[32, 0.5299, 0.8480, 0.6249],
[33, 0.5446, 0.8387, 0.6494],
[34, 0.5592, 0.8290, 0.6745],
[35, 0.5736, 0.8192, 0.7002],
[36, 0.5878, 0.8090, 0.7265],
[37, 0.6018, 0.7986,0.7536],
[38,0.6157,	0.7880,	0.7813],
[39,0.6293,	0.7771,	0.8098],
[40,0.6428,	0.7660,	0.8391],
[41,0.6561,	0.7547,	0.8693],
[42,0.6691,	0.7431,	0.9004],
[43,0.6820,	0.7314,	0.9325],
[44,0.6947,	0.7193,	0.9657],
[45,0.7071,	0.7071,	1],
[46,0.7193,	0.6947,	1.0355],
[47,0.7314,	0.6820,	1.0724],
[48,0.7431,	0.6691,	1.1106],
[49,0.7547,	0.6561,	1.1504],
[50,0.7660,	0.6428,	1.1918],
[51,0.7771,	0.6293,	1.2349],
[52,0.7880,	0.6157,	1.2799],
[53, 0.7986,	0.6018,	1.3270],
[54,0.8090,	0.5878,	1.3764],
[55,0.8192,	0.5736,	1.4281],
[56,0.8290,	0.5592,	1.4826],
[57,0.8387,	0.5446,1.5399],
[58,0.8480,	0.5299,	1.6003],
[59,0.8572,	0.5150,	1.6643],
[60,0.8660, 0.5000,	1.7321],
[61,0.8746, 0.4848,	1.8040],
[62,0.8829, 0.4695,	1.8807],
[63,0.8910, 0.4540,	1.9626],
[64,0.8988, 0.4384,	2.0503],
[65,0.9063, 0.4226,	2.1445],
[66,0.9135, 0.4067,2.2460],
[67,0.9205, 0.3907,	2.3559],
[68,0.9272, 0.3746,	2.4751],
[69,0.9336, 0.3584,	2.6051],
[70,0.9397, 0.3420,2.7475],
[71, 0.9455, 0.3256,	2.9042],
[72,0.9511, 0.3090,	3.0777],
[73,0.9563, 0.2924,	3.2709],
[74,0.9613, 0.2756,	3.4874],
[75,0.9659, 0.2588,	3.7321],
[76,0.9703, 0.2419,4.0108],
[77,0.9744, 0.2250,	4.3315],
[78,0.9781, 0.2079,	4.7046],
[79,0.9816, 0.1908,	5.1446],
[80,0.9848, 0.1736,	5.6713],
[81,0.9877, 0.1564,	6.3138],
[82,0.9903, 0.1392,	7.1154],
[83,0.9925, 0.1219,	8.1443],
[84,0.9945, 0.1045,	9.5144],
[85,0.9962, 0.0872,	11.4301],
[86,0.9976, 0.0698,	14.3007],
[87,0.9986, 0.0523,	19.0811],
[88,0.9994, 0.0349,28.6363],
[89,0.9998, 0.0175,	57.2900],
[90,1, 	0, 	None ]]
        v_final=[100,100,100,100]
        v_min=100
        for a in range(0,len(valor_ang)-1):
            b=valor_ang[a][sct]-g
            #print(f"\033[33m{valor_ang[a][sct]} - {g}  ==  {valor_ang[a][sct]-g}\033[m")
            if b <= v_min and b >= 0 :
                #print("\033[96m entrou\033[m",end="",flush=True)
                #print("\033[91m*\033[m"*50)
                for d in range(0,4):
                    v_final[d]=valor_ang[a][d]
                v_min=valor_ang[a][sct] - g

        #print(f"\033[31mo valor final deu : {v_final}\033[m")
        #h = g * tam
        return v_final
    def valor(self):
        while True:
            n=input("Digite o valor : ")
            n=self.num(n)[0]
            try:
                n=float(n)
            except:
                print("ERRO VALOR INVALIDO ! DIGITE NOVAMENTE")
            else:
                break
        n = float(n)
        return n

    def imput(self, qt=0):
        while True:
            try:
                k = int(input('Digite sua escolha >>> \033[92m'))
            except ValueError:
                print('\033[91mERRO : caractere invalido !\033[m')
            else:
                if (k < 1 or k > qt):
                    print('\033[91mERRO : opção invalida !\033[m')
                else:
                    print("\033[m")
                    return k - 1

    def limpar(self):
        os.system("clear")

    def titulo(self, text=''):
        print('\033[96m_' * 50)
        print()
        print(text.center(50))
        print('\033[96m_\033[m' * 50)
        print()

    def quitar(self):
        exit()


    def numb_valor(self, g):
        g = f"{float(g):.2f}"
        g = str(g).replace(".", ",").strip()
        g.replace(" ", "").replace("  ", "")
        if (g == ""):
            return 0
        else:
            if (len(g) - 1 - g.find(",") < 2):
                g += "0"

            m = 0
            if (len(g) - 3 > 3):
                m = len(g) - 3
                l = list(g)
                while (m > 2):
                    m -= 3
                    l.insert(m, " ")
                r = ""
                for kl in range(0, len(l)):
                    r += str(l[kl])
                g = r
            return g


    def num(self, o):
        t = []
        i = str(o).replace(",", ".")
        kl = list(i)
        i = ""
        for c in range(0, len(kl)):
            if (kl[c] != " "):
                i += kl[c]
        try:
            p = float(i)
        except:
            t.append(i)
            t.append("false")
            return t
        else:
            i = float(f'{float(i):.2f}')
            t.append(float(i))
            t.append("true")
            return t


    def imput(self, qt=0):
        while True:
            try:
                k = int(input('Digite sua escolha >>> \033[92m'))
            except ValueError:
                print('\033[91mERRO : caractere invalido !\033[m')
            else:
                if (k < 1 or k > qt):
                    print('\033[91mERRO : opção invalida !\033[m')
                else:
                    print("\033[m")
                    return k - 1


main()