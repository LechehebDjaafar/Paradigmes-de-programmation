import re
from terme import Terme

class Analyse:
    def analyse_lexical(text: str):
        # تحليل لكلمات النص (lexical analysis)
        return re.sub(Terme.RE_TOUS, lambda amatch: "{}#".format(amatch.group()), text)

    def analyse_syntaxique(liste_termes: list):
        termes_definies = []
        append_to = [termes_definies]
        while len(liste_termes):
            terme = liste_termes[0]
            # إذا كان المصطلح هو دالة
            if re.match("^({})$".format(Terme.RE_FONCTION), terme):
                if terme[-1] == ')':
                    return [
                        Terme(
                            terme,
                            'Erreur, Fonction sans des paramètres',
                            True
                        )
                    ]
                function_term = Terme(
                    terme,
                    'Fonction'
                )
                append_to[-1].append(function_term)
                append_to.append(function_term.sous_termes)

            # إذا كان المصطلح هو متغير
            elif re.match("^({})$".format(Terme.RE_VARIABLE), terme):
                append_to[-1].append(Terme(
                    terme,
                    'Variable'
                ))
            # إذا كان المصطلح هو ثابت
            elif re.match("^({})$".format(Terme.RE_CONST), terme):
                append_to[-1].append(Terme(
                    terme,
                    'Constante'
                ))
            # إذا كان المصطلح هو قوس إغلاق
            elif re.match("^({})$".format(Terme.RE_PARENTHESE_FERMANTE), terme):
                if len(append_to) == 1:
                    return [Terme(
                        'Erreur',
                        'Parenthese fermante supplimentaire',
                        True
                    )]
                else:
                    append_to.pop()
            # إذا لم يتناسب المصطلح مع الأنماط المحددة
            elif not re.match("^(({})|({}))$".format(Terme.RE_COMMA, Terme.RE_ESPACE), terme):
                return [Terme(
                    terme,
                    'Terme pas definie',
                    True
                )]

            liste_termes.pop(0)

        # التحقق من وجود أقواس متبقية
        if len(append_to) > 1:
            return [Terme(
                'Erreur',
                "Un ')' est manquant",
                True
            )]
        return termes_definies

    def termes_separateur(text: str):
        # فصل النص إلى قائمة من المصطلحات
        liste_termes = text.split("#")
        if len(liste_termes) and liste_termes[-1] == "":
            liste_termes.pop()
        return liste_termes
