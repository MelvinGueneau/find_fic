import os

def search_files_in_current_directory(filename):
    current_directory = os.path.dirname(__file__)
    return search_files(current_directory, filename)

def search_files(directory, filename):
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for file in filenames:
            if file == filename:
                matches.append(os.path.join(root, file))
    return matches

filename = ""
filename = input("Nom du fichier que vous chercher :")

results = search_files_in_current_directory(filename)

if results:
    print("Fichiers trouvés :")
    for file_path in results:
        print(file_path)
else:
    print("Aucun fichier trouvé.")


#                                               
#                                                ██████████████                          
#                                        ████████▓▓▓▓██░░░░██▓▓████                      
#                                ████████░░░░░░░░██▓▓██░░░░██▓▓▓▓▓▓██                    
#                            ████░░██▓▓▓▓██░░░░░░██▓▓▓▓██░░██▓▓▓▓▓▓▓▓██                  
#                        ████░░░░░░░░██▓▓▓▓██░░░░██▓▓▓▓██░░██▓▓▓▓▓▓▓▓██                  
#                      ██▓▓▓▓██░░░░░░░░██▓▓▓▓██░░██▓▓▓▓██░░██▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓██░░░░░░██▓▓▓▓██░░██▓▓▓▓██░░██▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓▓▓██░░░░██▓▓▓▓██░░██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓██░░██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                      
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                        
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                            
#                      ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                                
#                          ████████▓▓▓▓▓▓▓▓▓▓▓▓██████                                    
#                                  ████████████           