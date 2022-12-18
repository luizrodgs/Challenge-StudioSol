from validation.validatorparms import ValidatorParms
from validation.validatorresponse import ValidatorResponse


class TestClass:
        def test_when_receive_all_rules_should_return_true(self):
                entry = {
                        "password": "aCorint@hians12!",
                        "rules": [
                                {"rule": "minSize","value": 8},
                                {"rule": "minSpecialChars","value": 1},
                                {"rule": "noRepeated","value": 1},
                                {"rule": "minDigit","value": 1},
                                {"rule": "minUpperCase","value": 1},
                                {"rule": "minLowerCase","value": 1}
                                ]
                        }
                should_return = True
                parms = ValidatorParms.from_dict(entry)
                response = ValidatorResponse(parms)
                returned = response.final_validation_status()
                result = returned['verify']
                assert result == should_return

