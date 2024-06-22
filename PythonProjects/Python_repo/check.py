from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import MDList, OneLineAvatarListItem
from kivymd.uix.selectioncontrol import MDCheckbox

Builder.load_string("""
<EditorScreen>:
    orientation: "vertical"
    spacing: "12dp"
    padding: "12dp"
    
    editor: editor
    checklist: checklist
    
    MDTextField:
        id: editor
        hint_text: "Enter text here"
        mode: "rectangle"
        multiline: True
        size_hint_y: 0.6
        
    MDList:
        id: checklist
        size_hint_y: 0.3
        
    MDRaisedButton:
        text: "Save"
        size_hint_y: 0.1
        on_release: root.save_text()
""")

class EditorScreen(MDScreen):
    def save_text(self):
        with open("text.txt", "w") as f:
            f.write(self.editor.text)
            
        with open("checklist.txt", "w") as f:
            for item in self.checklist.children:
                if isinstance(item, OneLineAvatarListItem):
                    text = item.text.strip()
                    checked = item.checkbox.active
                    f.write(f"{text}:{checked}\n")

    def load_checklist(self):
        with open("checklist.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    text, checked = line.split(":")
                    checked = True if checked == "True" else False
                    item = OneLineAvatarListItem(text=text)
                    item.add_widget = MDCheckbox(active=checked)
                    self.checklist.add_widget(item)

class TextEditorApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        screen = EditorScreen()
        screen.load_checklist()
        return screen

if __name__ == '__main__':
    TextEditorApp().run()
