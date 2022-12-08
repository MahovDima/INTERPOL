from django.test import TestCase
from pages.models import CustomUser, WantedPerson, Role


class ModelsTestCase(TestCase):
    def setUp(self):
        Role.objects.create(id=1, role='Администратор')
        CustomUser.objects.create(id=1, first_name='Дмитрий', last_name='Махов', role=Role.objects.get(id=1), username='dima', password='test13')
        WantedPerson.objects.create(name='Уфимцев1')
        WantedPerson.objects.create(name='Уфимцев2', age='19 лет')
        WantedPerson.objects.create(name='Уфимцев3', age='19 лет', briefInfo='Украл автоматы с кофе')
        WantedPerson.objects.create(name='Уфимцев4', age='19 лет', briefInfo='Украл автоматы с кофе', photo='vlad.svg')
        WantedPerson.objects.create(name='Уфимцев5', age='19 лет', briefInfo='Украл автоматы с кофе', photo='vlad.svg', detailInfo='vlad.svg')
        WantedPerson.objects.create(name='Уфимцев6', age='19 лет', briefInfo='Украл автоматы с кофе', photo='vlad.svg', detailInfo='vlad.svg', authorId=CustomUser.objects.get(id=1))

    def test_wantedPerson(self):
        first = WantedPerson.objects.get(name='Уфимцев1')
        second = WantedPerson.objects.get(name='Уфимцев2')
        third = WantedPerson.objects.get(name='Уфимцев3')
        fourth = WantedPerson.objects.get(name='Уфимцев4')
        fifth = WantedPerson.objects.get(name='Уфимцев5')
        sixth = WantedPerson.objects.get(name='Уфимцев6')
        self.assertEqual(first.name, 'Уфимцев1')
        self.assertEqual(second.age, '19 лет')
        self.assertEqual(third.briefInfo, 'Украл автоматы с кофе')
        self.assertEqual(fourth.photo, 'vlad.svg')
        self.assertEqual(fifth.detailInfo, 'vlad.svg')
        self.assertEqual(sixth.authorId.id, 1)
