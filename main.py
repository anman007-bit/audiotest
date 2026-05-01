"""
Тест воспроизведения фоновой музыки на Android.
Только зелёный экран + музыка. Больше ничего не происходит.

Если музыка ЗДЕСЬ играет чисто без прыжков — значит проблема в основной игре
(скорее всего в перерисовке плиток).
Если музыка ЗДЕСЬ ТОЖЕ дёргается — значит проблема в Kivy/телефоне.
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock


class TestApp(App):
    def build(self):
        # Корневой виджет
        root = BoxLayout(orientation='vertical')

        # Зелёный фон
        with root.canvas.before:
            Color(0.2, 0.6, 0.3, 1)  # зелёный
            self.bg_rect = Rectangle(pos=root.pos, size=root.size)

        # Привязка перерисовки фона при изменении размера
        root.bind(size=self._update_bg, pos=self._update_bg)

        # Большая надпись по центру
        label = Label(
            text='ТЕСТ МУЗЫКИ\n\nСлушай 1-2 минуты\nне трогай экран',
            font_size='32sp',
            color=(1, 1, 1, 1),
            halign='center'
        )
        root.add_widget(label)

        # Запускаем музыку через 1 секунду после старта
        # (даём приложению полностью загрузиться)
        Clock.schedule_once(self._start_music, 1.0)

        return root

    def _update_bg(self, instance, value):
        self.bg_rect.pos = instance.pos
        self.bg_rect.size = instance.size

    def _start_music(self, dt):
        """Запуск музыки."""
        try:
            self.bg = SoundLoader.load('sounds/Background.wav')
            if self.bg:
                self.bg.loop = True
                self.bg.volume = 0.5
                self.bg.play()
                print('[TEST] Музыка запущена')
            else:
                print('[TEST] ОШИБКА: файл не загрузился')
        except Exception as e:
            print(f'[TEST] Ошибка: {e}')


if __name__ == '__main__':
    TestApp().run()
