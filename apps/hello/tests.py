from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Person


class ShowPersonTest(TestCase):
    """Testing the show PersonalData template
    Getting a data in DB for template
    """

    def setUp(self):
        """
        Creating a data in DB for template
        """
        self.bio = Person.objects.get(pk=1)

    def test_index_person_template(self):
        """Testing usage of the needed templates.
        First checking the status code, then checking templates.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hello/index.html',
                                'hello/base.html')

    def test_index_person_hardcoded_data(self):
        """Testing hardcoded data in template.
        Testing that hardcoded data is in response
        """
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Name')
        self.assertContains(response, 'Email')
        self.assertContains(response, 'Last name')
        self.assertContains(response, 'Jabber')
        self.assertContains(response, 'Skype')


class PersonalDataModelTest(TestCase):
    """Test for the Bio model.
    """

    def create_model_data(self, first_name='name', last_name='last name',
                          email='email@mail.com', jabber='jid@42cc.co',
                          skype='skype', birthday='2000-02-03'):
        """Creating initial data for testing.
        :param first_name: Name of the person
        :param last_name: Surname of the person
        :param email: Email of the person
        :param jabber: JID of the person
        :param skype: Skype of the person
        :param birthday: Date of birth of the person
        :return: PersonalData object
        """
        return Person.objects.create(first_name=first_name,
                                     last_name=last_name,
                                     email=email,
                                     jabber=jabber,
                                     skype=skype,
                                     birthday=birthday)

    def test_person_creation(self):
        """Testing that we will receive a PersonalData model.
        Creating the model then checking it
        """
        personal_data = self.create_model_data()
        self.assertTrue(isinstance(personal_data, Person))


class PersonModelDataInTemplateTest(TestCase):
    def setUp(self):
        """
        Getting a data in DB for template
        """
        self.bio = Person.objects.get(pk=1)

    def test_model_data_in_template(self):
        """Testing if data from db is in template.
        Comparison of object with
        the response of rendering the template.
        """
        response = self.client.get(reverse('index'))
        self.assertContains(response, self.bio.first_name)
        self.assertContains(response, self.bio.last_name)
