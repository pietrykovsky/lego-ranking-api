from django.test import TestCase

from ..tasks import refresh_database

from ..models import LegoSet

class TasksTests(TestCase):
    """Test celery tasks."""

    def test_refresh_database_success(self):
        """Test refresh_database fills the database with legosets."""
        refresh_database()
        legosets = LegoSet.objects.all()
        self.assertNotEqual(legosets, None)