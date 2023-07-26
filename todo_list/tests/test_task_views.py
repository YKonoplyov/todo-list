from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from todo_list.models import Task, Tag

TASK_LIST_URL = reverse("todo_list:task-list")


class PublicTaskViewsTests(TestCase):

    def test_login_not_required_task_list(self):
        response = self.client.get(TASK_LIST_URL)
        self.assertEquals(response.status_code, 200)


class PrivateCarViewsTests(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username="inokentiy",
            password="password123",
        )
        self.user2 = get_user_model().objects.create_user(
            username="vasil",
            password="password123",
        )

        self.tag_home = Tag.objects.create(
            name="home",
        )
        self.tag_work = Tag.objects.create(
            name="work",
        )
        self.task_feed = Task.objects.create(
            content="feed dog",
            user=self.user1
        )
        self.task_feed.tags.add(self.tag_home)
        self.task_fix_bug = Task.objects.create(
            content="fix bug",
            user=self.user2
        )
        self.task_fix_bug.tags.add(self.tag_work)
        self.client.force_login(self.user1)

    def test_retrieve_task_list(self):
        response = self.client.get(TASK_LIST_URL)
        tasks = Task.objects.filter(user__id=self.user1.id)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(list(response.context["task_list"]), list(tasks))

    def test_change_task_statement(self):
        url = reverse("todo_list:task-change", args=[self.task_feed.id])
        self.client.get(url)
        self.task_feed.refresh_from_db()
        self.assertEqual(self.task_feed.is_completed, True)

        self.client.get(url)
        self.task_feed.refresh_from_db()
        self.assertEqual(self.task_feed.is_completed, False)
