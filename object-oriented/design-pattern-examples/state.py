class AuthenticationState(object):

   name = "authState"
   allowed = []

   def toggleAuth(self, authState):
      #--- change authentication status ---#
      if authState.name in self.allowed:
         print('Currently:',self,' => Changing authentication status',authState.name)
         self.__class__ = authState
      else:
         print('Currently:',self,' => Changing status',authState.name,'not possible.')

   def __str__(self):
      return self.name

class LoggedOut(AuthenticationState):
   name = "logged out"
   allowed = ['logged in']

class LoggedIn(AuthenticationState):
   name = "logged in"
   allowed = ['logged out']


class AdminPanel(object):
   def __init__(self,):
      self.authState = LoggedOut()
   
   def change(self, state):
      self.authState.toggleAuth(state)

if __name__ == "__main__":
   adminPanel = AdminPanel()
   adminPanel.change(LoggedIn)
   adminPanel.change(LoggedOut)
   adminPanel.change(LoggedIn)
   adminPanel.change(LoggedOut)
