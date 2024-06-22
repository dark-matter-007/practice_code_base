from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import ILeftBody, ThreeLineAvatarIconListItem, ImageLeftWidget
import sqlite3


class TaskListItem(ThreeLineAvatarIconListItem):
    task_id = None
    task = None
    is_done = BooleanProperty(False)


class TaskManagerApp(MDApp):
    conn = None
    cursor = None

    def on_start(self):
        self.theme_cls.primary_palette = 'Blue'
        self.create_database()

    def build(self):
        screen = MDScreen()

        self.task_list = self.create_task_list()
        screen.add_widget(self.task_list)

        add_task_layout = MDBoxLayout(padding=20, size_hint_y=None, height='48dp')
        self.task_input = MDTextField(hint_text='Enter task', size_hint_x=None, width='200dp')
        add_task_layout.add_widget(self.task_input)

        add_task_button = MDIconButton(icon='plus', on_release=self.add_task)
        add_task_layout.add_widget(add_task_button)

        screen.add_widget(add_task_layout)

        return screen

    def create_database(self):
        self.conn = sqlite3.connect(':memory:')  # In-memory SQLite3 database for simplicity
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                               (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, is_done INTEGER)''')
        self.conn.commit()

    def create_task_list(self):
        task_list = TaskList()
        self.load_tasks(task_list)
        return task_list

    def load_tasks(self, task_list):
        task_list.clear_widgets()
        self.cursor.execute('SELECT * FROM tasks')
        rows = self.cursor.fetchall()
        for row in rows:
            task_id, task, is_done = row
            task_widget = TaskListItem()
            task_widget.task_id = task_id
            task_widget.task = task
            task_widget.is_done = bool(is_done)
            task_widget.on_checkbox = self.update_task
            task_widget.on_delete = self.delete_task
            task_list.add_widget(task_widget)

    def add_task(self, *args):
        task = self.task_input.text
        if task:
            self.cursor.execute('INSERT INTO tasks (task, is_done) VALUES (?, ?)', (task, 0))
            self.conn.commit()
            self.load_tasks(self.task_list)
            self.task_input.text = ''

    def update_task(self, task_id, is_done):
        self.cursor.execute('UPDATE tasks SET is_done=? WHERE id=?', (int(is_done), task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        self.cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
        self.conn.commit()
        self.load_tasks(self.task_list)


class TaskList(ILeftBody, MDBoxLayout):
    orientation = 'vertical'
    adaptive_height = True
    spacing = '8dp'
   
TaskManagerApp().run()