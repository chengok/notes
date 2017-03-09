# coding: utf-8

'''
super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。


在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照mro进行的

'''


class FooParent(object):  
    def __init__(self):  
        self.parent = 'I\'m the parent.'  
        print 'Parent'  
      
    def bar(self,message):  
        print message,'from Parent'  
  
class FooChild(FooParent):  
    def __init__(self):  
        super(FooChild,self).__init__()  
        print 'Child'  
        # self.parent = 'I\'m the child.' 
          
    def bar(self,message):  
        super(FooChild, self).bar(message)  
        print 'Child bar fuction'  
        print self.parent  
  
if __name__ == '__main__':  
    fooChild = FooChild()  
    fooChild.bar('HelloWorld') 