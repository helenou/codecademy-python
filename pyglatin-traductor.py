'''
Le Pyg Latin est un langage dans lequel on prend la premiere lettre d\'un mot et on la place a la fin de celui-ci.
Puis on y ajoute le son \"ay\".
Par exemple, bonjour devient "onjourbay".

Les mots commencant par une consonne seront traites differemment, deplacant egalement la premiere lettre vers la fin du mot, avant d\'inclure \"ay\".
'''

pyg = 'ay'

original = raw_input('Entrez un mot :')
mot=original.lower()
if len(original) > 0 and original.isalpha():
    # Extrait la premiere lettre du mot saisi
    premiere=mot[0]
    # Cas si voyelle
    if premiere in 'aeiou':
        nouveau_mot = mot + pyg
        print nouveau_mot
    # Cas si consonne
    else:
        nouveau_mot = mot[1:len(mot)]+premiere+pyg
        print nouveau_mot

