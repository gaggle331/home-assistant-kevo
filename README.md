# Hass.io custom component - Kevo

## Needed python module

The ```pykevocontrol``` module is automatically installed when first used of this custom component on Hass.io.

## Kevo lock integration

Copy the files from the directories into your homeassistant directory.

```
custom_components/kevo/__init__.py
custom_components/kevo/lock.py
custom_components/kevo/manifest.json
```

congifuration.yaml file entry:
```
# Locks controls
lock:
  - platform: kevo
    email: KEVO_ACCOUNT_EMAIL         # Your Kevo account Email
    password: KEVO_ACCOUNT_PASSWORD   # Your Kevo account Password
```
