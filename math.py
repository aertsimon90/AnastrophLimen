class AL:
    """
    AL Number (Anastroph Limen Number)
    Attributes:
        threshold: threshold value
        density: density value
        sign: True = positive, False = negative, None = neutral
    """

    def __init__(self, value, density=None, direction=None):
        direction = (True if value > 0 else False if value < 0 else None) if direction is None else direction
        self.data = (abs(value), 1 if density is None else density, direction)  # (threshold, density, sign)

    def __repr__(self):
        threshold, density, sign = self.data
        sign_str = '+' if sign else '-' if sign == False else '0'
        return f"AL({threshold}, {density}, {sign_str})"

    # ----------------- Measure -----------------
    def measure(self):
        threshold, density, sign = self.data
        if sign is True:
            return threshold
        elif sign is False:
            return -threshold
        else:
            return 0

    # ----------------- Arithmetic Operations -----------------
    def add(self, other):
        if isinstance(other, (int, float)):
            other = AL(other)
        t1, d1, s1 = self.data
        t2, d2, s2 = other.data

        if s1 == s2:  # same sign
            new_t = max(t1, t2)
            new_d = d1 + d2
            new_s = s1
        else:  # opposite sign
            if d1 > d2:
                new_t = max(t1, t2)
                new_d = d1 - d2
                new_s = s1
            elif d2 > d1:
                new_t = max(t1, t2)
                new_d = d2 - d1
                new_s = s2
            else:
                return AL(0)  # neutral

        return AL._from_data(new_t, new_d, new_s)

    def subtract(self, other):
        if isinstance(other, (int, float)):
            other = AL(other)
        t, d, s = other.data
        inv_s = None if s is None else not s
        return self.add(AL._from_data(t, d, inv_s))

    def multiply(self, other):
        # Special rule: AL * 0 = measure value (int)
        if isinstance(other, (int, float)):
            if other == 0:
                return self.measure()  # AL rule
            t, d, s = self.data
            new_d = d * abs(other)
            new_s = s if other >= 0 else not s if s is not None else None
            return AL._from_data(t, new_d, new_s)

        # AL * AL
        t1, d1, s1 = self.data
        t2, d2, s2 = other.data

        if s1 == s2:
            new_s = True
        elif None not in (s1, s2) and s1 != s2:
            new_s = False
        else:
            new_s = None

        new_t = t1 + t2
        new_d = d1 * d2

        return AL._from_data(new_t, new_d, new_s)

    def divide(self, other):
        # Special rule: division by zero returns AL(self.measure())
        if isinstance(other, (int, float)):
            if other == 0:
                return AL(self.measure())  # AL rule for number/0
            t, d, s = self.data
            new_d = d / abs(other)
            new_s = s if other > 0 else not s if s is not None else None
            return AL._from_data(t, new_d, new_s)

        t1, d1, s1 = self.data
        t2, d2, s2 = other.data

        if t2 == 0:
            return AL(t1)  # AL / 0 → AL object

        if s1 == s2:
            new_s = True
        elif None not in (s1, s2) and s1 != s2:
            new_s = False
        else:
            new_s = None

        new_t = t1 - t2
        new_d = d1 // d2 if d2 != 0 else d1

        if new_t < 0:
            new_t = abs(new_t)
            if new_s == True:
                new_s = False
            elif new_s == False:
                new_s = True

        return AL._from_data(new_t, new_d, new_s)

    # ----------------- Other Operators -----------------
    def modulo(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                return AL(self.measure())
            t, d, s = self.data
            new_t = t % abs(other)
            new_d = d % abs(other)
            return AL._from_data(new_t, new_d, s)

        t1, d1, s1 = self.data
        t2, d2, s2 = other.data
        if t2 == 0:
            return AL(self.measure())
        new_t = t1 % t2
        new_d = d1 % d2 if d2 != 0 else d1
        return AL._from_data(new_t, new_d, s1)

    def power(self, other):
        if isinstance(other, (int, float)):
            t, d, s = self.data
            new_t = t ** other
            new_d = d ** other
            return AL._from_data(new_t, new_d, s)

        t1, d1, s1 = self.data
        t2, d2, s2 = other.data
        new_t = t1 ** t2
        new_d = d1 ** d2
        new_s = s1 if s1 == s2 else None
        return AL._from_data(new_t, new_d, new_s)

    # ----------------- Operator Overloading -----------------
    def __add__(self, other): return self.add(other)
    def __sub__(self, other): return self.subtract(other)
    def __mul__(self, other): return self.multiply(other)
    def __truediv__(self, other): return self.divide(other)
    def __floordiv__(self, other): return self.divide(other)
    def __mod__(self, other): return self.modulo(other)
    def __pow__(self, other): return self.power(other)

    def __iadd__(self, other): self.data = self.add(other).data; return self
    def __isub__(self, other): self.data = self.subtract(other).data; return self
    def __imul__(self, other):
        res = self.multiply(other)
        if isinstance(res, AL):
            self.data = res.data
            return self
        else:
            return res  # measure returned
    def __itruediv__(self, other):
        res = self.divide(other)
        if isinstance(res, AL):
            self.data = res.data
            return self
        else:
            return res
    def __ifloordiv__(self, other): return self.__itruediv__(other)
    def __imod__(self, other):
        res = self.modulo(other)
        if isinstance(res, AL):
            self.data = res.data
            return self
        else:
            return res
    def __ipow__(self, other):
        res = self.power(other)
        if isinstance(res, AL):
            self.data = res.data
            return self
        else:
            return res

    # ----------------- Helper -----------------
    @staticmethod
    def _from_data(threshold, density, sign):
        obj = AL(0)
        obj.data = (threshold, density, sign)
        return obj


# ----------------- Python-level zero division helper -----------------
def safe_div(a, b):
    """
    Safe division: if b == 0, return AL(a)
    Works for numbers and AL objects
    """
    if b == 0:
        if isinstance(a, AL):
            return AL(a.measure())
        return AL(a)
    return a / b
