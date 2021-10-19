from django.core.exceptions import ValidationError
from edc_constants.constants import NO, YES
from edc_form_validators import FormValidator


class ScreeningFormValidator(FormValidator):

    def clean(self):
        participant_age = self.cleaned_data.get('age_in_years')

        guardian = self.cleaned_data.get('guardian_available')

        citizen = self.cleaned_data.get('citizen')
        legal_marriage = self.cleaned_data.get('legal_marriage')
        marriage_certificate = self.cleaned_data.get('marriage_certificate')
        marriage_certificate_no = self.cleaned_data.get('marriage_certificate_no')

        if participant_age < 0:
            raise ValidationError(
                {'age_in_years': ['Age cant be negative']}
            )

        self.required_if_true(
            participant_age < 18,
            field_required='guardian_available',
            required_msg='Participant is a minor, Guardian must be present'
        )

        self.required_if(
            NO,
            field='citizen',
            field_required='legal_marriage',
        )

        self.applicable_if(
            YES,
            field='legal_marriage',
            field_applicable='marriage_certificate',
        )

        self.required_if_true(
            condition=marriage_certificate == YES,
            field='marriage_certificate',
            field_required='marriage_certificate_no',
        )
