# Hass.io custom component - Kevo

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

Update: As of 9 Sep 2019, pykevoplus:Kevo.GetLocks() can no longer pull lock ids due to CAPTCHA changes. This fork does NOT pull lock ids, but rather requires you to specify one specific lock via the lock_id attribute in order to connect a Kevo lock to Home Assistant.

## What you need

- A Kevo smart lock
- Kevo Plus bluetooth enabled gateway
- Reference : https://www.weiserlock.com/en/kevo/smart-lock

## Needed python module

The ```pykevocontrol``` module is automatically installed when first used of this custom component on Hass.io.

## Kevo custom component setup

This component can be added by adding the GitHub repository URL into the HACS system.

Alternatively, you can copy these project files into your Home Assistant ```/config``` directory:

```
custom_components/Kevo/__init__.py
custom_components/Kevo/lock.py
custom_components/Kevo/manifest.json
```

Once installed, add this to your congifuration.yaml file:
```
# Locks controls
lock:
  - platform: Kevo
    email: KEVO_ACCOUNT_EMAIL         # Your Kevo account Email
    password: KEVO_ACCOUNT_PASSWORD   # Your Kevo account Password
    lock_id: KEVO_LOCK_ID             # Your Kevo lock id (obtained manually from kevo website*)
    max_retries: 3                    # Optionally set how many times it should try to initalise the lock
    retry_delay: 2                    # Optionally set the delay (in seconds) between each retry
```
\* You can get the lock IDs manually by logging into mykevo.com, click Details for the lock, click Settings, the lock ID is on the right.
     
## TODOs

- handle multiple kevo locks with the same or different account credentials
- set friendly name for devices

