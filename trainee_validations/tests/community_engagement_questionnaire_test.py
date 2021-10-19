from django.core.exceptions import ValidationError
from django.test import TestCase
from edc_constants.constants import YES, OTHER

from ..form_validators.community_engagement_questionnaire_validator import CommunityEngangementQuestionnaireValidator


class CommunityEngagementQuestionnaireTest(TestCase):

    def setUp(self):
        self.options = {
            'societal_activity': 'Very active',
            'vote': 'vote',
            'problems_in_the_neighbourhood': OTHER,
            'problems_other': 'type_of_work',
            'solutions_to_problems': YES,
        }

    def test_form_valid(self):
        form_validator = CommunityEngangementQuestionnaireValidator(
            cleaned_data=self.options
        )
        try:
            form_validator.validate()
        except ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_societal_activity(self):
        """
        Raise Validation error if participant is
        unemployed and type of job is selected
        """
        cleaned_data = {
            'societal_activity': 'Very active',
            'vote': 'vote',
            'problems_in_the_neighbourhood': OTHER,
            'problems_other': 'type_of_work',
            'solutions_to_problems': YES,
        }

        form_validator = CommunityEngangementQuestionnaireValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertNotIn('employment_type', form_validator._errors)

    def test_problems_other(self):
        """
        Raise Validation error if participant is
        unemployed and type of job is selected
        """
        cleaned_data = {
            'societal_activity': 'Very active',
            'vote': 'vote',
            'problems_in_the_neighbourhood': OTHER,
            'problems_other': None,
            'solutions_to_problems': YES,
        }

        form_validator = CommunityEngangementQuestionnaireValidator(
            cleaned_data=cleaned_data
        )
        self.assertRaises(ValidationError, form_validator.clean)
        self.assertIn('employment_type', form_validator._errors)
