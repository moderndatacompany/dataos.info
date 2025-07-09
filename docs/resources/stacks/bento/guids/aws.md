# Amazon Web Services

There are many components within Bento which utilize AWS services. You will find that each of these components contains a configuration section under the field credentials, of the format:

```yaml
credentials:
  profile: ""
  id: ""
  secret: ""
  token: ""
  role: ""
  role_external_id: ""
```

This section contains many fields and it isn't immediately clear which of them are compulsory and which aren't. This document aims to make it clear what each field is responsible for and how it might be used.

## None of these fields are compulsory
The first thing to make clear is that all of these fields are optional. When all fields are left blank Bento will attempt to load credentials from a shared credentials file (`~/.aws/credentials`). The profile loaded will be `default` unless the `AWS_PROFILE` environment variable is set.

## Explicit Credentials
By explicitly setting the credentials you are using at the component level it's possible to connect to components using different accounts within the same Bento process.

### **Selecting a Profile**

If you are using your shared credentials file but wish to explicitly select a profile set the profile field:

```yaml
credentials:
  profile: foo
```

### **Manual**

If you are using long term credentials for your account you only need to set the fields id and secret:

```yaml
credentials:
  id: foo     # aws_access_key_id
  secret: bar # aws_secret_access_key
```

If you are using short term credentials then you will also need to set the field token:

```yaml
credentials:
  id: foo     # aws_access_key_id
  secret: bar # aws_secret_access_key
  token: baz  # aws_session_token
```

## Assuming a Role

It's also possible to configure Bento to assume a role using your credentials by setting the field role to your target role ARN.

```yaml
credentials:
  role: fooarn # Role ARN
```

This does NOT require explicit credentials, but it's possible to use both.

If you need to assume a role owned by another organization they might require you to [provide an external ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html), in which case place it in the field role_external_id:

```yaml
credentials:
  role: fooarn # Role ARN
  role_external_id: bar_id
```