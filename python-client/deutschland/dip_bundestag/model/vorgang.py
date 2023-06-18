"""
    Deutscher Bundestag - DIP

    API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.2
    Contact: parlamentsdokumentation@bundestag.de
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.dip_bundestag.exceptions import ApiAttributeError
from deutschland.dip_bundestag.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    OpenApiModel,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


def lazy_import():
    from deutschland.dip_bundestag.model.inkrafttreten import Inkrafttreten
    from deutschland.dip_bundestag.model.verkuendung import Verkuendung
    from deutschland.dip_bundestag.model.vorgang_deskriptor import VorgangDeskriptor
    from deutschland.dip_bundestag.model.vorgang_verlinkung import VorgangVerlinkung

    globals()["Inkrafttreten"] = Inkrafttreten
    globals()["Verkuendung"] = Verkuendung
    globals()["VorgangDeskriptor"] = VorgangDeskriptor
    globals()["VorgangVerlinkung"] = VorgangVerlinkung


class Vorgang(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ("typ",): {
            "VORGANG": "Vorgang",
        },
    }

    validations = {
        ("id",): {
            "regex": {
                "pattern": r"^\d+$",  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (
            bool,
            date,
            datetime,
            dict,
            float,
            int,
            list,
            str,
            none_type,
        )  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "id": (str,),  # noqa: E501
            "typ": (str,),  # noqa: E501
            "vorgangstyp": (str,),  # noqa: E501
            "wahlperiode": (int,),  # noqa: E501
            "aktualisiert": (datetime,),  # noqa: E501
            "titel": (str,),  # noqa: E501
            "beratungsstand": (str,),  # noqa: E501
            "initiative": ([str],),  # noqa: E501
            "datum": (date,),  # noqa: E501
            "abstract": (str,),  # noqa: E501
            "sachgebiet": ([str],),  # noqa: E501
            "deskriptor": ([VorgangDeskriptor],),  # noqa: E501
            "gesta": (str,),  # noqa: E501
            "zustimmungsbeduerftigkeit": ([str],),  # noqa: E501
            "kom": (str,),  # noqa: E501
            "ratsdok": (str,),  # noqa: E501
            "verkuendung": ([Verkuendung],),  # noqa: E501
            "inkrafttreten": ([Inkrafttreten],),  # noqa: E501
            "archiv": (str,),  # noqa: E501
            "mitteilung": (str,),  # noqa: E501
            "vorgang_verlinkung": ([VorgangVerlinkung],),  # noqa: E501
            "sek": (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "id": "id",  # noqa: E501
        "typ": "typ",  # noqa: E501
        "vorgangstyp": "vorgangstyp",  # noqa: E501
        "wahlperiode": "wahlperiode",  # noqa: E501
        "aktualisiert": "aktualisiert",  # noqa: E501
        "titel": "titel",  # noqa: E501
        "beratungsstand": "beratungsstand",  # noqa: E501
        "initiative": "initiative",  # noqa: E501
        "datum": "datum",  # noqa: E501
        "abstract": "abstract",  # noqa: E501
        "sachgebiet": "sachgebiet",  # noqa: E501
        "deskriptor": "deskriptor",  # noqa: E501
        "gesta": "gesta",  # noqa: E501
        "zustimmungsbeduerftigkeit": "zustimmungsbeduerftigkeit",  # noqa: E501
        "kom": "kom",  # noqa: E501
        "ratsdok": "ratsdok",  # noqa: E501
        "verkuendung": "verkuendung",  # noqa: E501
        "inkrafttreten": "inkrafttreten",  # noqa: E501
        "archiv": "archiv",  # noqa: E501
        "mitteilung": "mitteilung",  # noqa: E501
        "vorgang_verlinkung": "vorgang_verlinkung",  # noqa: E501
        "sek": "sek",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(
        cls, id, vorgangstyp, wahlperiode, aktualisiert, titel, *args, **kwargs
    ):  # noqa: E501
        """Vorgang - a model defined in OpenAPI

        Args:
            id (str):
            vorgangstyp (str):
            wahlperiode (int):
            aktualisiert (datetime): Letzte Aktualisierung der Entität
            titel (str):

        Keyword Args:
            typ (str): defaults to "Vorgang", must be one of ["Vorgang", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            beratungsstand (str): [optional]  # noqa: E501
            initiative ([str]): [optional]  # noqa: E501
            datum (date): Datierung des letzten zugehörigen Dokuments. [optional]  # noqa: E501
            abstract (str): [optional]  # noqa: E501
            sachgebiet ([str]): [optional]  # noqa: E501
            deskriptor ([VorgangDeskriptor]): [optional]  # noqa: E501
            gesta (str): GESTA-Ordnungsnummer. [optional]  # noqa: E501
            zustimmungsbeduerftigkeit ([str]): [optional]  # noqa: E501
            kom (str): KOM-Nr.. [optional]  # noqa: E501
            ratsdok (str): Ratsdok-Nr.. [optional]  # noqa: E501
            verkuendung ([Verkuendung]): [optional]  # noqa: E501
            inkrafttreten ([Inkrafttreten]): [optional]  # noqa: E501
            archiv (str): Archivsignatur. [optional]  # noqa: E501
            mitteilung (str): [optional]  # noqa: E501
            vorgang_verlinkung ([VorgangVerlinkung]): [optional]  # noqa: E501
            sek (str): SEK-Nr.. [optional]  # noqa: E501
        """

        typ = kwargs.get("typ", "Vorgang")
        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", True)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.typ = typ
        self.vorgangstyp = vorgangstyp
        self.wahlperiode = wahlperiode
        self.aktualisiert = aktualisiert
        self.titel = titel
        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(
        self, id, vorgangstyp, wahlperiode, aktualisiert, titel, *args, **kwargs
    ):  # noqa: E501
        """Vorgang - a model defined in OpenAPI

        Args:
            id (str):
            vorgangstyp (str):
            wahlperiode (int):
            aktualisiert (datetime): Letzte Aktualisierung der Entität
            titel (str):

        Keyword Args:
            typ (str): defaults to "Vorgang", must be one of ["Vorgang", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            beratungsstand (str): [optional]  # noqa: E501
            initiative ([str]): [optional]  # noqa: E501
            datum (date): Datierung des letzten zugehörigen Dokuments. [optional]  # noqa: E501
            abstract (str): [optional]  # noqa: E501
            sachgebiet ([str]): [optional]  # noqa: E501
            deskriptor ([VorgangDeskriptor]): [optional]  # noqa: E501
            gesta (str): GESTA-Ordnungsnummer. [optional]  # noqa: E501
            zustimmungsbeduerftigkeit ([str]): [optional]  # noqa: E501
            kom (str): KOM-Nr.. [optional]  # noqa: E501
            ratsdok (str): Ratsdok-Nr.. [optional]  # noqa: E501
            verkuendung ([Verkuendung]): [optional]  # noqa: E501
            inkrafttreten ([Inkrafttreten]): [optional]  # noqa: E501
            archiv (str): Archivsignatur. [optional]  # noqa: E501
            mitteilung (str): [optional]  # noqa: E501
            vorgang_verlinkung ([VorgangVerlinkung]): [optional]  # noqa: E501
            sek (str): SEK-Nr.. [optional]  # noqa: E501
        """

        typ = kwargs.get("typ", "Vorgang")
        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                        % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.typ = typ
        self.vorgangstyp = vorgangstyp
        self.wahlperiode = wahlperiode
        self.aktualisiert = aktualisiert
        self.titel = titel
        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(
                    f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                    f"class with read only attributes."
                )
