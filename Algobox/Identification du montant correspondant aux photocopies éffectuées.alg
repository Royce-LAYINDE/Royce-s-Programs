<?xml version="1.0" encoding="UTF-8"?>
<Algo>
    <description texte="" courant="AFFICHER B"/>
    <extension extnom="inactif"/>
    <fonction fctetat="inactif" fctcode=""/>
    <F2 F2defaut="" F2etat="inactif" F2para="" F2lignes=""/>
    <repere repetat="inactif" repcode="-10#10#-10#10#2#2"/>
    <item algoitem="VARIABLES" code="100#declarationsvariables">
        <item algoitem="A EST_DU_TYPE NOMBRE" code="1#NOMBRE#A"/>
        <item algoitem="B EST_DU_TYPE NOMBRE" code="1#NOMBRE#B"/>
        <item algoitem="C EST_DU_TYPE CHAINE" code="1#CHAINE#C"/>
        <item algoitem="D EST_DU_TYPE NOMBRE" code="1#NOMBRE#D"/>
    </item>
    <item algoitem="DEBUT_ALGORITHME" code="101#debutalgo">
        <item algoitem="AFFICHER &quot;Veuiller écrire le nombre de photocopies éffectuées(A)&quot;" code="4#Veuiller écrire le nombre de photocopies éffectuées(A)#0"/>
        <item algoitem="LIRE A" code="2#A#pasliste"/>
        <item algoitem="SI (A&lt;=10) ALORS" code="6#A&lt;=10">
            <item algoitem="DEBUT_SI" code="7#debutsi"/>
            <item algoitem="B PREND_LA_VALEUR 2" code="5#B#2#pasliste"/>
            <item algoitem="AFFICHER &quot;Le prix unitaire en fcfa des photocopies éffectuées est:&quot;" code="4#Le prix unitaire en fcfa des photocopies éffectuées est:#0"/>
            <item algoitem="AFFICHER B" code="3#B#1#pasliste"/>
            <item algoitem="AFFICHER &quot;Désirer vous connaitre le montant total des photocopies éffectuées? Réponder 1 pour oui et 0 pour non&quot;" code="4#Désirer vous connaitre le montant total des photocopies éffectuées? Réponder 1 pour oui et 0 pour non#1"/>
            <item algoitem="LIRE C" code="2#C#pasliste"/>
            <item algoitem="SI (C==1) ALORS" code="6#C==1">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="D PREND_LA_VALEUR A*B" code="5#D#A*B#pasliste"/>
                <item algoitem="AFFICHER &quot;Le montant total en fcfa des photocopies éffectuées est:&quot;" code="4#Le montant total en fcfa des photocopies éffectuées est:#0"/>
                <item algoitem="AFFICHER D" code="3#D#0#pasliste"/>
                <item algoitem="FIN_SI" code="8#finsi"/>
            </item>
            <item algoitem="SI (C==0) ALORS" code="6#C==0">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="AFFICHER &quot;D'accord&quot;" code="4#D'accord#0"/>
                <item algoitem="FIN_SI" code="8#finsi"/>
            </item>
            <item algoitem="SI (C>1) ALORS" code="6#C>1">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="AFFICHER &quot;Erreur de saisie. Réponder par 1 ou 0&quot;" code="4#Erreur de saisie. Réponder par 1 ou 0#0"/>
                <item algoitem="LIRE C" code="2#C#pasliste"/>
                <item algoitem="SI (C==1) ALORS" code="6#C==1">
                    <item algoitem="DEBUT_SI" code="7#debutsi"/>
                    <item algoitem="D PREND_LA_VALEUR A*B" code="5#D#A*B#pasliste"/>
                    <item algoitem="AFFICHER &quot;Le montant total en fcfa des photocopies éffectuées est:&quot;" code="4#Le montant total en fcfa des photocopies éffectuées est:#0"/>
                    <item algoitem="AFFICHER D" code="3#D#0#pasliste"/>
                    <item algoitem="FIN_SI" code="8#finsi"/>
                </item>
                <item algoitem="SI (C==0) ALORS" code="6#C==0">
                    <item algoitem="DEBUT_SI" code="7#debutsi"/>
                    <item algoitem="AFFICHER &quot;D'accord&quot;" code="4#D'accord#0"/>
                    <item algoitem="FIN_SI" code="8#finsi"/>
                </item>
                <item algoitem="FIN_SI" code="8#finsi"/>
            </item>
            <item algoitem="FIN_SI" code="8#finsi"/>
        </item>
        <item algoitem="SI (A>10 ET A&lt;=20) ALORS" code="6#A>10 ET A&lt;=20">
            <item algoitem="DEBUT_SI" code="7#debutsi"/>
            <item algoitem="B PREND_LA_VALEUR 1.5" code="5#B#1.5#pasliste"/>
            <item algoitem="AFFICHER &quot;Le prix unitaire en fcfa des photocopiées éffectuées est:&quot;" code="4#Le prix unitaire en fcfa des photocopiées éffectuées est:#0"/>
            <item algoitem="AFFICHER B" code="3#B#1#pasliste"/>
            <item algoitem="AFFICHER &quot;Désirer vous connaitre le montant total des photocopies éffectuées? Réponder 1 pour oui et 0 pour non&quot;" code="4#Désirer vous connaitre le montant total des photocopies éffectuées? Réponder 1 pour oui et 0 pour non#1"/>
            <item algoitem="LIRE C" code="2#C#pasliste"/>
            <item algoitem="SI (C==1) ALORS" code="6#C==1">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="D PREND_LA_VALEUR A*B" code="5#D#A*B#pasliste"/>
                <item algoitem="AFFICHER &quot;Le montant total en fcfa des photocopies éffectuées est:&quot;" code="4#Le montant total en fcfa des photocopies éffectuées est:#0"/>
                <item algoitem="AFFICHER D" code="3#D#0#pasliste"/>
                <item algoitem="FIN_SI" code="8#finsi"/>
            </item>
            <item algoitem="SI (C==0) ALORS" code="6#C==0">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="AFFICHER &quot;D'accord&quot;" code="4#D'accord#0"/>
                <item algoitem="FIN_SI" code="8#finsi"/>
            </item>
            <item algoitem="SI (C>1) ALORS" code="6#C>1">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="AFFICHER &quot;Erreur de saisie. Réponder par 1 ou 0&quot;" code="4#Erreur de saisie. Réponder par 1 ou 0#0"/>
                <item algoitem="LIRE C" code="2#C#pasliste"/>
                <item algoitem="SI (C==1) ALORS" code="6#C==1">
                    <item algoitem="DEBUT_SI" code="7#debutsi"/>
                    <item algoitem="D PREND_LA_VALEUR A*B" code="5#D#A*B#pasliste"/>
                    <item algoitem="AFFICHER &quot;Le montant total en fcfa des photocopies éffectuées est:&quot;" code="4#Le montant total en fcfa des photocopies éffectuées est:#0"/>
                    <item algoitem="AFFICHER D" code="3#D#0#pasliste"/>
                    <item algoitem="FIN_SI" code="8#finsi"/>
                </item>
                <item algoitem="SI (C==0) ALORS" code="6#C==0">
                    <item algoitem="DEBUT_SI" code="7#debutsi"/>
                    <item algoitem="AFFICHER &quot;D'accord&quot;" code="4#D'accord#0"/>
                    <item algoitem="FIN_SI" code="8#finsi"/>
                </item>
                <item algoitem="FIN_SI" code="8#finsi"/>
            </item>
            <item algoitem="FIN_SI" code="8#finsi"/>
        </item>
        <item algoitem="SI (A>20) ALORS" code="6#A>20">
            <item algoitem="DEBUT_SI" code="7#debutsi"/>
            <item algoitem="B PREND_LA_VALEUR 1" code="5#B#1#pasliste"/>
            <item algoitem="AFFICHER &quot;Le prix unitaire en fcfa des photocopies éffectués est:&quot;" code="4#Le prix unitaire en fcfa des photocopies éffectués est:#0"/>
            <item algoitem="AFFICHER B" code="3#B#1#pasliste"/>
            <item algoitem="AFFICHER &quot;Désirer vous connaitre le montant total des photocopies éffectuées? Réponder 1 pour oui et 0 pour non&quot;" code="4#Désirer vous connaitre le montant total des photocopies éffectuées? Réponder 1 pour oui et 0 pour non#1"/>
            <item algoitem="LIRE C" code="2#C#pasliste"/>
            <item algoitem="SI (C==1) ALORS" code="6#C==1">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="D PREND_LA_VALEUR A*B" code="5#D#A*B#pasliste"/>
                <item algoitem="AFFICHER &quot;Le montant total en fcfa des photocopies éffectuées est:&quot;" code="4#Le montant total en fcfa des photocopies éffectuées est:#0"/>
                <item algoitem="AFFICHER D" code="3#D#0#pasliste"/>
                <item algoitem="FIN_SI" code="8#finsi"/>
            </item>
            <item algoitem="SI (C==0) ALORS" code="6#C==0">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="AFFICHER &quot;D'accord&quot;" code="4#D'accord#0"/>
                <item algoitem="FIN_SI" code="8#finsi"/>
            </item>
            <item algoitem="SI (C>1) ALORS" code="6#C>1">
                <item algoitem="DEBUT_SI" code="7#debutsi"/>
                <item algoitem="AFFICHER &quot;Erreur de saisie. Réponder par 1 ou 0&quot;" code="4#Erreur de saisie. Réponder par 1 ou 0#0"/>
                <item algoitem="LIRE C" code="2#C#pasliste"/>
                <item algoitem="SI (C==1) ALORS" code="6#C==1">
                    <item algoitem="DEBUT_SI" code="7#debutsi"/>
                    <item algoitem="D PREND_LA_VALEUR A*B" code="5#D#A*B#pasliste"/>
                    <item algoitem="AFFICHER &quot;Le montant total en fcfa des photocopies éffectuées est:&quot;" code="4#Le montant total en fcfa des photocopies éffectuées est:#0"/>
                    <item algoitem="AFFICHER D" code="3#D#0#pasliste"/>
                    <item algoitem="FIN_SI" code="8#finsi"/>
                </item>
                <item algoitem="SI (C==0) ALORS" code="6#C==0">
                    <item algoitem="DEBUT_SI" code="7#debutsi"/>
                    <item algoitem="AFFICHER &quot;D'accord&quot;" code="4#D'accord#0"/>
                    <item algoitem="FIN_SI" code="8#finsi"/>
                </item>
                <item algoitem="FIN_SI" code="8#finsi"/>
            </item>
            <item algoitem="FIN_SI" code="8#finsi"/>
        </item>
    </item>
    <item algoitem="FIN_ALGORITHME" code="102#finalgo"/>
</Algo>
