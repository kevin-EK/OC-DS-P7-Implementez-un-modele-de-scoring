# I. Introduction
L’entreprise "Prêt à dépenser"  souhaite mettre en œuvre un outil de “scoring crédit” pour calculer la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé.
De plus cette entreprise souhaite plus de transparence vis-à-vis des décisions d’octroi de crédit.

Besoin de « Prêt à dépenser » :
Un modèle de scoring qui donnera la probabilité de faillite d’un client de façon automatique
Pour les besoin de transparence des chargés de relation client, il est donc nécessaire de développer un dashboard interactif.

# II. Présentation des données
Nous possédons 7 jeux de données, contentant des informations: 
  - Personnelles tels que l’âge, le sexe, l’emploi, le niveau d’éducation, nombre d’enfant, possession etc…
  - Financières tels que le revenu, le montant du prêt, historique des crédits, historiques de remboursement, historique du solde des cartes de crédits etc…

![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/35e720c9-0888-48b5-ae83-2dde2db6d1a3)

# III. Etape de modélisation
  ## Problématique :
  Le déséquilibre entre le nombre de bons et de moins bons clients doit être pris en compte pour élaborer un modèle pertinent.
  En adoptant une approche qui ne prend pas en compte ce déséquilibre des classes, on risque fortement de biaiser le modèle. 

  ## Risque :
  - **FN** => mauvais client prédit bon client : donc crédit accordé et perte en capital.
  - **FP** => bon client prédit mauvais : donc refus crédit et manque à gagner en marge.

  ## Besoin:
  ![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/6ffd1933-6979-4e94-9fca-52e7f2b327a2)

  ## Gestion du déséquilibre des classes:
  ![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/bc026cc2-2823-4269-ac97-9711c341f58a)

  ## Meilleur modèle: LightGBMClassifier

  ![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/09b4fec1-5a31-4728-a1e5-ab5c40c36200)

# IV. Présentaion de l'api et du dashboard

![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/1df60b36-0ee5-4bb2-9166-826c7de31b65)

![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/da0074b6-c333-44f6-b148-6852605145a2)

![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/3346640f-e4d4-458b-9673-349948bbbcdd)

![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/dc6edf06-0daa-4af0-b8b9-cd7278835cd3)



