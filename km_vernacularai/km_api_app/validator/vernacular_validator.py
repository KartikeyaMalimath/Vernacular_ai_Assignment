from km_api_app.validator.ab_base_class import ABCVernacularValidator
from typing import List, Dict, Tuple

class Constants:
    #constants 
    cFilled = "filled"
    cPartial = "partially filled"
    cTrigger = "trigger"
    cParams = "parameters"
    cValue = "value"

class VernacularValidator(ABCVernacularValidator):
    SlotValidationResult = Tuple[bool, bool, str, Dict]

    def validate_finite_values_entity(self, values: List[Dict], supported_values: List[str] = None, invalid_trigger: str = None, key: str = None, support_multiple: bool = True, pick_first: bool = False, **kwargs) -> SlotValidationResult:
        filled = False
        partially_filled = False
        trigger = invalid_trigger
        parameters = {}
        arr = []
        n = len(values)
        count = 0

        for i in values:
            if i[Constants.cValue] in supported_values:
                count += 1
                arr.append(i[Constants.cValue].upper())
        if 0 < n == count:
            filled = True
            trigger = ""
            if pick_first:
                parameters = {key:arr[0]}
            else:
                parameters = {key:arr}
        else:
            if n:
                partially_filled = True
        return filled, partially_filled, trigger, parameters

    def validate_numeric_entity(self, values: List[Dict], invalid_trigger: str = None, key: str = None, support_multiple : bool = True, pick_first: bool = False, constraint = None, var_name = None, **kwargs) -> SlotValidationResult:
        filled = False
        partially_filled = False
        trigger = ""
        parameters = {}
        arr = []
        count = 0
        n = len(values)

        for j in values:
            if constraint is None:
                count += 1
                arr.append(j[Constants.cValue])
                continue
            temp = constraint.replace(var_name, str(j[Constants.cValue]))
            if eval(temp):
                count += 1
                arr.append(j[Constants.cValue])
        if 0 < n == count:
            filled = True
            if pick_first:
                parameters = {key: arr[0]}
            else:
                parameters = {key: arr}
        else:
            trigger = invalid_trigger
            if n:
                partially_filled = True
            if count > 0 and support_multiple:
                if pick_first:
                    parameters = {key: arr[0]}
                else:
                    parameters = {key: arr}
        return filled, partially_filled, trigger, parameters




