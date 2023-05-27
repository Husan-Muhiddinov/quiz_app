from django import forms
from .models import Test, Question

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('title', 'category', 'maximum_attemps', 'start_date', 'end_date', 'pass_percentage')

    def save(self, request, commit=True):
        test= self.instance
        test.author = request.user    # Testni kim qo'shishini  bilishimiz uchun '"Save"' funksiyasini yozdik 
        super().save(commit)
        return test.id
    
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question', 'a','b','c','d','true_answer')
    submit_and_exit=forms.BooleanField(required=False)  # agar bu check(belgilan) bo'lgan bo'lsa boshqa sahifaga o'tib ketadi, belgilanmagan bo'lsa shu sahifaga qoladi

    def save(self, test_id, commit=True):
        question=self.instance
        question.test = Test.objects.get(id=test_id)       # Qaysi test ga savol qo'shishimizni bilishimiz uchun '"Save"' funksiyasini yozdik 
        super().save(commit)
        return question