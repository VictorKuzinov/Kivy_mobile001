# Координаты
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from plyer import gps


class GPSApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Нажмите кнопку для получения местоположения")
        self.layout.add_widget(self.label)

        self.button = Button(text="Получить местоположение", background_color=(1, 0, 0, 1), font_size=32)
        self.button.bind(on_press=self.get_location)
        self.layout.add_widget(self.button)

        return self.layout

    def get_location(self, instance):
        try:
            gps.configure(on_location=self.on_location)
            gps.start(minTime=1000, minDistance=0)
        except NotImplementedError:
            self.label.text = "Ошибка: GPS не поддерживается на этом устройстве."

    def on_location(self, **kwargs):
        latitude = kwargs.get('lat')
        longitude = kwargs.get('lon')
        self.label.text = f"Широта: {latitude}, Долгота: {longitude}"


if __name__ == '__main__':
    GPSApp().run()
