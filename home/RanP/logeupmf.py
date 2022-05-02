from random import choices


class Pmf:

    def __init__(self, words, right=None, wrong=None):
        self.words = words
        self.cache = None  # <= provide
        self.mag = len(words)
        if right is None:
            self.rights = [1] * self.mag
        else:
            self.rights = right
        if wrong is None:
            self.wrongs = [0] * self.mag
        else:
            self.wrongs = wrong

    @staticmethod
    def check(subj):
        if type(subj) in {float, int}:
            return True
        raise ValueError("Probability is non-numerical")

    def full_count(self):
        count = 0
        for i in self.wrongs:
            if i != 0:
                count += 1
        return count

    def choose_norm(self):
        choix = choices(['v', 'f'], weights=[0.55, 0.45])[0]
        if choix == 'v':
            lst = self.rights
        else:
            lst = self.wrongs
            cn = self.full_count()
            if self.cache not in {None, 'None'}:
                if (cn == 0) or (self.wrongs[self.cache] > 0 and cn == 1):
                    lst = self.rights
        prop_total = 0
        for p in lst:
            prop_total += p
        norms = [i/prop_total for i in lst]
        return norms

    def update(self, ind, data):
        self.check(ind)
        if data:
            current = self.wrongs[ind]
            if current >= 1:
                self.wrongs[ind] = ((current-1)/2)+1
                if self.wrongs[ind] < 1.125:
                    self.wrongs[ind] = 0
                    self.rights[ind] = 1
        else:
            self.wrongs[ind] = 2
            self.rights[ind] = 0
