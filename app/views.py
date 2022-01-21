from django.shortcuts import render
from .models import Book
from django.views.generic import ListView

hiragana = ["あ", "い", "う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ",
            "て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や",
            "ゆ","よ","ら","り","る","れ","ろ","わ","を","ん"]

alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v",
             "w","x","y","z"]


class BookListView(ListView):
    model = Book
    template_name = 'app/index.html'
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
       context = super(BookListView, self).get_context_data(**kwargs)
       context['hiragana'] = hiragana
       context['alphabets'] = alphabets
       return context
   
class BookFilterView(ListView):

    template_name = 'app/index.html'
    paginate_by = 4
    
    def get_queryset(self):
        """カテゴリでの絞り込み"""
        search_text = self.kwargs['q']
        queryset = Book.objects.filter(name__istartswith=search_text).order_by('name')
        
        return queryset

   
    def get_context_data(self, **kwargs):
       context = super(BookFilterView, self).get_context_data(**kwargs)
       context['hiragana'] = hiragana
       context['alphabets'] = alphabets
       return context