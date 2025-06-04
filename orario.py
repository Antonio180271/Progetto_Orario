class Orario:
    def __init__(self,ore,minuti,secondi):
        if ore < 0 or ore > 23:
            raise ValueError("Ore must be 0..23")
        if minuti < 0 or minuti > 59:
            raise ValueError("Minuti must be 0..59")
        if secondi < 0 or secondi > 59:
            raise ValueError("Secondi must be 0..59")
        self.ore = ore
        self.minuti = minuti
        self.secondi = secondi

    def __str__(self):
        return f"{str(self.ore).zfill(2)}:{str(self.minuti).zfill(2)}:{str(self.secondi).zfill(2)}"

    def aggiungi_ore(self,ore):
        self.ore += ore
        if self.ore > 23:
            self.ore = self.ore % 24

    def aggiungi_secondi(self,secondi):
        secondi_attuali = self.converti_in_secondi()
        secondi_attuali += secondi

        self.ore = secondi_attuali // 3600 % 60
        self.minuti = secondi_attuali // 60 % 60
        self.secondi = secondi_attuali % 60

    def converti_in_secondi(self):
        return self.secondi + self.minuti*60 + self.ore*60**2