# -*- coding: UTF-8 -*-

def certo_errado(archive):
    '''
    (file) -> none (file)

    input a text archive and the program will scrap all the
    answers and save it in a new file with the respective
    number

    >>>certo_errado("adm.txt")
    >>>

    '''
    ## given file, opening to read it
    txt = '/Users/t316775/Downloads/'+archive
    fp = open (txt, 'r')
    
    ## creating file to write into
    novo_arquivo = '/Users/t316775/Downloads/'+ "certo_errado_"+archive
    qp = open(novo_arquivo, "w")

    ## Counter for the questions and pages read
    ## The pages counter is used to remove such number when encountered
    ## during the parsing
    questao = 1
    
    
    ## The text as encountered by python, without propor decoding
    #bad_text = "1001 QuestÃµes Comentadas - Direito Administrativo - CESPE" 
    #bad_text2 = "Leandro Cadenas Prado & PatrÃ­cia Carla de Farias Teixeira"

    ## Creating loop to go through the lines
    for line in fp:
         
        ## Establishing when to start copying the text
        if ("Errado." in line) or ("Correto." in line) or ("Errada." in line) or ("Correta." in line):
            #qp.write("\n")
            qp.write("Resposta " + str("%03d" % questao) + " ")
            questao += 1
            if ("Errado." in line) or ("Errada." in line):
                qp.write("Errado")
                qp.write("\n")
            else:
                qp.write("Certo")
                qp.write("\n")
            
            for line in fp:
                ## if period and line break encountered, copy line and break loop
                if (".  "+"\n") in line or (".  "+"\n") in line or (".   "+"\n") in line\
                or (". "+"\n") in line or (".    "+"\n") in line or ("."+"\n") in line:
                    break

                ## if "(grifou-se)" encountered break loop
                elif "(grifou-se)" in line:
                    break
                ##
                elif ("” " +"\n") in line or ("’" +"\n") in line\
                or ("’ " +"\n") in line or ("”  " +"\n") in line:
                    break

                   
                ##
                elif (": " +"\n") in line:
                    break
                
                    
    ## close opened files
    fp.close()
    qp.close()


if __name__ == "__main__":
    certo_errado("Drt_Adm_Cespe.txt")
