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

class FoodSearchCriteria(object):
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
        'query': 'str',
        'data_type': 'list[str]',
        'page_size': 'int',
        'page_number': 'int',
        'sort_by': 'str',
        'sort_order': 'str',
        'brand_owner': 'str',
        'trade_channel': 'list[str]',
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'query': 'query',
        'data_type': 'dataType',
        'page_size': 'pageSize',
        'page_number': 'pageNumber',
        'sort_by': 'sortBy',
        'sort_order': 'sortOrder',
        'brand_owner': 'brandOwner',
        'trade_channel': 'tradeChannel',
        'start_date': 'startDate',
        'end_date': 'endDate'
    }

    def __init__(self, query=None, data_type=None, page_size=None, page_number=None, sort_by=None, sort_order=None, brand_owner=None, trade_channel=None, start_date=None, end_date=None):  # noqa: E501
        """FoodSearchCriteria - a model defined in Swagger"""  # noqa: E501
        self._query = None
        self._data_type = None
        self._page_size = None
        self._page_number = None
        self._sort_by = None
        self._sort_order = None
        self._brand_owner = None
        self._trade_channel = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None
        if query is not None:
            self.query = query
        if data_type is not None:
            self.data_type = data_type
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order
        if brand_owner is not None:
            self.brand_owner = brand_owner
        if trade_channel is not None:
            self.trade_channel = trade_channel
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def query(self):
        """Gets the query of this FoodSearchCriteria.  # noqa: E501

        Search terms to use in the search. The string may also include standard [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2)  # noqa: E501

        :return: The query of this FoodSearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this FoodSearchCriteria.

        Search terms to use in the search. The string may also include standard [search operators](https://fdc.nal.usda.gov/help.html#bkmk-2)  # noqa: E501

        :param query: The query of this FoodSearchCriteria.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def data_type(self):
        """Gets the data_type of this FoodSearchCriteria.  # noqa: E501

        Optional. Filter on a specific data type; specify one or more values in an array.  # noqa: E501

        :return: The data_type of this FoodSearchCriteria.  # noqa: E501
        :rtype: list[str]
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this FoodSearchCriteria.

        Optional. Filter on a specific data type; specify one or more values in an array.  # noqa: E501

        :param data_type: The data_type of this FoodSearchCriteria.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Branded", "Foundation", "Survey (FNDDS)", "SR Legacy"]  # noqa: E501
        if not set(data_type).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `data_type` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(data_type) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._data_type = data_type

    @property
    def page_size(self):
        """Gets the page_size of this FoodSearchCriteria.  # noqa: E501

        Optional. Maximum number of results to return for the current page. Default is 50.  # noqa: E501

        :return: The page_size of this FoodSearchCriteria.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this FoodSearchCriteria.

        Optional. Maximum number of results to return for the current page. Default is 50.  # noqa: E501

        :param page_size: The page_size of this FoodSearchCriteria.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this FoodSearchCriteria.  # noqa: E501

        Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize)  # noqa: E501

        :return: The page_number of this FoodSearchCriteria.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this FoodSearchCriteria.

        Optional. Page number to retrieve. The offset into the overall result set is expressed as (pageNumber * pageSize)  # noqa: E501

        :param page_number: The page_number of this FoodSearchCriteria.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def sort_by(self):
        """Gets the sort_by of this FoodSearchCriteria.  # noqa: E501

        Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and description.keyword will be description in future releases.  # noqa: E501

        :return: The sort_by of this FoodSearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this FoodSearchCriteria.

        Optional. Specify one of the possible values to sort by that field. Note, dataType.keyword will be dataType and description.keyword will be description in future releases.  # noqa: E501

        :param sort_by: The sort_by of this FoodSearchCriteria.  # noqa: E501
        :type: str
        """
        allowed_values = ["dataType.keyword", "lowercaseDescription.keyword", "fdcId", "publishedDate"]  # noqa: E501
        if sort_by not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_by` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_by, allowed_values)
            )

        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this FoodSearchCriteria.  # noqa: E501

        Optional. The sort direction for the results. Only applicable if sortBy is specified.  # noqa: E501

        :return: The sort_order of this FoodSearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this FoodSearchCriteria.

        Optional. The sort direction for the results. Only applicable if sortBy is specified.  # noqa: E501

        :param sort_order: The sort_order of this FoodSearchCriteria.  # noqa: E501
        :type: str
        """
        allowed_values = ["asc", "desc"]  # noqa: E501
        if sort_order not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_order` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_order, allowed_values)
            )

        self._sort_order = sort_order

    @property
    def brand_owner(self):
        """Gets the brand_owner of this FoodSearchCriteria.  # noqa: E501

        Optional. Filter results based on the brand owner of the food. Only applies to Branded Foods.  # noqa: E501

        :return: The brand_owner of this FoodSearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._brand_owner

    @brand_owner.setter
    def brand_owner(self, brand_owner):
        """Sets the brand_owner of this FoodSearchCriteria.

        Optional. Filter results based on the brand owner of the food. Only applies to Branded Foods.  # noqa: E501

        :param brand_owner: The brand_owner of this FoodSearchCriteria.  # noqa: E501
        :type: str
        """

        self._brand_owner = brand_owner

    @property
    def trade_channel(self):
        """Gets the trade_channel of this FoodSearchCriteria.  # noqa: E501

        Optional. Filter foods containing any of the specified trade channels.  # noqa: E501

        :return: The trade_channel of this FoodSearchCriteria.  # noqa: E501
        :rtype: list[str]
        """
        return self._trade_channel

    @trade_channel.setter
    def trade_channel(self, trade_channel):
        """Sets the trade_channel of this FoodSearchCriteria.

        Optional. Filter foods containing any of the specified trade channels.  # noqa: E501

        :param trade_channel: The trade_channel of this FoodSearchCriteria.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["CHILD_NUTRITION_FOOD_PROGRAMS", "DRUG", "FOOD_SERVICE", "GROCERY", "MASS_MERCHANDISING", "MILITARY", "ONLINE", "VENDING"]  # noqa: E501
        if not set(trade_channel).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `trade_channel` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(trade_channel) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._trade_channel = trade_channel

    @property
    def start_date(self):
        """Gets the start_date of this FoodSearchCriteria.  # noqa: E501

        Filter foods published on or after this date. Format: YYYY-MM-DD  # noqa: E501

        :return: The start_date of this FoodSearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this FoodSearchCriteria.

        Filter foods published on or after this date. Format: YYYY-MM-DD  # noqa: E501

        :param start_date: The start_date of this FoodSearchCriteria.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this FoodSearchCriteria.  # noqa: E501

        Filter foods published on or before this date. Format: YYYY-MM-DD  # noqa: E501

        :return: The end_date of this FoodSearchCriteria.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this FoodSearchCriteria.

        Filter foods published on or before this date. Format: YYYY-MM-DD  # noqa: E501

        :param end_date: The end_date of this FoodSearchCriteria.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

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
        if issubclass(FoodSearchCriteria, dict):
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
        if not isinstance(other, FoodSearchCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
