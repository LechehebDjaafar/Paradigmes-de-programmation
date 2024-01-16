from terme import Terme
from equation import Equation
from typing import List

class Regle:
    # قاعدة 1: استبدال الجهة اليمنى بالجهة اليسرى للمعادلة
    def regle1(gauche: Terme, droite: Terme):
        return Equation(droite, gauche)

    # قاعدة 2: التحقق من مساواة الجهتين في المعادلة
    def regle2(equation: Equation):
        return equation.gauche == equation.droite

    # قاعدة 3: استبدال قائمة من المصطلحات في الجهة اليسرى بالجهة اليمنى
    def regle3(g_sous_termes: List[Terme], d_sous_termes: List[Terme]) -> List[Equation]:
        return [Equation(g_terme, d_terme) for g_terme, d_terme in zip(
            g_sous_termes,
            d_sous_termes
        )]

    # قاعدة 4: استبدال كل حالة ظهور للمصطلح القديم بالمصطلح الجديد في القائمة من المعادلات
    def regle4(equations: List[Equation], sele_eq: Equation):
        if Regle.verifier_occurence(equations, sele_eq.gauche):
            Regle.__terme_remplaceur(equations, sele_eq.gauche, sele_eq.droite)
            return True
        return False

    # التحقق من وجود المصطلح في إحدى المعادلات
    def verifier_occurence(equations: List[Equation], terme: Terme):
        if len(equations) == 0:
            return False

        equation = equations[0]
        if equation.gauche == terme or equation.droite == terme:
            return True

        if equation.gauche.type == 'Fonction':
            if terme.verifier_occurence(equation.gauche.sous_termes):
                return True
        if equation.droite.type == 'Fonction':
            if terme.verifier_occurence(equation.droite.sous_termes):
                return True
        return Regle.verifier_occurence(equations[1:], terme)

    # دالة تقوم بتبديل المصطلح القديم بالمصطلح الجديد في القائمة من المصطلحات
    def __params_remplaceur(sous_termes: List[Terme], old_terme: Terme, new_terme: Terme):
        new_sous_termes: List[Terme] = []
        for terme in sous_termes:
            new_sous_termes.append(
                new_terme if terme == old_terme else terme
            )
            if terme.type == 'Fonction':
                terme.sous_termes = Regle.__params_remplaceur(
                    terme.sous_termes, old_terme, new_terme
                )
        return new_sous_termes

    # دالة تقوم بتبديل المصطلح القديم بالمصطلح الجديد في القائمة من المعادلات
    def __terme_remplaceur(equations: List[Equation], old_terme: Terme, new_terme: Terme):
        if len(equations) == 0:
            return

        equation = equations[0]
        if equation.gauche == old_terme:
            equation.gauche = new_terme
        elif equation.gauche.type == 'Fonction':
            equation.gauche.sous_termes = Regle.__params_remplaceur(
                equation.gauche.sous_termes, old_terme, new_terme
            )
        if equation.droite == old_terme:
            equation.droite = new_terme
        elif equation.droite.type == 'Fonction':
            equation.droite.sous_termes = Regle.__params_remplaceur(
                equation.droite.sous_termes, old_terme, new_terme
            )

        Regle.__terme_remplaceur(equations[1:], old_terme, new_terme)
