from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import NO, YES, OTHER

from ..form_validators.education_questionnaire_validator import EducationQuestionnaireValidator


class EducationFormTest(TestCase):

    def setUp(self):
        self.options = {
            'work_status': YES,
            'employment_type': OTHER,
            'employment_type_other': 'None',
            'type_of_work': OTHER,
            'type_of_work_other': 'None',
            'salary_range': 'No income',
        }

    def test_form_valid(self):
        form_validator = EducationQuestionnaireValidator(
            cleaned_data=self.options
        )
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_work_status(self):
        """
        Raise Validation error if participant is
        unemployed and type of job is selected
        """
        cleaned_data = {
            'work_status': NO,
            'employment_type': 'Seasonal employment',
            'employment_type_other': None,
            'type_of_work': 'type_of_work',
            'salary_range': 'salary_range',
        }

        form_validator = EducationQuestionnaireValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('employment_type', form_validator._errors)

    def test_work_status_none(self):
        """
        Raise Validation error if participant is
        employed and type of job is selected
        """
        cleaned_data = {
            'work_status': YES,
            'employment_type': None,
            'employment_type_other': None,
            'type_of_work': 'type_of_work',
            'salary_range': 'salary_range',
        }

        form_validator = EducationQuestionnaireValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('employment_type', form_validator._errors)

    def test_employment_types_other(self):
        cleaned_data = {
            'work_status': YES,
            'employment_type': OTHER,
            'employment_type_other': None,
            'type_of_work': 'type_of_work',
            'salary_range': 'salary_range',
        }

        form_validator = EducationQuestionnaireValidator(
            cleaned_data=cleaned_data
        )

        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('employment_type_other', form_validator._errors)

    def test_work_types_other(self):
        cleaned_data = {
            'work_status': NO,
            'employment_type': OTHER,
            'employment_type_other': 'None',
            'type_of_work': OTHER,
            'type_of_work_other': None,
            'salary_range': 'salary_range',
        }

        form_validator = EducationQuestionnaireValidator(
            cleaned_data=cleaned_data
        )

        self.assertRaises(ValidationError, form_validator.clean)
        self.assertNotIn('type_of_work_other', form_validator._errors)
