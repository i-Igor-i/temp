from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalcApp(App):
    def build(self):
        self.nums = []
        gl = GridLayout(cols=1, rows=7,row_default_height=40,row_force_default=True)
        self.SA = 0
        self.mediana = 0
        self.razmah = 0

        def on_enter(instance):
            print(textinput.text)
            self.nums.append(float(textinput.text))
            self.nums = sorted(self.nums)
            print(self.nums)
            textinput.text = ''
            nums_str = ", ".join(str(x) for x in self.nums)
            label_nums.text = nums_str
            try:
                if len(self.nums) > 1:
                    self.SA = sum(self.nums) / len(self.nums)
                    self.SA = round(self.SA, 2)
                    print(self.SA)
                if len(self.nums)%2!=0:
                    self.mediana = self.nums[len(self.nums)//2]
                    print(self.mediana)
                else:
                    self.mediana = (self.nums[len(self.nums)//2-1]+self.nums[len(self.nums)//2])/2
                    self.mediana = round(self.mediana, 2)
                    print(self.mediana)
                self.razmah = max(self.nums)-min(self.nums)
            except Exception as ex:
                print(ex)
            label_sa.text = f"СА: {self.SA}"
            label_mediana.text = f"медиана: {self.mediana}"
            label_razmah.text = f"размах: {self.razmah}"

        def reset(*args):
            self.nums = []
            print(self.nums)
            nums_str = ", ".join(str(x) for x in self.nums)
            label_nums.text = nums_str
            label_sa.text = f"СА: 0"
            label_mediana.text = f"медиана: 0"
            label_razmah.text = f"размах: 0"
        label_sa = Label(color="white", bold=True, text=f"СА: {self.SA}")
        label_mediana = Label(color="white", bold=True,text=f"медиана: {self.mediana}")
        label_razmah = Label(color="white",bold=True,text=f"размах: {self.razmah}")
        textinput = TextInput(input_filter='float',multiline=False)
        textinput.bind(on_text_validate=on_enter)
        label_nums = Label(color="white",bold=True)
        reset_button = Button(text="reset",bold=True)
        reset_button.bind(on_press=reset)
        gl.add_widget(textinput)
        gl.add_widget(label_nums)
        gl.add_widget(label_sa)
        gl.add_widget(label_mediana)
        gl.add_widget(label_razmah)
        gl.add_widget(reset_button)

        return gl

if __name__ == "__main__":
    CalcApp().run()