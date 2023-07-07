from threading import Thread

class panggilan (Thread):
   def __init__(self, name):
      Thread.__init__(self)
      self.name = name

  
   def run(self):
       
       print("Tidak menjawab panggilan dari {}".format(self.name))

def main():
    #pembuatan thread
    bapak = panggilan("Bapak")
    ibu = panggilan("Ibu")
    ade = panggilan("Ade")
    kaka = panggilan ("Kakak")
    kakek = panggilan ("Kakek")
    nenek = panggilan ("Nenek")
    
    bapak.start()
    ibu.start()
    ade.start()
    kaka.start()
    kakek.start()
    nenek.start()

    print("Semua panggilan tidak terjawab")


if __name__ == "__main__":
    main()

    

