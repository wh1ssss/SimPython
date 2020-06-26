def Sim(VarNov):
    resp = 0
    print ("                                                                               QUESTOES                                                                 ")
    
    print ("1) Em um programa escrito em linguagem Python, o comando de atribuição x = int(5.9) fará com que a variável x passe a armazenar um valor inteiro igual a 6.")
    print ()
    print ("a) correta")
    print ("b) falsa")
    print ()
    r1 = input ("Reposta: ")
    if ( r1 == "b") :
        resp = resp + 1

    print ()
    print ("2) Considere uma String s, que armazena o valor 'ALO MUNDO'. Utilizando Python, a alternativa com as instruções que exibiriam a substring 'MU' seria:")
    print ()
    print ("a) s. substring(5,7)")
    print ("b) s[5:6]")
    print ("c) s[-5:-3]")
    print ("d) s. substr(4:6)")
    print ()
    r2 = input ("Resposta: ")
    if ( r2 == "c") :
        resp = resp + 1

    print ()
    print ("3) Considerando que em um programa Python em condições ideais há um array criado pelo comando nomes = ['Maria', 'Pedro', 'João'], para exibir os valores contidos nesse array utiliza-se:")
    print ()
    print ("a) for x in nomes: print(x)")
    print ("b) for x in nomes: out.print(x)")
    print ("c) foreach x in nomes: print(x)")
    print ("d) foreach x in nomes: system.println(x)?")
    print ()
    r3 = input ("Resposta: ")
    if ( r3 == "a" ) :
        resp = resp + 1

    print ()
    print ("4) O comando input serve para solicitar ao usuário a inserção de dados.")
    print ("a) correta")
    print ("b) falsa")
    print ()
    r4 = input ("Resposta: ")
    if (r4 == "a") :
        resp = resp + 1

    print ()
    if (resp == 1) :
        print ("Você acertou somente " , resp , " questão, estude mais e volte a fazer o simulado " + nome + ".")

    elif (resp == 2):
        print ("Você acertou somente " , resp , " questões, estude mais e volte a fazer o simulado " + nome + ".")
        
    elif (resp == 3) :
        print ("Parabéns " + nome + ", voce acertou" , resp , "questões e mandou bem mas não acertou todas, estude mais.")

    elif (resp == 4) :
        print ("Parabéns " + nome + ", você acertou todas as questões.")


nome = input ("Boa tarde, qual é o seu nome: ")
VarNov = input ("Vamos iniciar o simulado " + nome + "? ")

print ()

if ( VarNov == "Sim") :

    Sim(VarNov)

    VarNov = input ("Gostaria de fazer o questionário novamente?")

    if ( VarNov == "Sim" ):
     Sim(VarNov)
    else:
         print ("Tudo bem então " + nome + ", obrigado pela resposta")

else:
     print ("Tudo bem então " + nome + ", obrigado pela resposta")

