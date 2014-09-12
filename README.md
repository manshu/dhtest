Diffie-Hellman key exchange example in python

You can use as reference OpenSSL's dhparam module that can produce following output, e.g.

```bash
openssl dhparam 16 |openssl dhparam -noout -text
Generating DH parameters, 16 bit long safe prime, generator 2
This is going to take a long time
.++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*++*
    PKCS#3 DH Parameters: (16 bit)
        prime: 61547 (0xf06b)
        generator: 2 (0x2)
```
