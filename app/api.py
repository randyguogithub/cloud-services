from flask_appbuilder import ModelRestApi, BaseView, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import db, appbuilder
from .models import ContactGroup, Gender, Contact,PriceGroup


def fill_gender():
    try:
        db.session.add(Gender(name='Male'))
        db.session.add(Gender(name='Female'))
        db.session.commit()
    except:
        db.session.rollback()


db.create_all()
fill_gender()


class ContactModelApi(ModelRestApi):
    resource_name = 'contact'
    datamodel = SQLAInterface(Contact)
    allow_browser_login = True


appbuilder.add_api(ContactModelApi)


class GroupModelApi(ModelRestApi):
    resource_name = 'group'
    datamodel = SQLAInterface(ContactGroup)
    allow_browser_login = True


appbuilder.add_api(GroupModelApi)

class PriceModelApi(ModelRestApi):
    resource_name = 'price'
    datamodel = SQLAInterface(PriceGroup)
    allow_browser_login = True


appbuilder.add_api(PriceModelApi)


class SwaggerViewv1(BaseView):

    default_view = 'method1'

    title = "Example"
    openapi_url = 'http://localhost:5000/api/v1/_openapi'

    @expose('/swagger/')
    def method1(self):
        return self.render_template('v1/v1.html')


appbuilder.add_view(SwaggerViewv1, "Swagger", icon="fa-envelope")

