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
  **FN** - mauvais client prédit bon client : donc crédit accordé et perte en capital
  **FP** - bon client prédit mauvais : donc refus crédit et manque à gagner en marge

  ## Besoin:
![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/986f2530-4f71-4e45-b7c7-43734ab3c9bc)

![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/7f3c6824-a3e2-4462-9a66-f0e33d693e43)
![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/e5397cba-8b79-454d-b964-ace7c4692e9c)


![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/3cd086d8-faa7-4425-9916-41d1e868b103)


![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/044cd05c-f82b-4b97-9840-4121c7404a0d)

![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/964c0d66-bd10-47c8-b84d-d59008b9bfb4)

# IV. Présentaion de l'api et du dashboard

![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/1df60b36-0ee5-4bb2-9166-826c7de31b65)

![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/da0074b6-c333-44f6-b148-6852605145a2)

![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/3346640f-e4d4-458b-9673-349948bbbcdd)

![image](https://github.com/kevin-EK/OC-DS-P7-Implementez-un-modele-de-scoring/assets/69479292/dc6edf06-0daa-4af0-b8b9-cd7278835cd3)



