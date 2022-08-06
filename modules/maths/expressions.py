import re
from itertools import chain


class Operators:

    o0 = ["^"]
    o1 = ["*", "/", "|", "%"]
    o2 = ["+", "-"]
    prioritized = [o0, o1, o2]
    operators = list(chain(*prioritized))

    regex = "".join(operators).replace("-", "\-")[::-1]

    def __init__(self, operator=None):
        if operator and (operator not in self.operators):
            raise ValueError(
                f"{operator} invalid. pls submit an operator from {self.operators}"
            )
        self.value = operator

    def __getitem__(self, key):
        return self.operators.__getitem__(key)

    def __repr__(self):
        return self.value


class Expression:

    simplified = False
    atomic = False

    def __init__(self, expression: str, *args, **kwargs):
        if type(expression) != str:
            raise TypeError("gimme a string")

        self.initial = expression
        self.current = self.initial
        self.format()
        self.validate()

        if self.canSimplify():
            self.current = self._simplify()
            self.simplified = True

        self.firstClause, self.operator, self.secondClause = self.split()

    def __getitem__(self, key):
        return self.current.__getitem__(key)

    def __len__(self):
        return len(self.current)

    def __repr__(self):
        if self.atomic:
            return f"{self.current}"
        return f"<{self.firstClause}{self.operator}{self.secondClause}>"

    def validate(self):
        """validates that an expression is valid
        1. check length
        2. check parentheses
        3. check if there inappropriate operator matchings"""
        # len check
        assert len(self), "expression cannot be empty"
        errors = []
        # paren check
        depth = 0
        for char in self:
            depth += char == "("
            depth -= char == ")"
            if depth < 0:
                errors.append(f"{self} is missing an opening parenthesis")
                break
        if depth > 0:
            errors.append(f"{self} is missing an opening parenthesis")

        # valid operator check
        ops = Operators.regex
        r = re.compile(
            f"""
            .*(
            [^{ops}\(]\(     # non-operator followed by open paren:   "1(" 
            |\)[^{ops}\)]    # clsoed paren followed by non-operator: ")1" 
            |[{ops}][{ops}]  # double operator:                       "++" 
            |\(\)            # open-closed parens:                    "()"
            |\([{ops}]       # open paren followed by an operator:    "(+"
            |[{ops}]\)       # operator followed by closed paren:     "+)"
            ).*""",
            re.X,  # this just makes it verbose so comments are ok ^
        )
        if match := r.match(self.current):
            errors.append(f"Invalid expression: {match}")

        if errors:
            raise ValueError(errors)

    def format(self):
        """formats self.current into more acceptable form
        1. removes spaces, replaces double characters with unique phrases
        2. removes unnecessary parentheses
        """
        replacements = {
            " ": "",
            "**": "^",
            "//": "||",
        }
        for replacement in replacements.items():
            self.current = self.current.replace(*replacement)
        blinded_count = self.blindParen().count("~")
        while blinded_count and blinded_count == len(self) - 2:
            self.current = self.current[1:-1]

    def blindParen(self, stression=None):
        """returns stression or self.current with insides of depth-0 parentheses replaced with ~"""
        stression = stression or self.current
        string = []
        depth = 0
        for char in stression:
            depth -= char == ")"
            string.append("~" if depth else char)
            depth += char == "("
        return "".join(string)

    def split(self):
        """
        returns (E1,op,E2) according to first operation to perform
        test pemdas-ordered ops, split on lowest priority one not inside parentheses
        """
        if self.atomic or not self.current:
            return self, None, None

        blinded = self.blindParen()

        split_index = 0  # record where to split self
        for oplist in reversed(Operators.prioritized):
            for op in oplist:
                index = blinded.find(op)
                if index >= 0:
                    split_index = max(split_index, index)
            if split_index:
                break

        if split_index == 0:
            self.atomic = True
            return self, None, None
        return (
            Expression(self[:split_index]),
            Operators(self[split_index]),
            Expression(self[split_index + 1 :]),
        )

    def _simplify(self):
        # Find the fist non-buried operator
        # Simplify and return the phrase before the operator
        ...

    def canSimplify(self):
        return False
