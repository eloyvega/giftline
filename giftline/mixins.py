from django.contrib.auth.decorators import login_required


"""
Mixin para las vistas basadas en clases que requieren el decorador login_required
"""
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)