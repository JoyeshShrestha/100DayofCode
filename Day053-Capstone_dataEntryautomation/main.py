from Zilloproperty import ZilloProperty
from FillForm import FillForm
Zillio = ZilloProperty()

Zillio.get_info()

form = FillForm()
form.fill_form(Zillio.all_info_list)
