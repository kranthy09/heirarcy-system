from django.test import TestCase
from directory.models import Level, SubLevel


class LevelTest(TestCase):

    def setUp(self) -> None:
        Level.objects.create(name="Root Node")
        Level.objects.create(name="Portfolio")
    
    def test_level_name(self):
        root_level = Level.objects.get(name="Root Node")
        portfolio_level = Level.objects.get(name="Portfolio")
        self.assertEqual(
            root_level.name, "Root Node"
        )
        self.assertEqual(
            portfolio_level.name, "Portfolio"
        )

class SubLevelTest(TestCase):

    def setUp(self) -> None:
        parent = Level.objects.create(name="Program")
        project_level = SubLevel.objects.create(name="Project", parent=parent)
    
    def test_sublevel_name(self):
        project_level = SubLevel.objects.get(name="Project")
        self.assertEqual(
            project_level.parent.name, "Program"
        )
        self.assertEqual(
            project_level.name, "Project"
        )