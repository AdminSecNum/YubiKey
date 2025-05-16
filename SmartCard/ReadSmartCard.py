'''
pip install python-pkcs11 cryptography
apt install opensc yubico-piv-tool ykcs11
apt install ykcs11
systemctl start pcscd
find / -name libykcs11.so 2>/dev/null
/usr/lib/x86_64-linux-gnu/libykcs11.so
'''
import pkcs11
from pkcs11 import Attribute, ObjectClass, PKCS11Error
from cryptography import x509
from cryptography.x509 import NameOID

# Chemin de la bibliothèque PKCS#11
lib_path = "/usr/lib/x86_64-linux-gnu/libykcs11.so"
lib = pkcs11.lib(lib_path)

# Détection du token
tokens = list(lib.get_tokens())
if not tokens:
    raise Exception("Aucune YubiKey détectée.")
token = tokens[0]

pin = input("Entrez votre PIN YubiKey : ")

try:
    with token.open(user_pin=pin) as session:
        # Récupérer le certificat du slot 9a (standard)
        certs = session.get_objects({
            Attribute.CLASS: ObjectClass.CERTIFICATE,
            Attribute.LABEL: "X.509 Certificate for PIV Authentication"  # Label commun
        })

        cert = next(certs)
        cert_der = cert[Attribute.VALUE]

        # Parser le certificat
        parsed_cert = x509.load_der_x509_certificate(cert_der)
        cn = parsed_cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)[0].value
        print(f"Common Name (CN) : {cn}")

except PKCS11Error as e:
    if "CKR_PIN_INCORRECT" in str(e):
        print("PIN incorrect.")
    else:
        print(f"Erreur PKCS#11 : {e}")
except StopIteration:
    print("Aucun certificat trouvé dans le slot 9a.")
except Exception as e:
    print(f"Erreur inattendue : {e}")
