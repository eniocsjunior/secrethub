# Secrethub
Creation and verification of cryptographic keys.

## How to use

To instantiate a Secret class you must first have a key:
```python
>>> from secrethub import Secret
>>> new_key = Secret.new()
>>> new_secret
'UEGVN46SwIOyQCneO-sudqDRlqbM3Td8ygozeoWqY2A='
>>> secret = Secret(key=new_key)
```
Now you can encrypt and decrypt messages:
```python
>>> message = 'Hello Secret'
>>> encrypted_message = secret.encrypt(message)
>>> encrypted_message
'gAAAAABnVgxFcin82sXSGvZH5Uwia4KDewcK3xk5Kbwiv2Uk95GLXwj0pVxReoQi04M9SJZ6yiYxGp8e6o8j9k0DiBWdEZWOLg=='
>>> secret.decrypt(encrypted_message)
'Hello Secret'
```
You can also hash passwords and verify them:
```python
>>> password = '57r0n6p4$5W0rD4n07h1n6'
>>> hashed_password = secret.hash(password)
>>> hashed_password
'$argon2id$v=19$m=65536,t=3,p=4$JB0aad1g1h01VrUK46iv2w$/8Sw0taHXdVi2tBFA4hRaBHPcx8JtJ7Qq71X46TWpP4'
>>> secret.verify(hashed_password, password)
True
```
You can also use this module via the command line:
```bash
$ python -m secrethub

How to use:
python -m secrethub [option]

Options:
new                     Generate new cryptographic key.
encrypt [message]       Encrypt message
decrypt [key]           Decrypt key
hash [password]
verify [hash] [password]

$
```
