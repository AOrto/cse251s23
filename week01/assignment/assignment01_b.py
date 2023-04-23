import threading
'''
Anne Orton
this is a sum of a number using threads, I am not suppose to use globals in this.
'''

class Charles(threading.Thread): #I was told to not use the name yourthread, or mythread, so Idecided to name it charles
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number
        Sum = 0

    def run(self):
        self.Sum = sum(range(self.number))#I dont know why this is how it decided to work.


def main():
    

   t1 = Charles(10) # this should end up being 55
   t1.start()
   t1.join()
   
   print(f'Charles(10) returns {t1.Sum}') 
    
   assert t1.Sum == 45, f'The sum should equal 45 but instead was {t1.Sum}'
   t2 = Charles(13) # this should end up being 55
   t2.start()
   t2.join()
   #assert SUM == 45, f'The sum should equal 45 but instead was {SUM}'  
   print(f'Charles(10) returns {t2.Sum}') 
   
   assert t2.Sum == 78, f'The sum should equal 78 but instead was {t2.Sum}'

   t3 = Charles(17) # this should end up being 55
   t3.start()
   t3.join()  
   print(f'Charles(17) returns {t3.Sum}') 
    # Repeat, passing in 17
   assert t3.Sum == 136, f'The sum should equal 136 but instead was {t3.Sum}'

if __name__ == '__main__':
    main()
    assert threading.active_count() == 1
