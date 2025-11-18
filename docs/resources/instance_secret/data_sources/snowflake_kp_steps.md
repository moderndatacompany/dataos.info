# Steps to Generate and Register a Key Pair in Snowflake

## Step 1: Generate and Secure RSA Key Pair

Run the following command sequence to generate an RSA key pair in one step:

```bash
mkdir -p ~/.snowflake/keys
cd ~/.snowflake/keys

# Generate encrypted private key (recommended)
openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 des3 -inform PEM -out snowflake_rsa_key.p8

# Or, unencrypted private key (not recommended)
# openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out snowflake_rsa_key.p8 -nocrypt

# Extract public key
openssl rsa -in snowflake_rsa_key.p8 -pubout -out snowflake_rsa_key.pub

# Secure file permissions
chmod 700 ~/.snowflake ~/.snowflake/keys
chmod 600 ~/.snowflake/keys/snowflake_rsa_key.p8 ~/.snowflake/keys/snowflake_rsa_key.pub
```
When executing the above command sequence, you will be prompted to enter three types of passwords sequentially:

- **Encryption Password:** A new password to encrypt the private key.

- **Verify Encryption Password:** Re-enter the same password to confirm.

- **Passphrase Prompt:** This passphrase serves as the key to decrypt the private key during authentication.


You can use the same password for all three prompts.
However, ensure that you securely note down the passphrase, as it will be required later when configuring Snowflake authentication.


## Step 2: Retrieve the Private Key 

Run the following command to display the private key contents which will be used while creating Instance Secret:

```bash
cd ~/.snowflake/keys
cat snowflake_rsa_key.p8
```

## Step 3: Retrieve the Public Key for Snowflake

Display the public key as a single line to register in Snowflake:

```sql
awk 'NR>1 && !/-----/' ~/.snowflake/keys/snowflake_rsa_key.pub | tr -d '\n'
```

Copy the output string and use it in the next step.

## Step 4: Register the Public Key in Snowflake

Use the Snowflake account (with appropriate privileges such as ACCOUNTADMIN or SECURITYADMIN) and run:

```sql
USE ROLE ACCOUNTADMIN;
ALTER USER <snowflake-username> SET RSA_PUBLIC_KEY='MIIBIjANBgkqh...';
```

Verify that your public key has been registered successfully:

```sql
DESC USER <snowflake-username>;
```

## Step 5: (Optional) Verify the Key Fingerprint

To verify that your registered public key matches your local key, generate a fingerprint:

```bash
openssl rsa -pubin -in ~/.snowflake/keys/snowflake_rsa_key.pub -outform DER | \
openssl dgst -sha256 -binary | openssl enc -base64
```

Compare the fingerprint with the RSA_PUBLIC_KEY_FP in Snowflake (from DESC USER <your_user>).
They must match for successful authentication.

<center>
<img src="/resources/instance_secret/data_sources/sf.png" alt="Snowflake UI" style="width:40rem; border: 1px solid black; padding: 5px;" />
<figcaption><i>Snowflake UI</i></figcaption>
</center>

## Step 6: Rotate Keys (Recommended Practice)

Snowflake supports dual public keys (RSA_PUBLIC_KEY and RSA_PUBLIC_KEY_2) to allow seamless key rotation.

1. Generate a new key pair.

2. Register the new public key:

    ```sql
    ALTER USER <your_user> SET RSA_PUBLIC_KEY_2='MIIBIjANBgkqh...';
    ```

3. Update your DataOS Instance Secret with the new private key.

4. Remove the old key after successful validation:

    ```sql
    ALTER USER <your_user> UNSET RSA_PUBLIC_KEY;
    ```



    