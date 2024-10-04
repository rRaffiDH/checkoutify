from django.urls import path
from main.views import show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id, edit_product, delete_product
# Tugas 4
from main.views import register
from main.views import login_user
from main.views import logout_user

# Tugas 6
from main.views import add_product_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-attribute-entry', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    # Tugas 4
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    # Tugas 5
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'), 
    # Tugas 6
    path('create-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),


]