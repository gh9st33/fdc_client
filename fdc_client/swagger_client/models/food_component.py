# coding: utf-8

"""
    Food Data Central API

    The FoodData Central API provides REST access to FoodData Central (FDC). It is intended primarily to assist application developers wishing to incorporate nutrient data into their applications or websites.   To take full advantage of the API, developers should familiarize themselves with the database by reading the database documentation available via links on [Data Type Documentation](https://fdc.nal.usda.gov/data-documentation.html). This documentation provides the detailed definitions and descriptions needed to understand the data elements referenced in the API documentation.      Additional details about the API including rate limits, access, and licensing are available on the [FDC website](https://fdc.nal.usda.gov/api-guide.html)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FoodComponent(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'data_points': 'int',
        'gram_weight': 'float',
        'is_refuse': 'bool',
        'min_year_acquired': 'int',
        'percent_weight': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'data_points': 'dataPoints',
        'gram_weight': 'gramWeight',
        'is_refuse': 'isRefuse',
        'min_year_acquired': 'minYearAcquired',
        'percent_weight': 'percentWeight'
    }

    def __init__(self, id=None, name=None, data_points=None, gram_weight=None, is_refuse=None, min_year_acquired=None, percent_weight=None):  # noqa: E501
        """FoodComponent - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._data_points = None
        self._gram_weight = None
        self._is_refuse = None
        self._min_year_acquired = None
        self._percent_weight = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if data_points is not None:
            self.data_points = data_points
        if gram_weight is not None:
            self.gram_weight = gram_weight
        if is_refuse is not None:
            self.is_refuse = is_refuse
        if min_year_acquired is not None:
            self.min_year_acquired = min_year_acquired
        if percent_weight is not None:
            self.percent_weight = percent_weight

    @property
    def id(self):
        """Gets the id of this FoodComponent.  # noqa: E501


        :return: The id of this FoodComponent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FoodComponent.


        :param id: The id of this FoodComponent.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FoodComponent.  # noqa: E501


        :return: The name of this FoodComponent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FoodComponent.


        :param name: The name of this FoodComponent.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def data_points(self):
        """Gets the data_points of this FoodComponent.  # noqa: E501


        :return: The data_points of this FoodComponent.  # noqa: E501
        :rtype: int
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this FoodComponent.


        :param data_points: The data_points of this FoodComponent.  # noqa: E501
        :type: int
        """

        self._data_points = data_points

    @property
    def gram_weight(self):
        """Gets the gram_weight of this FoodComponent.  # noqa: E501


        :return: The gram_weight of this FoodComponent.  # noqa: E501
        :rtype: float
        """
        return self._gram_weight

    @gram_weight.setter
    def gram_weight(self, gram_weight):
        """Sets the gram_weight of this FoodComponent.


        :param gram_weight: The gram_weight of this FoodComponent.  # noqa: E501
        :type: float
        """

        self._gram_weight = gram_weight

    @property
    def is_refuse(self):
        """Gets the is_refuse of this FoodComponent.  # noqa: E501


        :return: The is_refuse of this FoodComponent.  # noqa: E501
        :rtype: bool
        """
        return self._is_refuse

    @is_refuse.setter
    def is_refuse(self, is_refuse):
        """Sets the is_refuse of this FoodComponent.


        :param is_refuse: The is_refuse of this FoodComponent.  # noqa: E501
        :type: bool
        """

        self._is_refuse = is_refuse

    @property
    def min_year_acquired(self):
        """Gets the min_year_acquired of this FoodComponent.  # noqa: E501


        :return: The min_year_acquired of this FoodComponent.  # noqa: E501
        :rtype: int
        """
        return self._min_year_acquired

    @min_year_acquired.setter
    def min_year_acquired(self, min_year_acquired):
        """Sets the min_year_acquired of this FoodComponent.


        :param min_year_acquired: The min_year_acquired of this FoodComponent.  # noqa: E501
        :type: int
        """

        self._min_year_acquired = min_year_acquired

    @property
    def percent_weight(self):
        """Gets the percent_weight of this FoodComponent.  # noqa: E501


        :return: The percent_weight of this FoodComponent.  # noqa: E501
        :rtype: float
        """
        return self._percent_weight

    @percent_weight.setter
    def percent_weight(self, percent_weight):
        """Sets the percent_weight of this FoodComponent.


        :param percent_weight: The percent_weight of this FoodComponent.  # noqa: E501
        :type: float
        """

        self._percent_weight = percent_weight

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(FoodComponent, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FoodComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
