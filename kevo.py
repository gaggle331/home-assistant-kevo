import logging

import voluptuous as vol

# Import the device class from the component that you want to support
from homeassistant.components.lock import LockDevice, PLATFORM_SCHEMA
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD, STATE_LOCKED, STATE_UNLOCKED
import homeassistant.helpers.config_validation as cv

# Home Assistant depends on 3rd party packages for API specific code.
REQUIREMENTS = ['pykevoplus==1.0.1']

ATTR_DEVICE_ID = 'device_id'

_LOGGER = logging.getLogger(__name__)

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_EMAIL): cv.string,
    vol.Required(CONF_PASSWORD): cv.string,
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the Kevo platform."""
    from pykevoplus import Kevo

    # Assign configuration variables. The configuration check takes care they are
    # present.
    email = config.get(CONF_EMAIL)
    password = config.get(CONF_PASSWORD)

    # Setup connection with devices/cloud
    kevos = Kevo.GetLocks(email, password)
    
    # Debugging
    for kevo in kevos:
    	_LOGGER.debug(kevo)

    # Add devices
    add_devices(KevoDevice(kevo) for kevo in kevos)
    



class KevoDevice(LockDevice):
    """Representation of a Kevo Lock."""
    from pykevoplus import KevoLock

    def __init__(self, kevo):
        """Initialize an Kevo Lock."""
        self._kevo = kevo
        self._name = kevo.name
        self._id = None
        self._state = None

    @property
    def name(self):
        """Return the display name of this lock."""
        return self._name
    
    @property
    def id(self):
        """Return the unique id of this lock."""
        return self._id

    @property
    def is_locked(self):
        """Return true if lock is locked."""
        return self._state
        
    @property
    def state(self) -> str:
        """Get the state of the device."""
        if self._kevo.IsLocked():
            return STATE_LOCKED
        return STATE_UNLOCKED

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
        self._state = self._kevo.GetBoltState()
        
    @property
    def device_state_attributes(self) -> dict:
        """Return the state attributes."""
        attributes = {}
        attributes[ATTR_DEVICE_ID] = self._id