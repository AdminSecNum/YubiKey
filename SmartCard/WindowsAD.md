# Pré-requis

- Drivers yubikey
- CRL disponible
- L'AC doit être sur tout les postes + NTAuth 'dspublish'

# Certificat LDAPS DC

* Authentification du serveur (1.3.6.1.5.5.7.3.1)
* Ouverture de session par carte à puce (1.3.6.1.4.1.311.20.2.2)

* KeyUsage = 0xf0

SAN :
* FQDN
* Domain.com
* ldap.domain.com
* ldaps.domain.com

# Certificats utilisateurs

* Messagerie électronique sécurisée (1.3.6.1.5.5.7.3.4)
* Signature de liste d’approbation Microsoft (1.3.6.1.4.1.311.10.3.1)
* Système de fichiers EFS (Encrypting File System) (1.3.6.1.4.1.311.10.3.4)
* Système de sécurité IP en fin de chaîne (1.3.6.1.5.5.7.3.5)
* Fin du tunnel de sécurité IP (1.3.6.1.5.5.7.3.6)
* Utilisateur de sécurité IP (1.3.6.1.5.5.7.3.7)
* Authentification du client (1.3.6.1.5.5.7.3.2)
* Ouverture de session par carte à puce (1.3.6.1.4.1.311.20.2.2)
* Chiffrement de lecteur BitLocker (1.3.6.1.4.1.311.67.1.1)

* KeyUsage = 0xf0

* SAN = UPN + Email

# GPO

`SSI - Cartes à puce`
* Ordinateur, Paramètre Windows, PAramètre de sécurité, Stratégies Local, Options de sécurité, Ouverture de session interactive : Comportement lrosque la carte à puce est retirer : Verouiller la station
* Ordinateur, Modèle d'administration, Composant windows, Carte à puce, Autoriser l'utilisation de certificat ECC

# Utilisateur

* Crée un mappage fort certificat - Utilisateur
* Cocher 'Authentification par carte à puce"

# Debug

Sur le DC voir dans système -> source KDC

Vérifié la carte à puce : `certutil -scinfo`
Vérifié le DC : `certutil -dcinfo`
