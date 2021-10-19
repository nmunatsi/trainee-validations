from django.core.exceptions import ValidationError
from edc_constants.constants import NO, YES
from edc_form_validators import FormValidator


class ConsentFormValidator(FormValidator):
    def clean(self):
        screening_identifier=self.cleaned_data.get('screening_identifier')
        screening_identifier=self.cleaned_data.get('subject_identifier')
        first_name=self.cleaned_data.get('first_name')
        last_name=self.cleaned_data.get('last_name')
        initials=self.cleaned_data.get('initials')
        gender=self.cleaned_data.get('gender')
        language=self.cleaned_data.get('language')
        consent_datetime=self.cleaned_data.get('consent_datetime')
        is_dob_estimated=self.cleaned_data.get('is_dob_estimated')
        identity=self.cleaned_data.get('identity')
        identity_type=self.cleaned_data.get('identity_type')
        confirm_identity=self.cleaned_data.get('confirm_identity')
        comment=self.cleaned_data.get('comment')