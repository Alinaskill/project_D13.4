from django.core.management.base import BaseCommand, CommandError
from simpleapp.models import New, Category


class Command(BaseCommand):
    help = 'Удаление категории с подтверждением'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))

        try:
            category = Category.get(name=options['category'])
            New.objects.filter(category == category).delete()
            self.stdout.write(self.style.SUCCESS(
                f'Succesfully deleted all news from category {category.name}'))  # в случае неправильного подтверждения говорим, что в доступе отказано
        except New.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category'))