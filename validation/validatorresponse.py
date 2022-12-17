from .validatorparms import ValidatorParms


class ValidatorResponse:
    """Objeto filtra e valida os valores e regras da requisição"""
    def __init__(self, parms):
        self.error_list = []
        self.password = parms.password
        self.validation_status = False

        for rule in parms.rules:
            match rule['rule']:
                case 'minSize':
                    self.minSize_rule = rule['value']
                    self.check_minSize()
                case 'minUpperCase':
                    self.minUpperCase_rule = rule['value']
                    self.check_upperCase()
                case 'minLowerCase':
                    self.minLowerCase_rule = rule['value']
                    self.check_lowerCase()
                case 'minDigit':
                    self.minDigit_rule = rule['value']
                    self.check_minDigit()
                case 'minSpecialChars':
                    self.minSpecialChars_rule = rule['value']
                    self.check_minSpecialChars()
                case 'noRepeated':
                    self.noRepeated_rule = rule['value']
                    self.check_noRepeated()

        if not self.error_list:
            self.validation_status = True
    
    def final_validation_status(self):
        '''Retorna um dict com o status final e as falhas encontradas (caso haja)'''
        response = {"verify": self.validation_status, "noMatch": self.error_list}
        return response

    def check_minSize(self):
        '''Verifica se a senha tem a quantidade mínima exigida de caracteres'''
        if len(self.password) < self.minSize_rule:
                self.error_list.append("minSize")

    def check_upperCase(self):
        '''Verifica se a senha tem a quantidade mínima exigida de caracteres maiúsculos'''
        total_upper_case = 0
        for char in self.password:
            if char.isupper():
                total_upper_case += 1
        if total_upper_case < self.minUpperCase_rule:
            self.error_list.append("minUpperCase")

    def check_lowerCase(self):
        '''Verifica se a senha tem a quantidade mínima exigida de caracteres minúsculos'''
        total_lower_case = 0
        for char in self.password:
            if char.islower():
                total_lower_case += 1
        if total_lower_case < self.minLowerCase_rule:
            self.error_list.append("minLowerCase")

    def check_minDigit(self):
        '''Verifica se a senha tem a quantidade mínima exigida de dígitos (Ex: 0-9)'''
        total_digit = 0
        for char in self.password:
            if char.isdigit():
                total_digit += 1
        if total_digit < self.minDigit_rule:
            self.error_list.append("minDigit")

    def check_minSpecialChars(self):
        '''Verifica se a senha tem a quantidade mínima exigida de caracteres especiais (Ex: !@#$%^&*()-+\/{}[])'''
        total_special_char = 0
        for char in self.password:
            if not char.isalnum():
                total_special_char += 1
        if total_special_char < self.minSpecialChars_rule:
            self.error_list.append("minSpecialChars")

    def check_noRepeated(self):
        '''Verifica se a senha tem caracteres repetidos em sequência (Ex: aab, abb, bcc)'''
        if self.noRepeated_rule == 1:
            for i, char in enumerate(self.password):
                if self.password[i-1] == char:
                    self.error_list.append("noRepeated")
                    break