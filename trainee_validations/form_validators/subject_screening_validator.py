from django.core.exceptions import ValidationError
from edc_constants.constants import NO, NOT_APPLICABLE, YES
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
                'Invalid age input'
            )

        if participant_age < 18 and guardian == NO:
            raise ValidationError(
                'Participant is a minor, guardian is required'
            )

        if citizen == NO:
            if legal_marriage == NOT_APPLICABLE:
                raise ValidationError(
                    'This field is applicable'
                )

        if legal_marriage == YES:
            if marriage_certificate == NOT_APPLICABLE:
                raise ValidationError(
                    'This field is applicable'
                )

        if legal_marriage == NO:
            if marriage_certificate == YES:
                raise ValidationError(
                    'This field is not applicable'
                )

        if marriage_certificate == NO:
            if marriage_certificate_no:
                raise ValidationError(
                    'This field is not required'
                )
