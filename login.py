import kivy
kivy.require('1.8.0')

from main import MainApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(GridLayout):

	def __init__(self, **kwargs):
		self.theapp = kwargs["parent"]
		
		super(LoginScreen, self).__init__(**kwargs)
		#self.row_force_default=True
		#self.row_default_height=40
		self.cols = 2
		self.add_widget(Label(text='User Name'))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label(text='password'))
		self.password = TextInput(password=True, multiline=False)
		self.add_widget(self.password)
		
		def login(instance):
			if self.username.text == "Claus" and self.password.text == "p": 
				self.theapp.dologin()
			else:
				print("login false <%s> and <%s>" % (self.username.text, self.password.text))
		
		button = Button(text='Login', font_size=14)
		button.bind(on_press=login)
		self.add_widget(button)
		
		def close_app(instance):
			#main.MainApp().stop()
			self.theapp.terminate()
			
		button = Button(text='Close', font_size=14)
		button.bind(on_press=close_app)
		self.add_widget(button)
	
#	def validate(self, username, password):
#		if username == password:
#			success = LoginSuccess()
#			success.test()
#		else:
#			self.status.text="Login failed"
