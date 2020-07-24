import logging
import time
import voluptuous as vol

# Import the device class from the component that you want to support
from homeassistant.components.lock import LockEntity, PLATFORM_SCHEMA
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD, STATE_LOCKED
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)
CONF_LOCKS = "locks"
CONF_LOCK_ID = "lock_id"
CONF_MAX_RETRIES = "max_retries"
CONF_RETRY_DELAY = "retry_delay"

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_EMAIL): cv.string,
    vol.Required(CONF_PASSWORD): cv.string,
    vol.Required(CONF_LOCKS): vol.All(
        cv.ensure_list,
        [
            {
                vol.Required(CONF_LOCK_ID): cv.string,
                vol.Optional(CONF_MAX_RETRIES, default=3): cv.positive_int,
                vol.Optional(CONF_RETRY_DELAY, default=2): cv.positive_int
            }
        ]
    )
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the Kevo platform."""
    from pykevoplus import KevoLock

    # Assign configuration variables. The configuration check takes care they are
    # present.
    email = config.get(CONF_EMAIL)
    password = config.get(CONF_PASSWORD)
    locks = config.get(CONF_LOCKS)

    # Setup connection with devices/cloud (broken as of 9 Sep 2019 due to CAPTCHA changes)
    # kevos = Kevo.GetLocks(email, password)
    # add_devices(KevoDevice(kevo) for kevo in kevos)

    # Setup manual connection with specified device
    for lock in locks:
        lock_id = lock[CONF_LOCK_ID]
        max_retries = lock[CONF_MAX_RETRIES]
        retry_delay = lock[CONF_RETRY_DELAY]
        
        for attempt in range(max_retries):
            try:
                kevo = KevoLock.FromLockID(lock_id, email, password)
            except:
                if attempt == max_retries - 1:
                    raise
                else:
                    time.sleep(retry_delay)
            else:
                break
        
        add_devices([KevoDevice(kevo)])

class KevoDevice(LockEntity):
    """Representation of a Kevo Lock."""

    def __init__(self, kevo):
        """Initialize an Kevo Lock."""
        self._kevo = kevo
        self._name = kevo.name
        self._state = None

    @property
    def name(self):
        """Return the display name of this lock."""
        return self._name

    @property
    def is_locked(self):
        """Return true if lock is locked."""
        return self._state == STATE_LOCKED

    def lock(self, **kwargs):
        """Instruct the lock to lock."""
        self._kevo.Lock()

    def unlock(self, **kwargs):
        """Instruct the lock to unlock."""
        self._kevo.Unlock()

    def update(self):
        """Fetch new state data for this lock.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._kevo.EndSession()
        self._state = self._kevo.GetBoltState().lower()
