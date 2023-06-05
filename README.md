# Configure SSH with YubiKey

## Prerequisite

### Garuda Linux 

```
pacman -S openssh libfido2.so
```

## Generate SSH key

```
ssh-keygen -t ecdsa-sk -C 'your@email.com'
```

## Add SSH key on target Server

```
mkdir -p /home/user_name/.ssh && touch /home/user_name/.ssh/authorized_keys
```

```
echo 'sk-ecdsa-sha2-nistp256@openssh.com ADFAZFAZFAZFAZFAZFAZFAZFAZFAZFD45az6f4az6f74s56qf4az/faz6f4az65f4' >> /home/user_name/.ssh/authorized_keys
```

```
chmod 700 /home/user_name/.ssh && chmod 600 /home/user_name/.ssh/authorized_keys
```

```
chown -R username:username /home/username/.ssh
```
