# -*- coding: UTF-8 -*-

import os

def create_respostas(archive):
    '''
    (file) -> none (file)

    input a text archive and the program will scrap all the
    formulated answer and save it in a new file with the respective
    number

    >>>create_questoes("adm.txt")
    >>>

    '''
    ## given file, opening to read it
    txt = '/Users/t316775/Downloads/'+archive+".txt"
    fp = open (txt, 'r')

    ## creating temp file
    temp_file = '/Users/t316775/Downloads/temp.txt'
    temp = open (temp_file, 'w')
    
    ## creating file to write into
    novo_arquivo = '/Users/t316775/Downloads/'+ archive + "_explicacoes.txt"
    final = open(novo_arquivo, "w")

    ## Counter for the questions and pages read
    ## The pages counter is used to remove such number when encountered
    ## during the parsing
    questao = 1
    pagina = 4
    counter_1001 = 0

    ## The text as encountered by python, without propor decoding
    #bad_text = "1001 QuestÃµes Comentadas - Direito Administrativo - CESPE" 
    #bad_text2 = "Leandro Cadenas Prado & PatrÃ­cia Carla de Farias Teixeira"

    ## Creating loop tto go through the lines
    for line in fp:

        if counter_1001 == 0 and "1001 Ques" in line:
            for line in fp:
                author = line
                break
         
        ## Establishing when to start copying the text
        if ("Errado." in line) or ("Correto." in line) or ("Errada." in line)\
           or ("Correta." in line) or "Anulado." in line or "Anulada." in line:
            #temp.write("\n")
            temp.write("Resposta " + str("%03d" % questao) + " ")
            temp.write(line.replace("\n", " ").replace((str(questao)+"."), ""))
            questao += 1

            
            for line in fp:
                ## if period and line break encountered, copy line and break loop
                if (".  "+"\n") in line or (".  "+"\n") in line or (".   "+"\n") in line\
                or (". "+"\n") in line or (".    "+"\n") in line or ("."+"\n") in line:
                    temp.write(line)
                    break

                ## if "(grifou-se)" encountered break loop
                elif "(grifou-se)" in line:
                    temp.write(line)
                    break
                ##
                elif ("” " +"\n") in line or ("’" +"\n") in line\
                or ("’ " +"\n") in line or ("”  " +"\n") in line:
                    temp.write(line)
                    break

                   
                ##
                elif (": " +"\n") in line:
                    temp.write(line)
                    break
                
                ## if line has "Comentadas - Direito" it is the page header
                ## omit such line and continue loop
                elif "Comentadas - Direito" in line:
                    temp.write("")
                    continue
                ## if line has "Leandro Cadenas Prado" it is the page header
                ## omit such line
                elif author in line:
                    temp.write("")
                    continue
                ## if line has pagina number and line break it is a page ending
                ## increase counter of page and omit such number
                elif (str(pagina)+("\n")) in line:
                    temp.write("")
                    pagina +=1
                    continue
                
                ## if no stoping point encountered copy line, without page break
                else:
                    temp.write(line.replace("\n", " "))


    ## Closing temp file and openning it on read only mode
    temp.close()
    temp = open(temp_file, "r")
    
    ## Creating loop to copy from the temp file to definitive file
    ## without unnecessary white spaces
    for line in temp:
        if (".  "+"\n") in line or (".  "+"\n") in line or (".   "+"\n") in line\
                or (". "+"\n") in line or (".    "+"\n") in line\
                or ("."+"\n") in line:
            final.write(' '.join(line.split()))
            final.write("\n")
        else:
            final.write(' '.join(line.split()))
            #final.write(line.replace("  "," "))

    ## close opened files
    fp.close()
    final.close()
    temp.close()

    ## Deleting temp file
    os.remove(temp_file)


if __name__ == "__main__":
    create_respostas("Direito Constitucional - CESPE")
