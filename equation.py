from terme import Terme


class Equation:
    def __init__(self, g_terme: Terme, d_terme: Terme) -> None:
        self.gauche = g_terme
        self.droite = d_terme

        # True if unification is impossible for this equation, False otherwise
        self.erreur = False

    def __str__(self):
        return '{} = {}{}'.format(
            str(self.gauche),
            str(self.droite),
            ' <<<' if self.erreur else ''
        )
