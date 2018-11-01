from django.db import models

# Create your models here.
class MemeGenerator(models.Model):
    original_sentence = models.CharField(max_length=200)
    changed_to_sentence = models.CharField(max_length=200)
    # def __init__(self,original_sen,changed_to_sen):
    #     self.original_sentence=original_sen
    #     self.changed_to_sentence=changed_to_sen
    #     self.save()
    def make_meme(self,original_sen,changed_to_sen):
        count=0
        li = [i for i in str(original_sen)]
        big_list=[]
        other_li=[i for i in str(changed_to_sen)]
        del other_li[0]    
        while True:
            if li[-1]==' ':
                del li[-1]
                continue
            elif len(li)==1:
                big_list.append(li[0])
                break
            big_list.append(''.join(li))
            del li[-1]   
        while True:
            if count==len(other_li):
                break
            li.append(other_li[count])
            big_list.append(''.join(li))
            count+=1
        return big_list

    

 




