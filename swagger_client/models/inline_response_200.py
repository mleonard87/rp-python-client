# coding: utf-8

"""
    RepositPower External

    Unofficial RepositPower External API This API is built by hand from the description at https://api.repositpower.com/docs/ It should not be mistaken for official in any way shape or form, it's simply my attempt to document the API and build some client libraries from that. 

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


class InlineResponse200(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, rp_token=None):
        """
        InlineResponse200 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'rp_token': 'str'
        }

        self.attribute_map = {
            'rp_token': 'RP-TOKEN'
        }

        self._rp_token = rp_token


    @property
    def rp_token(self):
        """
        Gets the rp_token of this InlineResponse200.


        :return: The rp_token of this InlineResponse200.
        :rtype: str
        """
        return self._rp_token

    @rp_token.setter
    def rp_token(self, rp_token):
        """
        Sets the rp_token of this InlineResponse200.


        :param rp_token: The rp_token of this InlineResponse200.
        :type: str
        """

        self._rp_token = rp_token

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
