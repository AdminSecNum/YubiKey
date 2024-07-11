# OpenVPN

```
dev tun
persist-tun
persist-key
data-ciphers AES-128-GCM:AES-128-CBC
data-ciphers-fallback AES-128-GCM
auth SHA256
tls-client
client
#resolv-retry infinite
remote 10.10.1.1 1194 udp4  #IP address or FQDN
lport 0
verify-x509-name "Your 'Server certificate' name from OpenVPN settings"
auth-user-pass
remote-cert-tls server
comp-lzo adaptive
#compress 
passtos

connect-retry 5 300
connect-retry-max 1
resolv-retry 15
connect-timeout 10

reneg-sec 36000    # this may need to be set to zero (0) or it may fail trying to ask for smartcard PIN on regen

pkcs11-providers ..\\bin\\opensc-pkcs11.dll  # this is from the OpenSC installer and is the only file needed
pkcs11-id 'piv_II/PKCS\x2315\x20emulated/YourSerialIDHere/Your\x20Token\x20ID\x20Here/01'
 
<ca>
-----BEGIN CERTIFICATE-----
Your AD CA or whichever CA public key here defined in 'Peer Certificate Authority' from OpenVPN settings
-----END CERTIFICATE-----
</ca>

key-direction 1
<tls-auth>
#
# 2048 bit OpenVPN static key
#
-----BEGIN OpenVPN Static key V1-----
Your key here
-----END OpenVPN Static key V1-----
</tls-auth>

```
