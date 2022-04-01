from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from functools import wraps


def require_party_login(fn):
    @wraps(fn)
    def enforce(request, party_name, *args, **kwargs):
        if request.user.username == party_name:
            return fn(request, party_name, *args, **kwargs)
        else:
            return redirect(reverse("party_login", args=[party_name]))

    return enforce
