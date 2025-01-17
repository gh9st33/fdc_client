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

class FoodPortion(object):
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
        'amount': 'float',
        'data_points': 'int',
        'gram_weight': 'float',
        'min_year_acquired': 'int',
        'modifier': 'str',
        'portion_description': 'str',
        'sequence_number': 'int',
        'measure_unit': 'MeasureUnit'
    }

    attribute_map = {
        'id': 'id',
        'amount': 'amount',
        'data_points': 'dataPoints',
        'gram_weight': 'gramWeight',
        'min_year_acquired': 'minYearAcquired',
        'modifier': 'modifier',
        'portion_description': 'portionDescription',
        'sequence_number': 'sequenceNumber',
        'measure_unit': 'measureUnit'
    }

    def __init__(self, id=None, amount=None, data_points=None, gram_weight=None, min_year_acquired=None, modifier=None, portion_description=None, sequence_number=None, measure_unit=None):  # noqa: E501
        """FoodPortion - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._amount = None
        self._data_points = None
        self._gram_weight = None
        self._min_year_acquired = None
        self._modifier = None
        self._portion_description = None
        self._sequence_number = None
        self._measure_unit = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if amount is not None:
            self.amount = amount
        if data_points is not None:
            self.data_points = data_points
        if gram_weight is not None:
            self.gram_weight = gram_weight
        if min_year_acquired is not None:
            self.min_year_acquired = min_year_acquired
        if modifier is not None:
            self.modifier = modifier
        if portion_description is not None:
            self.portion_description = portion_description
        if sequence_number is not None:
            self.sequence_number = sequence_number
        if measure_unit is not None:
            self.measure_unit = measure_unit

    @property
    def id(self):
        """Gets the id of this FoodPortion.  # noqa: E501


        :return: The id of this FoodPortion.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FoodPortion.


        :param id: The id of this FoodPortion.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def amount(self):
        """Gets the amount of this FoodPortion.  # noqa: E501


        :return: The amount of this FoodPortion.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FoodPortion.


        :param amount: The amount of this FoodPortion.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def data_points(self):
        """Gets the data_points of this FoodPortion.  # noqa: E501


        :return: The data_points of this FoodPortion.  # noqa: E501
        :rtype: int
        """
        return self._data_points

    @data_points.setter
    def data_points(self, data_points):
        """Sets the data_points of this FoodPortion.


        :param data_points: The data_points of this FoodPortion.  # noqa: E501
        :type: int
        """

        self._data_points = data_points

    @property
    def gram_weight(self):
        """Gets the gram_weight of this FoodPortion.  # noqa: E501


        :return: The gram_weight of this FoodPortion.  # noqa: E501
        :rtype: float
        """
        return self._gram_weight

    @gram_weight.setter
    def gram_weight(self, gram_weight):
        """Sets the gram_weight of this FoodPortion.


        :param gram_weight: The gram_weight of this FoodPortion.  # noqa: E501
        :type: float
        """

        self._gram_weight = gram_weight

    @property
    def min_year_acquired(self):
        """Gets the min_year_acquired of this FoodPortion.  # noqa: E501


        :return: The min_year_acquired of this FoodPortion.  # noqa: E501
        :rtype: int
        """
        return self._min_year_acquired

    @min_year_acquired.setter
    def min_year_acquired(self, min_year_acquired):
        """Sets the min_year_acquired of this FoodPortion.


        :param min_year_acquired: The min_year_acquired of this FoodPortion.  # noqa: E501
        :type: int
        """

        self._min_year_acquired = min_year_acquired

    @property
    def modifier(self):
        """Gets the modifier of this FoodPortion.  # noqa: E501


        :return: The modifier of this FoodPortion.  # noqa: E501
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this FoodPortion.


        :param modifier: The modifier of this FoodPortion.  # noqa: E501
        :type: str
        """

        self._modifier = modifier

    @property
    def portion_description(self):
        """Gets the portion_description of this FoodPortion.  # noqa: E501


        :return: The portion_description of this FoodPortion.  # noqa: E501
        :rtype: str
        """
        return self._portion_description

    @portion_description.setter
    def portion_description(self, portion_description):
        """Sets the portion_description of this FoodPortion.


        :param portion_description: The portion_description of this FoodPortion.  # noqa: E501
        :type: str
        """

        self._portion_description = portion_description

    @property
    def sequence_number(self):
        """Gets the sequence_number of this FoodPortion.  # noqa: E501


        :return: The sequence_number of this FoodPortion.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this FoodPortion.


        :param sequence_number: The sequence_number of this FoodPortion.  # noqa: E501
        :type: int
        """

        self._sequence_number = sequence_number

    @property
    def measure_unit(self):
        """Gets the measure_unit of this FoodPortion.  # noqa: E501


        :return: The measure_unit of this FoodPortion.  # noqa: E501
        :rtype: MeasureUnit
        """
        return self._measure_unit

    @measure_unit.setter
    def measure_unit(self, measure_unit):
        """Sets the measure_unit of this FoodPortion.


        :param measure_unit: The measure_unit of this FoodPortion.  # noqa: E501
        :type: MeasureUnit
        """

        self._measure_unit = measure_unit

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
        if issubclass(FoodPortion, dict):
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
        if not isinstance(other, FoodPortion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
