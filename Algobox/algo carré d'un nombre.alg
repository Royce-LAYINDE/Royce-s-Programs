<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="AFFICHER B"/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2lignes="" F2para="" F2defaut="" F2etat="inactif"/>
    <repere repcode="-10#10#-10#10#2#2" repetat="inactif"/>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="A EST_DU_TYPE NOMBRE" code="1#NOMBRE#A"/>
        <item algoitem="B EST_DU_TYPE NOMBRE" code="1#NOMBRE#B"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="AFFICHER &quot;Veuillez entrer un nombre A dont vous souhaiter avoir le carré&quot;" code="4#Veuillez entrer un nombre A dont vous souhaiter avoir le carré#0"/>
        <item algoitem="LIRE A" code="2#A#pasliste"/>
        <item algoitem="B PREND_LA_VALEUR A*A" code="5#B#A*A#pasliste"/>
        <item algoitem="AFFICHER &quot;Le résultat est:&quot;" code="4#Le résultat est:#0"/>
        <item algoitem="AFFICHER B" code="3#B#0#pasliste"/>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
