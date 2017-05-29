# coding: utf-8

"""
    RepositPower External

    Unofficial RepositPower External API This API is built by hand from the description at https://api.repositpower.com/docs/ It should not be mistaken for official in any way shape or form, it's simply my attempt to document the API and build some client libraries from that.  This API is demonstrably wrong around authentication - please read the official docco at the link above for accurate details. It will login, but all the login options are not captured - I wasn't clear how to write up both basic and token login being available on all URLs (ie. how to make auth an either/or rather than a both).  This API is also not completed yet. I'm missing a bunch of 200 responses for the calls I haven't tested yet. 

    OpenAPI spec version: 1.0.0
    Contact: kevin@littlejohn.id.au
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class InlineResponse2003Data(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ac_dc=None, battery=None, dc_coupled=None, frequency_trigger=None, inverter=None, load_meter=None, load_phases=None, solar_meter=None, solar_phases=None, solar_streams_ac=None, solar_streams_dc=None):
        """
        InlineResponse2003Data - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ac_dc': 'bool',
            'battery': 'bool',
            'dc_coupled': 'bool',
            'frequency_trigger': 'bool',
            'inverter': 'bool',
            'load_meter': 'bool',
            'load_phases': 'list[str]',
            'solar_meter': 'bool',
            'solar_phases': 'list[str]',
            'solar_streams_ac': 'object',
            'solar_streams_dc': 'object'
        }

        self.attribute_map = {
            'ac_dc': 'ac_dc',
            'battery': 'battery',
            'dc_coupled': 'dc_coupled',
            'frequency_trigger': 'frequency_trigger',
            'inverter': 'inverter',
            'load_meter': 'load_meter',
            'load_phases': 'load_phases',
            'solar_meter': 'solar_meter',
            'solar_phases': 'solar_phases',
            'solar_streams_ac': 'solar_streams_ac',
            'solar_streams_dc': 'solar_streams_dc'
        }

        self._ac_dc = ac_dc
        self._battery = battery
        self._dc_coupled = dc_coupled
        self._frequency_trigger = frequency_trigger
        self._inverter = inverter
        self._load_meter = load_meter
        self._load_phases = load_phases
        self._solar_meter = solar_meter
        self._solar_phases = solar_phases
        self._solar_streams_ac = solar_streams_ac
        self._solar_streams_dc = solar_streams_dc


    @property
    def ac_dc(self):
        """
        Gets the ac_dc of this InlineResponse2003Data.


        :return: The ac_dc of this InlineResponse2003Data.
        :rtype: bool
        """
        return self._ac_dc

    @ac_dc.setter
    def ac_dc(self, ac_dc):
        """
        Sets the ac_dc of this InlineResponse2003Data.


        :param ac_dc: The ac_dc of this InlineResponse2003Data.
        :type: bool
        """

        self._ac_dc = ac_dc

    @property
    def battery(self):
        """
        Gets the battery of this InlineResponse2003Data.


        :return: The battery of this InlineResponse2003Data.
        :rtype: bool
        """
        return self._battery

    @battery.setter
    def battery(self, battery):
        """
        Sets the battery of this InlineResponse2003Data.


        :param battery: The battery of this InlineResponse2003Data.
        :type: bool
        """

        self._battery = battery

    @property
    def dc_coupled(self):
        """
        Gets the dc_coupled of this InlineResponse2003Data.


        :return: The dc_coupled of this InlineResponse2003Data.
        :rtype: bool
        """
        return self._dc_coupled

    @dc_coupled.setter
    def dc_coupled(self, dc_coupled):
        """
        Sets the dc_coupled of this InlineResponse2003Data.


        :param dc_coupled: The dc_coupled of this InlineResponse2003Data.
        :type: bool
        """

        self._dc_coupled = dc_coupled

    @property
    def frequency_trigger(self):
        """
        Gets the frequency_trigger of this InlineResponse2003Data.


        :return: The frequency_trigger of this InlineResponse2003Data.
        :rtype: bool
        """
        return self._frequency_trigger

    @frequency_trigger.setter
    def frequency_trigger(self, frequency_trigger):
        """
        Sets the frequency_trigger of this InlineResponse2003Data.


        :param frequency_trigger: The frequency_trigger of this InlineResponse2003Data.
        :type: bool
        """

        self._frequency_trigger = frequency_trigger

    @property
    def inverter(self):
        """
        Gets the inverter of this InlineResponse2003Data.


        :return: The inverter of this InlineResponse2003Data.
        :rtype: bool
        """
        return self._inverter

    @inverter.setter
    def inverter(self, inverter):
        """
        Sets the inverter of this InlineResponse2003Data.


        :param inverter: The inverter of this InlineResponse2003Data.
        :type: bool
        """

        self._inverter = inverter

    @property
    def load_meter(self):
        """
        Gets the load_meter of this InlineResponse2003Data.


        :return: The load_meter of this InlineResponse2003Data.
        :rtype: bool
        """
        return self._load_meter

    @load_meter.setter
    def load_meter(self, load_meter):
        """
        Sets the load_meter of this InlineResponse2003Data.


        :param load_meter: The load_meter of this InlineResponse2003Data.
        :type: bool
        """

        self._load_meter = load_meter

    @property
    def load_phases(self):
        """
        Gets the load_phases of this InlineResponse2003Data.


        :return: The load_phases of this InlineResponse2003Data.
        :rtype: list[str]
        """
        return self._load_phases

    @load_phases.setter
    def load_phases(self, load_phases):
        """
        Sets the load_phases of this InlineResponse2003Data.


        :param load_phases: The load_phases of this InlineResponse2003Data.
        :type: list[str]
        """

        self._load_phases = load_phases

    @property
    def solar_meter(self):
        """
        Gets the solar_meter of this InlineResponse2003Data.


        :return: The solar_meter of this InlineResponse2003Data.
        :rtype: bool
        """
        return self._solar_meter

    @solar_meter.setter
    def solar_meter(self, solar_meter):
        """
        Sets the solar_meter of this InlineResponse2003Data.


        :param solar_meter: The solar_meter of this InlineResponse2003Data.
        :type: bool
        """

        self._solar_meter = solar_meter

    @property
    def solar_phases(self):
        """
        Gets the solar_phases of this InlineResponse2003Data.


        :return: The solar_phases of this InlineResponse2003Data.
        :rtype: list[str]
        """
        return self._solar_phases

    @solar_phases.setter
    def solar_phases(self, solar_phases):
        """
        Sets the solar_phases of this InlineResponse2003Data.


        :param solar_phases: The solar_phases of this InlineResponse2003Data.
        :type: list[str]
        """

        self._solar_phases = solar_phases

    @property
    def solar_streams_ac(self):
        """
        Gets the solar_streams_ac of this InlineResponse2003Data.


        :return: The solar_streams_ac of this InlineResponse2003Data.
        :rtype: object
        """
        return self._solar_streams_ac

    @solar_streams_ac.setter
    def solar_streams_ac(self, solar_streams_ac):
        """
        Sets the solar_streams_ac of this InlineResponse2003Data.


        :param solar_streams_ac: The solar_streams_ac of this InlineResponse2003Data.
        :type: object
        """

        self._solar_streams_ac = solar_streams_ac

    @property
    def solar_streams_dc(self):
        """
        Gets the solar_streams_dc of this InlineResponse2003Data.


        :return: The solar_streams_dc of this InlineResponse2003Data.
        :rtype: object
        """
        return self._solar_streams_dc

    @solar_streams_dc.setter
    def solar_streams_dc(self, solar_streams_dc):
        """
        Sets the solar_streams_dc of this InlineResponse2003Data.


        :param solar_streams_dc: The solar_streams_dc of this InlineResponse2003Data.
        :type: object
        """

        self._solar_streams_dc = solar_streams_dc

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
