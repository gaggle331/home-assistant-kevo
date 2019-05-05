# homeassistant custom components - kevo

## Requirements

Make sure 'pykevocontrol' requirements installing properly in '/deps' folder. Can be found here: https://github.com/Bahnburner/pykevoplus/tree/master/pykevoplus

## Kevo lock integration

Copy the files from the directories into your homeassistant directory.

```
custom_components/kevo/__init__.py
custom_components/kevo/lock.py
```

congifuration.yaml file entry:
```
# Locks controls
lock:
  - platform: kevo
    email: KEVO_ACCOUNT_EMAIL         # Your Kevo account Email
    password: KEVO_ACCOUNT_PASSWORD   # Your Kevo account Password
```