"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import POWER_WATT, REVOLUTIONS_PER_MINUTE
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
    """Set up the sensor platform."""
    add_entities([PoolPumpSpeedSensor(), PoolPumpPowerSensor()])


class PoolPumpSpeedSensor(SensorEntity):
    """Pool pump speed sensor."""

    _pump = pump.Pump("http://192.168.1.54")

    _attr_name = "Pool Pump Speed"
    _attr_native_unit_of_measurement = REVOLUTIONS_PER_MINUTE
    _attr_device_class = SensorDeviceClass.SPEED
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.
        """
        data = self._pump.get_data()
        self._attr_native_value = data.speed


class PoolPumpPowerSensor(SensorEntity):
    """Pool pump power sensor."""

    _pump = pump.Pump("http://192.168.1.54")

    _attr_name = "Pool Pump Power"
    _attr_native_unit_of_measurement = POWER_WATT
    _attr_device_class = SensorDeviceClass.POWER
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.
        """
        data = self._pump.get_data()
        self._attr_native_value = data.power
