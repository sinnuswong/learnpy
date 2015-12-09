class test(object):
      def __init__(self,var):
            self.var=var

      def get(self):
            return self.var
      def getname(self):
            self.name='test'
            return self.name
'''
t=test('hello')
print(t.get())
print(t.getname())
'''
