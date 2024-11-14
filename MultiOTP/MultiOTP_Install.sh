#!/bin/bash

mkdir /opt/multiotp

wget https://download.multiotp.net/multiotp_5.9.8.0.zip

unzip multiotp_5.9.8.0.zip -d /opt/multiotp

# Local LDAP

echo slapd slapd/internal/adminpw password rtzewrpiZRT753 | debconf-set-selections
echo slapd slapd/internal/generated_adminpw password rtzewrpiZRT753 | debconf-set-selections
echo slapd slapd/password2 password rtzewrpiZRT753 | debconf-set-selections
echo slapd slapd/password1 password rtzewrpiZRT753 | debconf-set-selections

# Downloads Requirements

apt-get update && apt-get install -y apache2-utils apt-utils build-essential bzip2 dialog dselect freeradius initramfs-tools ldap-utils libbz2-dev logrotate nano net-tools nginx-extras p7zip-full php-pear php-bcmath php-cgi php-dev php-fpm php-gd php-gmp php-ldap php8.2-sqlite3 slapd snmp snmpd sqlite3 subversion sudo unzip wget php-mbstring


# Local LDAP

chmod 777  /opt/multiopt/raspberry/boot-part/*.sh
