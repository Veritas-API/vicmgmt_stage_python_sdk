# coding: utf-8

"""
    Veritas Information Classifier (VIC)

    APIs

    OpenAPI spec version: Resource Specific
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TagsCollection(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, total_items=None, items=None):
        """
        TagsCollection - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total_items': 'int',
            'items': 'list[Tag]'
        }

        self.attribute_map = {
            'total_items': 'totalItems',
            'items': 'items'
        }

        self._total_items = total_items
        self._items = items

    @property
    def total_items(self):
        """
        Gets the total_items of this TagsCollection.

        :return: The total_items of this TagsCollection.
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """
        Sets the total_items of this TagsCollection.

        :param total_items: The total_items of this TagsCollection.
        :type: int
        """

        self._total_items = total_items

    @property
    def items(self):
        """
        Gets the items of this TagsCollection.

        :return: The items of this TagsCollection.
        :rtype: list[Tag]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this TagsCollection.

        :param items: The items of this TagsCollection.
        :type: list[Tag]
        """

        self._items = items

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
        if not isinstance(other, TagsCollection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
