# Hass.io custom component - Kevo

## What you need

- A Kevo smart lock
- Kevo Plus bluetooth enabled gateway
- Reference : https://www.weiserlock.com/en/kevo/smart-lock

## Needed python module

The ```pykevocontrol``` module is automatically installed when first used of this custom component on Hass.io.

## Kevo custom component setup

Copy these project files into your Home Assistant ```/config``` directory.

```
custom_components/Kevo/__init__.py
custom_components/Kevo/lock.py
custom_components/Kevo/manifest.json
```

congifuration.yaml file entry:
```
# Locks controls
lock:
  - platform: Kevo
    email: KEVO_ACCOUNT_EMAIL         # Your Kevo account Email
    password: KEVO_ACCOUNT_PASSWORD   # Your Kevo account Password
```
     
## TODOs

- 

