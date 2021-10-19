from edc_constants.constants import OTHER
from edc_form_validators import FormValidator


class CommunityEngangementQuestionnaireValidator(FormValidator):
    def clean(self):

        self.m2m_other_specify(
            OTHER,
            m2m_field='problems_in_the_neighbourhood',
            field_other='problems_other'
        )

        self.require_together(
            field='problems_other',
            field_required='solutions_to_problems'
        )
