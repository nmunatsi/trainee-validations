from edc_constants.constants import OTHER, YES
from edc_form_validators import FormValidator


class EducationQuestionnaireValidator(FormValidator):

    def clean(self):

        self.required_if(
            YES,
            field='work_status',
            field_required='employment_type',
        )

        self.required_if(
            OTHER,
            field='employment_type',
            field_required='employment_type_other'
        )

        self.required_if(
            OTHER,
            field='type_of_work',
            field_required='type_of_work_other'
        )
