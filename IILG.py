import csv
import git  # Asegúrate de tener GitPython instalado
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class IILGApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.input_text = TextInput(hint_text='Introduce la nueva combinación', multiline=False)
        self.meaning_input = TextInput(hint_text='Introduce el significado', multiline=False)
        submit_button = Button(text='Agregar y Hacer Push', on_press=self.add_and_push)
        self.status_label = Label(text='Estado: Esperando...')

        layout.add_widget(self.input_text)
        layout.add_widget(self.meaning_input)
        layout.add_widget(submit_button)
        layout.add_widget(self.status_label)

        return layout

    def add_and_push(self, instance):
        new_combination = self.input_text.text.strip()
        meaning = self.meaning_input.text.strip()
        
        if not new_combination or not meaning:
            self.show_popup("Error", "Ambos campos deben ser llenados.")
            return

        # Leer el archivo CSV y agregar la nueva combinación
        try:
            with open('IILG.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([new_combination, meaning])
        except Exception as e:
            self.show_popup("Error", f"No se pudo escribir en el archivo: {e}")
            return
        
        # Hacer push al repositorio
        try:
            self.push_to_git(new_combination, meaning)
        except Exception as e:
            self.show_popup("Error", f"No se pudo hacer push: {e}")

    def push_to_git(self, combination, meaning):
        repo_path = 'ruta/al/repositorio'  # Cambia esto a la ruta de tu repositorio
        repo = git.Repo(repo_path)
        
        repo.git.add('IILG.csv')
        repo.index.commit(f'Agregada combinación {combination} con significado "{meaning}"')
        origin = repo.remote(name='origin')
        origin.push()
        
        self.status_label.text = 'Estado: Combinación agregada y cambios enviados!'

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    IILGApp().run()
