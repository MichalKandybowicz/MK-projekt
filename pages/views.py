from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

# def books_to_csv(request):  todo zamienić na import ataków do csv?
#     # Create the HttpResponse object with the appropriate CSV header.
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="books.csv"'
#
#     writer = csv.writer(response)
#     writer.writerow(
#         [
#             "id ", "title ", "author ", "date_of_publication ", "book type "
#          ]
#     )
#     books_list = Book.objects.all().order_by("id")
#     for book in books_list:
#         writer.writerow(
#             [
#                 book.id,
#                 book.title,
#                 book.author,
#                 book.date_of_publication,
#                 book.book_type,
#
#              ]
#         )
#     return response
