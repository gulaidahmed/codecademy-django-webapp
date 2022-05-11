# Create view functions within the appropriate views.py file:

def home_view(request):
  name = "Tom"
  text = f"<h1>My name is {name}</h1>"
  return HttpResponse(text)

# Explored how to use class-based views:
class OwnerList(Listview):
  model = Owner
  
# Attach the view function to a route urls.py file:
urlpatterns = [
  path("catalogue/", views.Catalogue.as_view(), name="catalogue"),
]

# How to access data rendered into a template
<!-- /templates/book_list.html -->
 
{% for book in book_list %}
<tr>
  <td>{{ book.title }} </td>
  <td>{{ book.author }} </td>
</tr>

# Make use of Django’s default 404 page with Http404.

# Used dynamic URLs in templates and made use of specific views.
