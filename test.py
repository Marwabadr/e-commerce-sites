from app import db, create_app
from app.models.fournisseur import Fournisseur
from app.models.produit import Produit
from app.models.historique_ventes import HistoriqueVentes

# Créer l'application Flask
app = create_app()

# Créer un contexte d'application
with app.app_context():
    # Supprimer et recréer les tables (optionnel, pour un environnement de test)
    db.drop_all()
    db.create_all()

    # Ajouter des fournisseurs
    fournisseur1 = Fournisseur(nom="Fournisseur A", contact="contactA@example.com")
    fournisseur2 = Fournisseur(nom="Fournisseur B", contact="contactB@example.com")
    db.session.add(fournisseur1)
    db.session.add(fournisseur2)
    db.session.commit()

    # Ajouter des produits
    produit1 = Produit(
        nom="Produit 1",
        description="Description du Produit 1",
        quantite_entree=100,
        quantite_sortie=50,
        quantite_finale=50,
        seuil_reapprovisionnement=20,
        prix_unitaire=10.5,
        fournisseur_id=fournisseur1.id
    )
    produit2 = Produit(
        nom="Produit 2",
        description="Description du Produit 2",
        quantite_entree=200,
        quantite_sortie=100,
        quantite_finale=100,
        seuil_reapprovisionnement=50,
        prix_unitaire=15.0,
        fournisseur_id=fournisseur2.id
    )
    db.session.add(produit1)
    db.session.add(produit2)
    db.session.commit()

    # Ajouter des historiques de ventes
    historique1 = HistoriqueVentes(
        produit_id=produit1.id,
        mois="2024-12",
        quantite_vendue=30
    )
    historique2 = HistoriqueVentes(
        produit_id=produit2.id,
        mois="2024-12",
        quantite_vendue=50
    )
    db.session.add(historique1)
    db.session.add(historique2)
    db.session.commit()

    print("Données de test insérées avec succès!")