"""Switch setup for our Integration."""

from homeassistant.components.switch import (
    SwitchDeviceClass, 
    SwitchEntity
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from emaux_client import pump

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the switch platform."""
    add_entities([PoolPumpSwitch()], update_before_add=True)

class PoolPumpSwitch(SwitchEntity):
    """Pool pump switch."""

    _pump = pump.Pump("http://192.168.1.54")

    _attr_name = "Pool Pump"
    _attr_device_class = SwitchDeviceClass.SWITCH

    async def async_update(self, **kwargs: Any) -> None:
        data = self._pump.get_data()
        self._attr_is_on = data.on
    
    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the entity on."""
        self._pump.turn_on

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the entity off."""
        self._pump.turn_off