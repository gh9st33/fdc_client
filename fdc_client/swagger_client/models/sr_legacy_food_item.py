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

class SRLegacyFoodItem(object):
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
        'data_type': 'str',
        'description': 'str',
        'food_class': 'str',
        'is_historical_reference': 'bool',
        'ndb_number': 'int',
        'publication_date': 'str',
        'scientific_name': 'str',
        'food_category': 'FoodCategory',
        'food_nutrients': 'list[FoodNutrient]',
        'nutrient_conversion_factors': 'list[NutrientConversionFactors]'
    }

    attribute_map = {
        'fdc_id': 'fdcId',
        'data_type': 'dataType',
        'description': 'description',
        'food_class': 'foodClass',
        'is_historical_reference': 'isHistoricalReference',
        'ndb_number': 'ndbNumber',
        'publication_date': 'publicationDate',
        'scientific_name': 'scientificName',
        'food_category': 'foodCategory',
        'food_nutrients': 'foodNutrients',
        'nutrient_conversion_factors': 'nutrientConversionFactors'
    }

    def __init__(self, fdc_id=None, data_type=None, description=None, food_class=None, is_historical_reference=None, ndb_number=None, publication_date=None, scientific_name=None, food_category=None, food_nutrients=None, nutrient_conversion_factors=None):  # noqa: E501
        """SRLegacyFoodItem - a model defined in Swagger"""  # noqa: E501
        self._fdc_id = None
        self._data_type = None
        self._description = None
        self._food_class = None
        self._is_historical_reference = None
        self._ndb_number = None
        self._publication_date = None
        self._scientific_name = None
        self._food_category = None
        self._food_nutrients = None
        self._nutrient_conversion_factors = None
        self.discriminator = None
        self.fdc_id = fdc_id
        self.data_type = data_type
        self.description = description
        if food_class is not None:
            self.food_class = food_class
        if is_historical_reference is not None:
            self.is_historical_reference = is_historical_reference
        if ndb_number is not None:
            self.ndb_number = ndb_number
        if publication_date is not None:
            self.publication_date = publication_date
        if scientific_name is not None:
            self.scientific_name = scientific_name
        if food_category is not None:
            self.food_category = food_category
        if food_nutrients is not None:
            self.food_nutrients = food_nutrients
        if nutrient_conversion_factors is not None:
            self.nutrient_conversion_factors = nutrient_conversion_factors

    @property
    def fdc_id(self):
        """Gets the fdc_id of this SRLegacyFoodItem.  # noqa: E501


        :return: The fdc_id of this SRLegacyFoodItem.  # noqa: E501
        :rtype: int
        """
        return self._fdc_id

    @fdc_id.setter
    def fdc_id(self, fdc_id):
        """Sets the fdc_id of this SRLegacyFoodItem.


        :param fdc_id: The fdc_id of this SRLegacyFoodItem.  # noqa: E501
        :type: int
        """
        if fdc_id is None:
            raise ValueError("Invalid value for `fdc_id`, must not be `None`")  # noqa: E501

        self._fdc_id = fdc_id

    @property
    def data_type(self):
        """Gets the data_type of this SRLegacyFoodItem.  # noqa: E501


        :return: The data_type of this SRLegacyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this SRLegacyFoodItem.


        :param data_type: The data_type of this SRLegacyFoodItem.  # noqa: E501
        :type: str
        """
        if data_type is None:
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501

        self._data_type = data_type

    @property
    def description(self):
        """Gets the description of this SRLegacyFoodItem.  # noqa: E501


        :return: The description of this SRLegacyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SRLegacyFoodItem.


        :param description: The description of this SRLegacyFoodItem.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def food_class(self):
        """Gets the food_class of this SRLegacyFoodItem.  # noqa: E501


        :return: The food_class of this SRLegacyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._food_class

    @food_class.setter
    def food_class(self, food_class):
        """Sets the food_class of this SRLegacyFoodItem.


        :param food_class: The food_class of this SRLegacyFoodItem.  # noqa: E501
        :type: str
        """

        self._food_class = food_class

    @property
    def is_historical_reference(self):
        """Gets the is_historical_reference of this SRLegacyFoodItem.  # noqa: E501


        :return: The is_historical_reference of this SRLegacyFoodItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_historical_reference

    @is_historical_reference.setter
    def is_historical_reference(self, is_historical_reference):
        """Sets the is_historical_reference of this SRLegacyFoodItem.


        :param is_historical_reference: The is_historical_reference of this SRLegacyFoodItem.  # noqa: E501
        :type: bool
        """

        self._is_historical_reference = is_historical_reference

    @property
    def ndb_number(self):
        """Gets the ndb_number of this SRLegacyFoodItem.  # noqa: E501


        :return: The ndb_number of this SRLegacyFoodItem.  # noqa: E501
        :rtype: int
        """
        return self._ndb_number

    @ndb_number.setter
    def ndb_number(self, ndb_number):
        """Sets the ndb_number of this SRLegacyFoodItem.


        :param ndb_number: The ndb_number of this SRLegacyFoodItem.  # noqa: E501
        :type: int
        """

        self._ndb_number = ndb_number

    @property
    def publication_date(self):
        """Gets the publication_date of this SRLegacyFoodItem.  # noqa: E501


        :return: The publication_date of this SRLegacyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._publication_date

    @publication_date.setter
    def publication_date(self, publication_date):
        """Sets the publication_date of this SRLegacyFoodItem.


        :param publication_date: The publication_date of this SRLegacyFoodItem.  # noqa: E501
        :type: str
        """

        self._publication_date = publication_date

    @property
    def scientific_name(self):
        """Gets the scientific_name of this SRLegacyFoodItem.  # noqa: E501


        :return: The scientific_name of this SRLegacyFoodItem.  # noqa: E501
        :rtype: str
        """
        return self._scientific_name

    @scientific_name.setter
    def scientific_name(self, scientific_name):
        """Sets the scientific_name of this SRLegacyFoodItem.


        :param scientific_name: The scientific_name of this SRLegacyFoodItem.  # noqa: E501
        :type: str
        """

        self._scientific_name = scientific_name

    @property
    def food_category(self):
        """Gets the food_category of this SRLegacyFoodItem.  # noqa: E501


        :return: The food_category of this SRLegacyFoodItem.  # noqa: E501
        :rtype: FoodCategory
        """
        return self._food_category

    @food_category.setter
    def food_category(self, food_category):
        """Sets the food_category of this SRLegacyFoodItem.


        :param food_category: The food_category of this SRLegacyFoodItem.  # noqa: E501
        :type: FoodCategory
        """

        self._food_category = food_category

    @property
    def food_nutrients(self):
        """Gets the food_nutrients of this SRLegacyFoodItem.  # noqa: E501


        :return: The food_nutrients of this SRLegacyFoodItem.  # noqa: E501
        :rtype: list[FoodNutrient]
        """
        return self._food_nutrients

    @food_nutrients.setter
    def food_nutrients(self, food_nutrients):
        """Sets the food_nutrients of this SRLegacyFoodItem.


        :param food_nutrients: The food_nutrients of this SRLegacyFoodItem.  # noqa: E501
        :type: list[FoodNutrient]
        """

        self._food_nutrients = food_nutrients

    @property
    def nutrient_conversion_factors(self):
        """Gets the nutrient_conversion_factors of this SRLegacyFoodItem.  # noqa: E501


        :return: The nutrient_conversion_factors of this SRLegacyFoodItem.  # noqa: E501
        :rtype: list[NutrientConversionFactors]
        """
        return self._nutrient_conversion_factors

    @nutrient_conversion_factors.setter
    def nutrient_conversion_factors(self, nutrient_conversion_factors):
        """Sets the nutrient_conversion_factors of this SRLegacyFoodItem.


        :param nutrient_conversion_factors: The nutrient_conversion_factors of this SRLegacyFoodItem.  # noqa: E501
        :type: list[NutrientConversionFactors]
        """

        self._nutrient_conversion_factors = nutrient_conversion_factors

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
        if issubclass(SRLegacyFoodItem, dict):
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
        if not isinstance(other, SRLegacyFoodItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
