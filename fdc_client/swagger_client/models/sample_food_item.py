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

class SampleFoodItem(object):
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
        'fdc_id': 'int',
        'datatype': 'str',
        'description': 'str',
        'food_class': 'str',
        'publication_date': 'str',
        'food_attributes': 'list[FoodCategory]'
    }

    attribute_map = {
        'fdc_id': 'fdcId',
        'datatype': 'datatype',
        'description': 'description',
        'food_class': 'foodClass',
        'publication_date': 'publicationDate',
        'food_attributes': 'foodAttributes'
    }

    def __init__(self, fdc_id=None, datatype=None, description=None, food_class=None, publication_date=None, food_attributes=None):  # noqa: E501
        """SampleFoodItem - a model defined in Swagger"""  # noqa: E501
        self._fdc_id = None
        self._datatype = None
        self._description = None
        self._food_class = None
        self._publication_date = None
        self._food_attributes = None
        self.discriminator = None
        self.fdc_id = fdc_id
        if datatype is not None:
            self.datatype = datatype
        self.description = description
        if food_class is not None:
            self.food_class = food_class
        if publication_date is not None:
            self.publication_date = publication_date
        if food_attributes is not None:
            self.food_attributes = food_attributes

    @property
    def fdc_id(self):
        """Gets the fdc_id of this SampleFoodItem.  # noqa: E501


        :return: The fdc_id of this SampleFoodItem.  # noqa: E501
        :rtype: int
        """
        return self._fdc_id

    @fdc_id.setter
    def fdc_id(self, fdc_id):
        """Sets the fdc_id of this SampleFoodItem.


        :param fdc_id: The fdc_id of this SampleFoodItem.  # noqa: E501
        :type: int
        """
        if fdc_id is None:
            raise ValueError("Invalid value for `fdc_id`, must not be `None`")  # noqa: E501

        self._fdc_id = fdc_id

    @property
    def datatype(self):
        """Gets the datatype of this SampleFoodItem.  # noqa: E501


        :return: The datatype of this SampleFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this SampleFoodItem.


        :param datatype: The datatype of this SampleFoodItem.  # noqa: E501
        :type: str
        """

        self._datatype = datatype

    @property
    def description(self):
        """Gets the description of this SampleFoodItem.  # noqa: E501


        :return: The description of this SampleFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SampleFoodItem.


        :param description: The description of this SampleFoodItem.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def food_class(self):
        """Gets the food_class of this SampleFoodItem.  # noqa: E501


        :return: The food_class of this SampleFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._food_class

    @food_class.setter
    def food_class(self, food_class):
        """Sets the food_class of this SampleFoodItem.


        :param food_class: The food_class of this SampleFoodItem.  # noqa: E501
        :type: str
        """

        self._food_class = food_class

    @property
    def publication_date(self):
        """Gets the publication_date of this SampleFoodItem.  # noqa: E501


        :return: The publication_date of this SampleFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this SampleFoodItem.


        :param publication_date: The publication_date of this SampleFoodItem.  # noqa: E501
        :type: str
        """

        self._publication_date = publication_date

    @property
    def food_attributes(self):
        """Gets the food_attributes of this SampleFoodItem.  # noqa: E501


        :return: The food_attributes of this SampleFoodItem.  # noqa: E501
        :rtype: list[FoodCategory]
        """
        return self._food_attributes

    @food_attributes.setter
    def food_attributes(self, food_attributes):
        """Sets the food_attributes of this SampleFoodItem.


        :param food_attributes: The food_attributes of this SampleFoodItem.  # noqa: E501
        :type: list[FoodCategory]
        """

        self._food_attributes = food_attributes

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
        if issubclass(SampleFoodItem, dict):
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
        if not isinstance(other, SampleFoodItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other