from __future__ import annotations
import re
from typing import List

class Terme:
    # تعريف تعابير النمط لتحليل المصطلحات
    RE_TOUS = r"\"[^\"]*\"|[-+]?[\w_\.]+(\(\)?)?|\)|,|[ ]+"
    RE_FONCTION = r"[a-zA-Z][\w_]*\(\)?"
    RE_PARENTHESE_FERMANTE = r"\)"
    RE_VARIABLE = r"[a-zA-Z][\w_]*"
    RE_CONST = r"\-?(\.\d+|\d+(\.\d*)?)|\"[^\"]*\""
    RE_COMMA = r","
    RE_PARENTHESE_OUVRANTE = r"\("
    RE_ESPACE = r"[ ]+"

    # تعريف الدالة __init__ لتهيئة الكائن
    def __init__(self, t_match: str, t_type: str, t_erreur=False) -> None:
        self.match = self.__normlize_match(t_match)
        self.type = t_type
        self.erreur = t_erreur
        if t_type == 'Fonction':
            self.sous_termes: List[Terme] = []

    # تعريف الدالة الخاصة __normlize_match لتنظيف مطابقة المصطلح
    def __normlize_match(self, t_match: str):
        return t_match[:-2] if re.match(
            "^{}$".format(Terme.RE_FONCTION[:-1]),
            t_match
        ) else t_match[:-1] if re.match(
            "^{}$".format(Terme.RE_FONCTION),
            t_match
        ) else t_match

    # تعريف دالة للتحقق من وجود المصطلح في القائمة
    def verifier_occurence(self, termes_liste: List[Terme]):
        if len(termes_liste) == 0:
            return False

        terme = termes_liste[0]
        if self == terme:
            return True

        if terme.type == 'Fonction':
            if terme.verifier_occurence(terme.sous_termes):
                return True
        return terme.verifier_occurence(termes_liste[1:])

    # تعريف دالة للمقارنة بين مصطلحين
    def __eq__(self, other_terme: Terme) -> bool:
        other_terme: Terme
        if type(other_terme) != Terme:
            return False
        if self.match == other_terme.match and self.type == other_terme.type:
            if self.type == 'Fonction':
                if self.sous_termes == other_terme.sous_termes:
                    return True
                else:
                    return False
            else:
                return True
        return False

    # تعريف دالة للتمثيل النصي للمصطلح
    def __str__(self):
        if self.type == 'Fonction':
            return '{}({})'.format(self.match, ', '.join([
                str(aterm) for aterm in self.sous_termes
            ]))
        else:
            return self.match

    # تعريف دالة لإنشاء جدول للمصطلحات
    def terms_table(liste_termes: List[Terme]):
        terms_str = ''
        for terme in liste_termes:
            terms_str += "{}: {}\n".format(
                terme, terme.type
            )

            if terme.type == 'Fonction':
                terms_str += Terme.terms_table(terme.sous_termes)

        return terms_str
