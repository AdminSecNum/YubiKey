
# VeraCrypt

## ArchLinux

```
pacman -S ccid opensc
systemctl start pcscd.service
pcsc_scan
```

If the card reader does not have a PIN pad, append the line(s) and set enable_pinpad = false in the opensc configuration file /etc/opensc.conf.

Go to Setting -> Security tokens -> PKCS #11 Library Path -> /usr/lib/opensc-pkcs11.so


