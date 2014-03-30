import kivy
import login
import galaxyportal
kivy.require('1.8.0')

from kivy.app import App
from kivy.logger import Logger
	
class LoginSuccess():
	def test(self):
		self.clear_widgets()
		self.add_widget(Label(text='Success'))
		
class MainApp(App):
	icon = 'dna-th.png'
	title = 'Galaxy Portal'
		
	def build(self):
		return login.LoginScreen(parent=self)
	#	if loginscreen:
	#		Logger.info('Login Authorized')
		#	return GalaxyPortal();
		
	def on_start(self):
		Logger.info('Do app startup work')
 
	def on_stop(self):
		Logger.critical('Do app shutdown work')
	
	def terminate(self):
		print('The close button <%s> is being pressed' % self.__str__)
		#App().close()
		
	def dologin(self):
		return galaxyportal.GalaxyPortal()

if __name__ == '__main__':
	MainApp().run()
	