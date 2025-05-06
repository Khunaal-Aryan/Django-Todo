from django.test import TestCase, Client
from django.urls import reverse
from .models import Todo

class TodoModelTest(TestCase):
    def test_str_representation(self):
        todo = Todo(title="Sample Task")
        self.assertEqual(str(todo), "Sample Task")

    def test_default_completion(self):
        todo = Todo(title="Task")
        self.assertFalse(todo.completed)

class TodoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.todo = Todo.objects.create(title="Initial Task")

    def test_index_view_status_code(self):
        response = self.client.get(reverse('todos:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse('todos:index'))
        self.assertTemplateUsed(response, 'todos/index.html')

    def test_todo_in_context(self):
        response = self.client.get(reverse('todos:index'))
        self.assertIn(self.todo, response.context['todo_list'])  # Adjust context variable as needed
