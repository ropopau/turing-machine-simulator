# SIMULATEUR D'UNE MACHINE DE TURING
## Utilisation
 * Le makefile peut ne pas fonctionner si vous avez une ver
 * Si vous êtes sur linux, utilisez la commande make. 
 * Sinon vous pouvez l'exécuter manuellement à partir du dossier racine "TDL".
 *
        python -m unittest
        python src/main.py
 * Il y a des messages d'erreurs pour la plupart des erreurs. Cependant il se peut que certaines soient passés à la trappe. Voici les messages d'erreurs contenus dans le fichier main.py:
 *          0: "La machine n'appelle aucune machine.",
            1: "Il n'existe pas de fichier correspondant à la machine appelée dans le répertoire.",
            2: "Veuillez ajouter les fichiers *.tur nécessaire pour utiliser le linker.",
            100: "Erreur de syntaxe dans l'entête.", 
            101: "Une transition est présente plus qu'une fois.", 
            102: "Erreur de syntaxe dans une transitions.",
            103: "Nombre de ruban incorrect",
            105: "Il y un appel de machine. Utilisez d'abord le linker pour éxécuter cette machine.",
            7: "Il y a un appel de machine. Veuillez utiliser le linker avant d'utiliser cette fonctionnalité."
            
## Interface
#### L'interface affiche 4 options: 

        Utiliser le linker: L
        Exécuter une machine: E
        Optimiser un code de turing: O
        Quitter: Q

 * Le linker permet de créer un fichier contenant le code d'une machine équivalente à la machine choisi. Si la machine choisie possède plusieurs appels de machine, alors il "fusionnera" tout ces machines ensemble.
 * La deuxième option permet d'exécuter une machine choisie. Si elle n'est pas utilisable, alors cela renvoie le code d'erreur adapté.
 * L'optimisation nous donne le choix entre trois options. La simplification, la suppresion des codes morts ou les deux. On privilégiera naturellement la troisième option qui permet de faire les deux en même temps.
 * 
        Simplifier: S
        Elimination: E
        Les deux: B
 * Quitter permet de quitter l'application
 
### Système de fichier
 * Les fichiers contenant le code d'une machine de turing ont l'extensions ".tur" pour une question de facilité d'utilisation.
 * Un fichier possède une entête avec toute les informations. Ces informations sont toute les lignes commençant par "&".
 * Les transitions reprennent la syntaxe du site turingmachinesimulator.com.
 * Les machines de turing basique comme retour à droite, retour à droite etc, sont situés dans le dossier ./turs. Lors de l'utilisation du linker, le programme cherchera les machines appelantes dans ce dossier.
 
    
