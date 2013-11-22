def final_txt (name_file):
    ## path to documents
    path = "/Users/t316775/Downloads/Site/"

    ## subject name
    materia = "teste"
    #materia = name_file

    ## opening the files
    explicacao = open(path+materia+"_explicacoes.txt", "r")
    questoes = open(path+materia+"_questoes.txt", "r")
    respostas = open(path+materia+"_respostas.txt", "r")
    materias = open(path+materia+"_materias.txt", "r")

    ##opening new file
    final = open(path+materia+"_final.txt", "w")

    subject = 0

    for i in range(1,11):

        subject = qual_a_materia(i)
        
        final.write(' '.join(questoes.readline().split()).replace("Questao "+"%03d" % i, ""))
        final.write("\t")
        final.write(' '.join(explicacao.readline().split()).replace("Resposta "+"%03d" % i, ""))
        final.write("\t")
        final.write(' '.join(respostas.readline().split()).replace("Resposta "+"%03d" % i, ""))
        final.write("\t")
        final.write('CESPE')
        final.write("\t")
        final.write(str(subject))
        final.write("\n")


    ## closing all files
    explicacao.close()
    questoes.close()
    respostas.close()
    materias.close()
    final.close()


def qual_a_materia(i):

    subject = 0
    
    if i < 6:
        subject = 1
    elif i > 5 and i < 11:
        subject = 2

    return subject
        
    
