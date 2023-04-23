'''
Anne Orton
this code is designed to use threading to get the sum up to the number input.
this specifically uses a global value.
'''

import threading

SUM=0

      
class MyThread(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        global SUM
        SUM = sum(range(self.number))
       
      
def main():
    # I left the asserts in to test the that the code works, they are currently just commented out
   t1 = MyThread(10) # this should end up being 45
   t1.start()
   t1.join()
   assert SUM == 45, f'The sum should equal 45 but instead was {SUM}'  
   print(f'{SUM= }') 
   
   t2 = MyThread(13) # this should end up being 78
   t2.start()
   t2.join()
   assert SUM == 78, f'The sum should equal 78 but instead was {SUM}' 
   print(f'{SUM= }') 

   t3 = MyThread(17) # this should end up being 136
   t3.start()
   t3.join()
   assert SUM == 136, f'The sum should equal 136 but instead was {SUM}'
   print(f'{SUM= }') 


if __name__ == '__main__':
      main()



